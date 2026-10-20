# scripts/generators/generate_questions.py
# -*- coding: utf-8 -*-
"""
Main generator script for Lab 1 and Lab 2 question banks.
Produces:
  - src/data/lab1.json (260 questions, including the teacher's original 10 questions)
  - src/data/lab2.json (260 questions)
Total: 520 questions.
"""

import json
import os
import sys

def build_all_questions():
    print("🚀 Generating question banks for Lab 1 and Lab 2...")
    
    # Import lab generators
    from lab1_builder import generate_lab1_bank
    from lab2_builder import generate_lab2_bank

    lab1_questions = generate_lab1_bank()
    lab2_questions = generate_lab2_bank()

    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/data'))
    os.makedirs(data_dir, exist_ok=True)

    lab1_path = os.path.join(data_dir, 'lab1.json')
    lab2_path = os.path.join(data_dir, 'lab2.json')

    with open(lab1_path, 'w', encoding='utf-8') as f:
        json.dump(lab1_questions, f, ensure_ascii=False, indent=2)
    print(f"✅ Saved {len(lab1_questions)} questions to {lab1_path}")

    with open(lab2_path, 'w', encoding='utf-8') as f:
        json.dump(lab2_questions, f, ensure_ascii=False, indent=2)
    print(f"✅ Saved {len(lab2_questions)} questions to {lab2_path}")

    total = len(lab1_questions) + len(lab2_questions)
    print(f"🎉 Generated {total} questions total (Lab 1: {len(lab1_questions)}, Lab 2: {len(lab2_questions)})")

if __name__ == '__main__':
    build_all_questions()
