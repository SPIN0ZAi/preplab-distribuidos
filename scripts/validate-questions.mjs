import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const lab1Path = path.resolve(__dirname, '../src/data/lab1.json');
const lab2Path = path.resolve(__dirname, '../src/data/lab2.json');

const ALLOWED_DIFFICULTIES = new Set(['easy', 'medium', 'hard']);
const ALLOWED_TYPES = new Set(['single', 'multi', 'truefalse']);

function validateQuestion(q, index, labNum, seenIds, seenQuestions, errors) {
  const prefix = `[Lab ${labNum} | Index ${index} | ID ${q?.id || 'MISSING'}]`;

  if (!q || typeof q !== 'object') {
    errors.push(`${prefix} Question is not an object.`);
    return;
  }

  // 1. Check ID
  if (!q.id || typeof q.id !== 'string') {
    errors.push(`${prefix} Missing or non-string 'id'.`);
  } else {
    if (seenIds.has(q.id)) {
      errors.push(`${prefix} Duplicate ID '${q.id}'.`);
    }
    seenIds.add(q.id);
  }

  // 2. Check lab number
  if (q.lab !== labNum) {
    errors.push(`${prefix} Expected lab ${labNum}, got ${q.lab}.`);
  }

  // 3. Topic
  if (!q.topic || typeof q.topic !== 'string' || !q.topic.trim()) {
    errors.push(`${prefix} Missing or empty 'topic'.`);
  }

  // 4. Difficulty
  if (!ALLOWED_DIFFICULTIES.has(q.difficulty)) {
    errors.push(`${prefix} Invalid difficulty '${q.difficulty}'. Allowed: easy, medium, hard.`);
  }

  // 5. Type
  if (!ALLOWED_TYPES.has(q.type)) {
    errors.push(`${prefix} Invalid type '${q.type}'. Allowed: single, multi, truefalse.`);
  }

  // 6. Question text & duplicate check
  if (!q.question || typeof q.question !== 'string' || !q.question.trim()) {
    errors.push(`${prefix} Missing or empty 'question' text.`);
  } else {
    const normalizedText = q.question.trim().toLowerCase().replace(/\s+/g, ' ');
    if (seenQuestions.has(normalizedText)) {
      errors.push(`${prefix} Duplicate question text: "${q.question.slice(0, 60)}..." (previously seen as ID '${seenQuestions.get(normalizedText)}')`);
    } else {
      seenQuestions.set(normalizedText, q.id);
    }
  }

  // 7. Options
  if (!Array.isArray(q.options) || q.options.length < 2) {
    errors.push(`${prefix} 'options' must be an array with at least 2 items.`);
    return;
  }

  const optionIds = new Set();
  for (let i = 0; i < q.options.length; i++) {
    const opt = q.options[i];
    if (!opt || typeof opt !== 'object') {
      errors.push(`${prefix} Option at index ${i} is not an object.`);
      continue;
    }
    if (!opt.id || typeof opt.id !== 'string') {
      errors.push(`${prefix} Option at index ${i} missing valid string 'id'.`);
    } else {
      if (optionIds.has(opt.id)) {
        errors.push(`${prefix} Duplicate option id '${opt.id}'.`);
      }
      optionIds.add(opt.id);
    }
    if (!opt.text || typeof opt.text !== 'string' || !opt.text.trim()) {
      errors.push(`${prefix} Option '${opt.id}' has empty or invalid text.`);
    }
  }

  // 8. Correct answers
  if (!Array.isArray(q.correct) || q.correct.length === 0) {
    errors.push(`${prefix} 'correct' must be a non-empty array of option IDs.`);
  } else {
    for (const corrId of q.correct) {
      if (!optionIds.has(corrId)) {
        errors.push(`${prefix} Correct option ID '${corrId}' does not exist in options: [${Array.from(optionIds).join(', ')}].`);
      }
    }
    if (q.type === 'single' && q.correct.length !== 1) {
      errors.push(`${prefix} Type 'single' must have exactly 1 correct answer, got ${q.correct.length}.`);
    }
    if (q.type === 'truefalse' && q.correct.length !== 1) {
      errors.push(`${prefix} Type 'truefalse' must have exactly 1 correct answer, got ${q.correct.length}.`);
    }
  }

  // 9. Explanations
  if (!q.explanation || typeof q.explanation !== 'object') {
    errors.push(`${prefix} Missing 'explanation' object.`);
  } else {
    if (!q.explanation.correct || typeof q.explanation.correct !== 'string' || !q.explanation.correct.trim()) {
      errors.push(`${prefix} Missing or empty 'explanation.correct'.`);
    }

    if (!q.explanation.wrong || typeof q.explanation.wrong !== 'object') {
      errors.push(`${prefix} Missing 'explanation.wrong' object.`);
    } else {
      const correctSet = new Set(Array.isArray(q.correct) ? q.correct : []);
      // Every option not in correct must have an explanation in explanation.wrong
      for (const optId of optionIds) {
        if (!correctSet.has(optId)) {
          const wrongExpl = q.explanation.wrong[optId];
          if (!wrongExpl || typeof wrongExpl !== 'string' || !wrongExpl.trim()) {
            errors.push(`${prefix} Missing wrong explanation for option '${optId}'.`);
          }
        }
      }
    }
  }

  // 10. Source
  if (!q.source || typeof q.source !== 'string' || !q.source.trim()) {
    errors.push(`${prefix} Missing or empty 'source' field.`);
  }
}

function runValidation() {
  console.log('🔍 Validating question bank for Lab 1 and Lab 2...\n');

  if (!fs.existsSync(lab1Path)) {
    console.error(`❌ Lab 1 file not found at: ${lab1Path}`);
    process.exit(1);
  }
  if (!fs.existsSync(lab2Path)) {
    console.error(`❌ Lab 2 file not found at: ${lab2Path}`);
    process.exit(1);
  }

  let lab1Data, lab2Data;
  try {
    lab1Data = JSON.parse(fs.readFileSync(lab1Path, 'utf-8'));
  } catch (err) {
    console.error(`❌ Error parsing ${lab1Path}:`, err.message);
    process.exit(1);
  }

  try {
    lab2Data = JSON.parse(fs.readFileSync(lab2Path, 'utf-8'));
  } catch (err) {
    console.error(`❌ Error parsing ${lab2Path}:`, err.message);
    process.exit(1);
  }

  if (!Array.isArray(lab1Data)) {
    console.error(`❌ ${lab1Path} must export an array of questions.`);
    process.exit(1);
  }
  if (!Array.isArray(lab2Data)) {
    console.error(`❌ ${lab2Path} must export an array of questions.`);
    process.exit(1);
  }

  const errors = [];
  const seenIds = new Set();
  const seenQuestions = new Map();

  lab1Data.forEach((q, idx) => validateQuestion(q, idx, 1, seenIds, seenQuestions, errors));
  lab2Data.forEach((q, idx) => validateQuestion(q, idx, 2, seenIds, seenQuestions, errors));

  const totalCount = lab1Data.length + lab2Data.length;
  console.log(`📊 Statistics:`);
  console.log(`   - Lab 1 questions: ${lab1Data.length}`);
  console.log(`   - Lab 2 questions: ${lab2Data.length}`);
  console.log(`   - Total questions: ${totalCount}`);

  // Count by difficulty & type
  const stats = {
    lab1: { easy: 0, medium: 0, hard: 0, single: 0, multi: 0, truefalse: 0 },
    lab2: { easy: 0, medium: 0, hard: 0, single: 0, multi: 0, truefalse: 0 },
  };

  lab1Data.forEach(q => {
    if (stats.lab1[q.difficulty] !== undefined) stats.lab1[q.difficulty]++;
    if (stats.lab1[q.type] !== undefined) stats.lab1[q.type]++;
  });
  lab2Data.forEach(q => {
    if (stats.lab2[q.difficulty] !== undefined) stats.lab2[q.difficulty]++;
    if (stats.lab2[q.type] !== undefined) stats.lab2[q.type]++;
  });

  console.log(`   - Lab 1 breakdown:`, stats.lab1);
  console.log(`   - Lab 2 breakdown:`, stats.lab2);

  const isPartial = process.argv.includes('--partial');

  if (!isPartial) {
    if (lab1Data.length < 250) {
      errors.push(`Lab 1 has ${lab1Data.length} questions; required at least 250.`);
    }
    if (lab2Data.length < 250) {
      errors.push(`Lab 2 has ${lab2Data.length} questions; required at least 250.`);
    }
    if (totalCount < 500) {
      errors.push(`Total questions: ${totalCount}; required at least 500.`);
    }
  } else {
    console.log(`ℹ️ Running in --partial mode: skipping total count >= 500 check.`);
  }

  if (errors.length > 0) {
    console.error(`\n❌ Validation FAILED with ${errors.length} error(s):`);
    errors.slice(0, 30).forEach(e => console.error(`  - ${e}`));
    if (errors.length > 30) {
      console.error(`  ... and ${errors.length - 30} more errors.`);
    }
    process.exit(1);
  }

  console.log('\n✅ Question bank is valid and meets all requirements! (Total >= 500, no duplicates, full explanations)');
}

runValidation();
