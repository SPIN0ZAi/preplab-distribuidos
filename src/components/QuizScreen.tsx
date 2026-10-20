// src/components/QuizScreen.tsx
import React, { useState } from 'react';
import '../styles/screens/quiz-screen.css';
import { Question, QuizSessionState } from '../types/quiz';
import { Timer } from './Timer';
import { GlassSurface } from './GlassSurface';
import { Button } from './primitives/Button';
import { Badge } from './primitives/Badge';
import { ModalSheet } from './primitives/ModalSheet';
import { ArrowLeftIcon, SparklesIcon, CheckIcon } from './primitives/Icons';

interface QuizScreenProps {
  session: QuizSessionState;
  onAnswerChange: (questionId: string, selectedOptionIds: string[]) => void;
  onToggleFlag: (questionId: string) => void;
  onNavigateTo: (index: number) => void;
  onFinishQuiz: () => void;
  onQuitQuiz: () => void;
  onTimerTick: (remainingSeconds: number) => void;
}

export const QuizScreen: React.FC<QuizScreenProps> = ({
  session,
  onAnswerChange,
  onToggleFlag,
  onNavigateTo,
  onFinishQuiz,
  onQuitQuiz,
  onTimerTick,
}) => {
  const [showConfirmModal, setShowConfirmModal] = useState<boolean>(false);
  const [showQuitModal, setShowQuitModal] = useState<boolean>(false);

  const {
    questions,
    currentIndex,
    userAnswers,
    flaggedQuestionIds,
    timeRemainingSeconds,
    initialDurationSeconds,
    timerStartedAtTimestamp,
  } = session;

  const currentQ: Question | undefined = questions[currentIndex];
  if (!currentQ) return null;

  const selectedForCurrent = userAnswers[currentQ.id] || [];
  const isFlagged = flaggedQuestionIds.includes(currentQ.id);

  // Count answered questions
  const answeredCount = Object.keys(userAnswers).filter(
    (id) => (userAnswers[id] || []).length > 0
  ).length;
  const unansweredCount = questions.length - answeredCount;

  // Handle option select
  const handleOptionClick = (optionId: string) => {
    if (currentQ.type === 'single' || currentQ.type === 'truefalse') {
      onAnswerChange(currentQ.id, [optionId]);
    } else if (currentQ.type === 'multi') {
      let updated: string[];
      if (selectedForCurrent.includes(optionId)) {
        updated = selectedForCurrent.filter((id) => id !== optionId);
      } else {
        updated = [...selectedForCurrent, optionId];
      }
      onAnswerChange(currentQ.id, updated);
    }
  };

  const difficultyTone =
    currentQ.difficulty === 'easy'
      ? 'success'
      : currentQ.difficulty === 'medium'
      ? 'warning'
      : 'danger';

  return (
    <div className="quiz-view">
      {/* 1. Chrome Glass Header Bar */}
      <GlassSurface variant="regular" shape="rounded" className="quiz-header-bar">
        <div className="quiz-header-bar__left">
          <Button
            variant="secondary"
            size="sm"
            shape="pill"
            leftIcon={<ArrowLeftIcon size={14} />}
            onClick={() => setShowQuitModal(true)}
            title="Salir y guardar sesión"
          >
            Salir
          </Button>

          <div className="quiz-header-bar__counter">
            Pregunta {currentIndex + 1}
            <span className="quiz-header-bar__counter-total"> / {questions.length}</span>
          </div>
        </div>

        <div className="quiz-header-bar__right">
          <Timer
            initialDurationSeconds={initialDurationSeconds}
            timeRemainingSeconds={timeRemainingSeconds}
            timerStartedAtTimestamp={timerStartedAtTimestamp}
            onTimeExpired={onFinishQuiz}
            onTick={onTimerTick}
          />

          <Button
            variant="primary"
            size="sm"
            shape="pill"
            onClick={() => setShowConfirmModal(true)}
          >
            Finalizar Examen
          </Button>
        </div>
      </GlassSurface>

      {/* 2. Question Navigation Strip */}
      <GlassSurface variant="thin" shape="rounded" className="quiz-nav-strip">
        {questions.map((q, idx) => {
          const isAnswered = (userAnswers[q.id] || []).length > 0;
          const isCurr = idx === currentIndex;
          const isFlg = flaggedQuestionIds.includes(q.id);

          return (
            <button
              key={q.id}
              type="button"
              className={`quiz-nav-pill ${isCurr ? 'quiz-nav-pill--current' : ''} ${
                isAnswered ? 'quiz-nav-pill--answered' : ''
              } ${isFlg ? 'quiz-nav-pill--flagged' : ''}`}
              onClick={() => onNavigateTo(idx)}
              title={`Pregunta ${idx + 1}${isAnswered ? ' (Respondida)' : ''}${
                isFlg ? ' (Marcada)' : ''
              }`}
            >
              {idx + 1}
            </button>
          );
        })}
      </GlassSurface>

      {/* 3. Solid Venus Question Card (Rule 10 - Glass Discipline) */}
      <div className="question-card-venus">
        <div className="question-card__meta-bar">
          <div className="question-card__badges">
            <Badge tone="indigo" size="md">
              {currentQ.lab === 1 ? '🐳 Práctica 1' : '⚡ Práctica 2'}
            </Badge>
            <Badge tone="neutral" size="md">
              {currentQ.topic}
            </Badge>
            <Badge tone={difficultyTone} size="md">
              {currentQ.difficulty === 'easy'
                ? 'Fácil'
                : currentQ.difficulty === 'medium'
                ? 'Intermedio'
                : 'Difícil'}
            </Badge>
            <Badge tone="neutral" size="md">
              {currentQ.type === 'single'
                ? 'Opción única'
                : currentQ.type === 'truefalse'
                ? 'V / F'
                : 'Múltiple'}
            </Badge>
          </div>

          <Button
            variant={isFlagged ? 'primary' : 'secondary'}
            size="sm"
            shape="pill"
            onClick={() => onToggleFlag(currentQ.id)}
            title="Marcar pregunta para revisarla después"
          >
            {isFlagged ? '★ Marcada' : '☆ Marcar'}
          </Button>
        </div>

        <h2 className="question-card__prompt">{currentQ.question}</h2>

        {/* Options List */}
        <div className="options-group" role="group" aria-label="Opciones de respuesta">
          {currentQ.options.map((opt) => {
            const isSelected = selectedForCurrent.includes(opt.id);
            return (
              <div
                key={opt.id}
                className={`option-card ${isSelected ? 'option-card--selected' : ''}`}
                onClick={() => handleOptionClick(opt.id)}
                role={currentQ.type === 'multi' ? 'checkbox' : 'radio'}
                aria-checked={isSelected}
                tabIndex={0}
                onKeyDown={(e) => {
                  if (e.key === ' ' || e.key === 'Enter') {
                    e.preventDefault();
                    handleOptionClick(opt.id);
                  }
                }}
              >
                <div className="option-marker">
                  {currentQ.type === 'multi' && isSelected ? (
                    <CheckIcon size={16} />
                  ) : (
                    opt.id.toUpperCase()
                  )}
                </div>
                <div className="option-label">{opt.text}</div>
              </div>
            );
          })}
        </div>
      </div>

      {/* 4. Bottom Sticky Actions Bar */}
      <GlassSurface variant="regular" shape="rounded" className="quiz-actions-bar">
        <Button
          variant="secondary"
          size="md"
          shape="pill"
          disabled={currentIndex === 0}
          onClick={() => onNavigateTo(currentIndex - 1)}
        >
          ← Anterior
        </Button>

        {currentIndex < questions.length - 1 ? (
          <Button
            variant="primary"
            size="md"
            shape="pill"
            onClick={() => onNavigateTo(currentIndex + 1)}
          >
            Siguiente →
          </Button>
        ) : (
          <Button
            variant="primary"
            size="md"
            shape="pill"
            rightIcon={<SparklesIcon size={16} />}
            onClick={() => setShowConfirmModal(true)}
          >
            Revisar y Entregar Examen
          </Button>
        )}
      </GlassSurface>

      {/* 5. Submission Confirmation Modal */}
      <ModalSheet
        isOpen={showConfirmModal}
        onClose={() => setShowConfirmModal(false)}
        title="¿Deseas entregar el examen?"
        subtitle="Verifica que has completado todas las preguntas antes de cerrar la sesión."
        footer={
          <div style={{ display: 'flex', gap: '12px', justifyContent: 'flex-end', width: '100%' }}>
            <Button
              variant="secondary"
              size="md"
              shape="pill"
              onClick={() => setShowConfirmModal(false)}
            >
              Seguir respondiendo
            </Button>
            <Button
              variant="primary"
              size="md"
              shape="pill"
              onClick={() => {
                setShowConfirmModal(false);
                onFinishQuiz();
              }}
            >
              Confirmar y Entregar
            </Button>
          </div>
        }
      >
        <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '12px' }}>
            <div
              style={{
                backgroundColor: 'var(--venus-bg-canvas)',
                padding: '16px',
                borderRadius: '14px',
                border: '1px solid var(--venus-card-border)',
              }}
            >
              <div style={{ fontSize: '12px', color: 'var(--venus-text-muted)', fontWeight: 600 }}>
                Respondidas
              </div>
              <div
                style={{
                  fontSize: '24px',
                  fontWeight: 800,
                  color: 'var(--venus-accent-emerald)',
                  marginTop: '4px',
                }}
              >
                {answeredCount} / {questions.length}
              </div>
            </div>

            <div
              style={{
                backgroundColor: 'var(--venus-bg-canvas)',
                padding: '16px',
                borderRadius: '14px',
                border: '1px solid var(--venus-card-border)',
              }}
            >
              <div style={{ fontSize: '12px', color: 'var(--venus-text-muted)', fontWeight: 600 }}>
                Sin responder
              </div>
              <div
                style={{
                  fontSize: '24px',
                  fontWeight: 800,
                  color: unansweredCount > 0 ? 'var(--venus-accent-coral)' : 'var(--venus-text-muted)',
                  marginTop: '4px',
                }}
              >
                {unansweredCount}
              </div>
            </div>
          </div>

          {unansweredCount > 0 && (
            <div
              style={{
                padding: '12px 16px',
                backgroundColor: 'rgba(255, 181, 71, 0.12)',
                border: '1px solid rgba(255, 181, 71, 0.25)',
                borderRadius: '12px',
                color: 'var(--venus-accent-amber)',
                fontSize: '13px',
              }}
            >
              ⚠️ Tienes <strong>{unansweredCount}</strong> {unansweredCount === 1 ? 'pregunta' : 'preguntas'} sin responder.
            </div>
          )}
        </div>
      </ModalSheet>

      {/* 6. Quit & Save Modal */}
      <ModalSheet
        isOpen={showQuitModal}
        onClose={() => setShowQuitModal(false)}
        title="Pausar intento de examen"
        subtitle="Tu progreso, respuestas y tiempo restante quedarán guardados en este navegador para que puedas continuar más tarde."
        footer={
          <div style={{ display: 'flex', gap: '12px', justifyContent: 'flex-end', width: '100%' }}>
            <Button
              variant="secondary"
              size="md"
              shape="pill"
              onClick={() => setShowQuitModal(false)}
            >
              Continuar examen
            </Button>
            <Button
              variant="danger"
              size="md"
              shape="pill"
              onClick={() => {
                setShowQuitModal(false);
                onQuitQuiz();
              }}
            >
              Guardar y Salir
            </Button>
          </div>
        }
      >
        <p style={{ fontSize: '14px', color: 'var(--venus-text-muted)', margin: 0, lineHeight: 1.5 }}>
          Puedes reanudar este examen en cualquier momento desde la pantalla principal o desde el menú lateral.
        </p>
      </ModalSheet>
    </div>
  );
};
