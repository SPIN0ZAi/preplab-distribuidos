// src/components/HistoryModal.tsx
import React, { useState } from 'react';
import '../styles/components/history-modal.css';
import { storage } from '../services/storage';
import { AttemptResult, Question } from '../types/quiz';
import { ModalSheet } from './primitives/ModalSheet';
import { SegmentedControl } from './primitives/SegmentedControl';
import { Badge } from './primitives/Badge';
import { Button } from './primitives/Button';
import { ArrowLeftIcon } from './primitives/Icons';

interface HistoryModalProps {
  isOpen: boolean;
  onClose: () => void;
  onRetryAttemptFailed?: (questions: Question[], labType: 'lab1' | 'lab2' | 'mixed') => void;
  onViewInResultsScreen?: (attempt: AttemptResult) => void;
}

export const HistoryModal: React.FC<HistoryModalProps> = ({
  isOpen,
  onClose,
  onRetryAttemptFailed,
  onViewInResultsScreen,
}) => {
  const [activeTab, setActiveTab] = useState<'history' | 'weaknesses'>('history');
  const [showClearConfirm, setShowClearConfirm] = useState<boolean>(false);
  const [selectedAttempt, setSelectedAttempt] = useState<AttemptResult | null>(null);
  const [reviewFilter, setReviewFilter] = useState<'all' | 'wrong' | 'correct'>('all');

  if (!isOpen) return null;

  const attempts: AttemptResult[] = storage.getAttempts();
  const weaknesses = storage.getTopicWeaknesses();

  // Sort weaknesses by lowest percentage first to highlight areas needing study
  const sortedWeaknessList = Object.entries(weaknesses)
    .map(([topic, data]) => ({ topic, ...data }))
    .sort((a, b) => a.percentage - b.percentage);

  const handleClearHistory = () => {
    storage.clearHistory();
    setShowClearConfirm(false);
    setSelectedAttempt(null);
    onClose();
  };

  const formatDuration = (secs: number) => {
    const m = Math.floor(secs / 60);
    const s = secs % 60;
    return `${m}m ${s < 10 ? '0' : ''}${s}s`;
  };

  const formatDate = (isoString: string) => {
    try {
      const d = new Date(isoString);
      return d.toLocaleDateString('es-ES', {
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
      });
    } catch {
      return isoString;
    }
  };

  const getLabLabel = (type: 'lab1' | 'lab2' | 'mixed') => {
    if (type === 'lab1') return 'Práctica 1 (Docker)';
    if (type === 'lab2') return 'Práctica 2 (gRPC)';
    return 'Simulacro Mixto (P1 + P2)';
  };

  // If viewing an attempt detail
  if (selectedAttempt) {
    const isPassed = selectedAttempt.percentage >= 50;
    const failedResults = selectedAttempt.questionResults.filter((qr) => !qr.isCorrect);
    const correctResults = selectedAttempt.questionResults.filter((qr) => qr.isCorrect);
    const failedQuestions = failedResults.map((qr) => qr.question);

    const displayedResults = selectedAttempt.questionResults.filter((qr) => {
      if (reviewFilter === 'wrong') return !qr.isCorrect;
      if (reviewFilter === 'correct') return qr.isCorrect;
      return true;
    });

    return (
      <ModalSheet
        isOpen={isOpen}
        onClose={onClose}
        title={
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
            <Button
              variant="secondary"
              size="sm"
              shape="pill"
              leftIcon={<ArrowLeftIcon size={16} />}
              onClick={() => setSelectedAttempt(null)}
            >
              Volver a Intentos
            </Button>
            <span>Revisión de Intento</span>
          </div>
        }
        subtitle={`${getLabLabel(selectedAttempt.labType)} • Realizado el ${formatDate(selectedAttempt.date)}`}
        maxWidth={860}
        footer={
          <div style={{ display: 'flex', width: '100%', justifyContent: 'space-between', alignItems: 'center' }}>
            <Button
              variant="ghost"
              size="sm"
              leftIcon={<ArrowLeftIcon size={16} />}
              onClick={() => setSelectedAttempt(null)}
            >
              Volver al Listado
            </Button>

            <div style={{ display: 'flex', gap: '8px' }}>
              {failedQuestions.length > 0 && onRetryAttemptFailed && (
                <Button
                  variant="primary"
                  size="md"
                  shape="pill"
                  style={{ backgroundColor: 'var(--venus-accent-amber)' }}
                  onClick={() => {
                    onRetryAttemptFailed(failedQuestions, selectedAttempt.labType);
                    onClose();
                  }}
                >
                  Reintentar {failedQuestions.length} falladas
                </Button>
              )}
              <Button variant="secondary" size="md" shape="pill" onClick={onClose}>
                Cerrar
              </Button>
            </div>
          </div>
        }
      >
        {/* Score Hero Summary */}
        <div className="attempt-review-hero">
          <div className="attempt-review-hero__left">
            <div
              className={`attempt-review-hero__score ${
                isPassed ? 'attempt-review-hero__score--passed' : 'attempt-review-hero__score--failed'
              }`}
            >
              {selectedAttempt.score}/{selectedAttempt.totalQuestions} ({selectedAttempt.percentage}%)
            </div>
            <div className="attempt-review-hero__meta">
              <span className="attempt-review-hero__title">
                {isPassed ? '¡Intento Aprobado!' : 'Intento No Superado'}
              </span>
              <span className="attempt-review-hero__desc">
                Duración: {formatDuration(selectedAttempt.timeTakenSeconds)} • {failedResults.length} falladas • {correctResults.length} acertadas
              </span>
            </div>
          </div>

          <div className="attempt-review-hero__actions">
            <Badge tone={isPassed ? 'success' : 'danger'} size="md">
              {isPassed ? '✓ Aprobado (≥ 50%)' : '✗ Suspenso (< 50%)'}
            </Badge>
            {failedQuestions.length > 0 && onRetryAttemptFailed && (
              <Button
                variant="primary"
                size="sm"
                shape="pill"
                style={{ backgroundColor: 'var(--venus-accent-amber)' }}
                onClick={() => {
                  onRetryAttemptFailed(failedQuestions, selectedAttempt.labType);
                  onClose();
                }}
              >
                Reintentar {failedQuestions.length} falladas
              </Button>
            )}
            {onViewInResultsScreen && (
              <Button
                variant="secondary"
                size="sm"
                shape="pill"
                onClick={() => {
                  onViewInResultsScreen(selectedAttempt);
                  onClose();
                }}
              >
                Ver en pantalla completa
              </Button>
            )}
          </div>
        </div>

        {/* Filter Segmented Control */}
        <div className="attempt-review-filters">
          <SegmentedControl<'all' | 'wrong' | 'correct'>
            value={reviewFilter}
            onChange={setReviewFilter}
            size="sm"
            options={[
              { id: 'all', label: 'Todas las preguntas', badge: selectedAttempt.questionResults.length },
              { id: 'wrong', label: 'Solo Falladas', badge: failedResults.length },
              { id: 'correct', label: 'Acertadas', badge: correctResults.length },
            ]}
          />
        </div>

        {/* Questions Review Deck */}
        <div className="attempt-questions-list">
          {displayedResults.map((qr) => {
            const { question: q, selectedAnswers, isCorrect } = qr;
            const originalIndex =
              selectedAttempt.questionResults.findIndex((item) => item.question.id === q.id) + 1;

            return (
              <div
                key={q.id}
                className={`attempt-qcard ${
                  isCorrect ? 'attempt-qcard--correct' : 'attempt-qcard--incorrect'
                }`}
              >
                {/* Card Header */}
                <div className="attempt-qcard__header">
                  <div className="attempt-qcard__tags">
                    <span style={{ fontWeight: 800, color: 'var(--venus-text-headline)', fontSize: '14px' }}>
                      Pregunta {originalIndex}
                    </span>
                    <Badge tone="indigo" size="sm">{q.topic}</Badge>
                    <Badge tone="neutral" size="sm">{q.difficulty}</Badge>
                    <span style={{ fontSize: '11px', color: 'var(--venus-text-disabled)' }}>
                      ID: {q.id}
                    </span>
                  </div>

                  <Badge tone={isCorrect ? 'success' : 'danger'} size="sm">
                    {isCorrect ? '✓ Acertada' : `✗ Fallada ${selectedAnswers.length === 0 ? '(Sin responder)' : ''}`}
                  </Badge>
                </div>

                {/* Prompt */}
                <h4 className="attempt-qcard__prompt">{q.question}</h4>

                {/* Options List */}
                <div className="attempt-options-deck">
                  {q.options.map((opt) => {
                    const isTarget = q.correct.includes(opt.id);
                    const isUserChoice = selectedAnswers.includes(opt.id);

                    let rowClass = 'attempt-opt-row';
                    if (isTarget) rowClass += ' attempt-opt-row--correct';
                    else if (isUserChoice) rowClass += ' attempt-opt-row--wrong-user';

                    return (
                      <div key={opt.id} className={rowClass}>
                        <span className="attempt-opt-marker">{opt.id.toUpperCase()}.</span>
                        <span style={{ flex: 1 }}>{opt.text}</span>
                        {isTarget && (
                          <Badge tone="success" size="sm">
                            {isUserChoice ? '✓ Tu respuesta correcta' : '✓ Respuesta Correcta'}
                          </Badge>
                        )}
                        {!isTarget && isUserChoice && (
                          <Badge tone="danger" size="sm">
                            ✗ Tu respuesta elegida
                          </Badge>
                        )}
                      </div>
                    );
                  })}
                </div>

                {/* Explanations Pane */}
                <div className="attempt-explanation-pane">
                  <div className="attempt-explanation-title">
                    💡 Justificación de la Opción Correcta:
                  </div>
                  <div className="attempt-explanation-text">
                    {q.explanation.correct}
                  </div>

                  {/* Why distractors are wrong */}
                  {q.explanation.wrong && Object.keys(q.explanation.wrong).length > 0 && (
                    <div style={{ marginTop: '6px' }}>
                      <div className="attempt-explanation-title" style={{ color: 'var(--venus-accent-coral)' }}>
                        ⚠️ Por qué los otros distractores son erróneos:
                      </div>
                      {Object.entries(q.explanation.wrong).map(([optId, reason]) => {
                        const wasChosenByUser = selectedAnswers.includes(optId);
                        return (
                          <div
                            key={optId}
                            className="attempt-explanation-wrong-item"
                            style={
                              wasChosenByUser
                                ? { fontWeight: 600, color: 'var(--venus-text-headline)' }
                                : undefined
                            }
                          >
                            <strong>Opción {optId.toUpperCase()}:</strong> {reason}
                            {wasChosenByUser && ' (⚠️ Esta fue tu opción errónea)'}
                          </div>
                        );
                      })}
                    </div>
                  )}
                </div>
              </div>
            );
          })}
        </div>
      </ModalSheet>
    );
  }

  // Normal List View (Tab 1: History List, Tab 2: Weaknesses)
  return (
    <ModalSheet
      isOpen={isOpen}
      onClose={onClose}
      title="Progreso y Analítica"
      subtitle="Resultados de simulacros anteriores y debilidades temáticas"
      maxWidth={800}
      footer={
        <div style={{ display: 'flex', width: '100%', justifyContent: 'space-between', alignItems: 'center' }}>
          <div>
            {attempts.length > 0 && !showClearConfirm && (
              <Button
                variant="ghost"
                size="sm"
                onClick={() => setShowClearConfirm(true)}
                style={{ color: 'var(--venus-accent-coral)' }}
              >
                Borrar historial
              </Button>
            )}

            {showClearConfirm && (
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <span style={{ fontSize: '13px', color: 'var(--venus-accent-coral)', fontWeight: 600 }}>
                  ¿Seguro?
                </span>
                <Button
                  variant="danger"
                  size="sm"
                  shape="pill"
                  onClick={handleClearHistory}
                >
                  Sí, borrar todo
                </Button>
                <Button
                  variant="secondary"
                  size="sm"
                  shape="pill"
                  onClick={() => setShowClearConfirm(false)}
                >
                  Cancelar
                </Button>
              </div>
            )}
          </div>

          <Button
            variant="primary"
            size="md"
            shape="pill"
            onClick={onClose}
          >
            Cerrar
          </Button>
        </div>
      }
    >
      {/* Tab Switcher using SegmentedControl */}
      <div className="history-modal__tabs">
        <SegmentedControl<'history' | 'weaknesses'>
          value={activeTab}
          onChange={setActiveTab}
          size="md"
          options={[
            { id: 'history', label: 'Historial de Intentos', badge: attempts.length },
            { id: 'weaknesses', label: 'Debilidades por Tema', badge: sortedWeaknessList.length },
          ]}
        />
      </div>

      {/* Tab 1: Attempt History */}
      {activeTab === 'history' && (
        <div>
          {attempts.length === 0 ? (
            <div className="history-modal__empty">
              <div className="history-modal__empty-icon">📝</div>
              <div className="history-modal__empty-title">Todavía no has completado ningún intento.</div>
              <div className="history-modal__empty-desc">
                Inicia un simulacro para registrar tu progreso y ver estadísticas detalladas.
              </div>
            </div>
          ) : (
            <div className="history-modal__list">
              {attempts.map((att) => {
                const isPassed = att.percentage >= 50;
                const failedCount = att.questionResults.filter((qr) => !qr.isCorrect).length;

                return (
                  <div
                    key={att.id}
                    className={`history-card history-card--clickable hover-lift ${
                      isPassed ? 'history-card--passed' : 'history-card--failed'
                    }`}
                    onClick={() => {
                      setSelectedAttempt(att);
                      setReviewFilter('all');
                    }}
                    role="button"
                    tabIndex={0}
                    onKeyDown={(e) => {
                      if (e.key === 'Enter' || e.key === ' ') {
                        setSelectedAttempt(att);
                        setReviewFilter('all');
                      }
                    }}
                    title="Haz clic para revisar las preguntas y explicaciones de este intento"
                  >
                    <div className="history-card__meta">
                      <div className="history-card__title-row">
                        <span className="history-card__lab-title">{getLabLabel(att.labType)}</span>
                        <span className="history-card__date">{formatDate(att.date)}</span>
                      </div>
                      <div className="history-card__details">
                        Duración: {formatDuration(att.timeTakenSeconds)} • Usuario: {att.username}
                      </div>
                      <span className="history-card__action-hint">
                        🔍 Ver {att.totalQuestions} preguntas ({failedCount} fallos) →
                      </span>
                    </div>

                    <div className="history-card__score-block">
                      <div
                        className={`history-card__score-value ${
                          isPassed ? 'history-card__score-value--passed' : 'history-card__score-value--failed'
                        }`}
                      >
                        {att.score}/{att.totalQuestions} ({att.percentage}%)
                      </div>
                      <Badge tone={isPassed ? 'success' : 'danger'} size="sm">
                        {isPassed ? 'Aprobado' : 'Suspenso'}
                      </Badge>
                    </div>
                  </div>
                );
              })}
            </div>
          )}
        </div>
      )}

      {/* Tab 2: Topic Weaknesses */}
      {activeTab === 'weaknesses' && (
        <div>
          {sortedWeaknessList.length === 0 ? (
            <div className="history-modal__empty">
              <div className="history-modal__empty-icon">🎯</div>
              <div className="history-modal__empty-title">No hay suficientes datos de temas todavía.</div>
              <div className="history-modal__empty-desc">
                Completa simulacros para que el motor identifique en qué temas fallas más.
              </div>
            </div>
          ) : (
            <div className="weakness-table-container">
              <p className="weakness-intro">
                Ordenado de menor a mayor porcentaje de acierto. Los temas en rojo o amarillo son tus áreas de máxima prioridad de estudio:
              </p>
              <table className="venus-table">
                <thead>
                  <tr>
                    <th>Tema</th>
                    <th style={{ width: '45%' }}>Rendimiento</th>
                    <th style={{ textAlign: 'right' }}>Estado</th>
                  </tr>
                </thead>
                <tbody>
                  {sortedWeaknessList.map(({ topic, total, correct, percentage }) => {
                    let fillClass = 'venus-progress__bar-fill--high';
                    let badgeTone: 'success' | 'warning' | 'danger' = 'success';
                    let label = 'Dominado';

                    if (percentage < 60) {
                      fillClass = 'venus-progress__bar-fill--low';
                      badgeTone = 'danger';
                      label = 'Reforzar';
                    } else if (percentage < 80) {
                      fillClass = 'venus-progress__bar-fill--medium';
                      badgeTone = 'warning';
                      label = 'Repasar';
                    }

                    return (
                      <tr key={topic}>
                        <td>
                          <div className="venus-table__topic-title">{topic}</div>
                          <div className="venus-table__topic-stat">
                            {correct} de {total} correctas
                          </div>
                        </td>
                        <td>
                          <div className="venus-progress">
                            <div className="venus-progress__bar-bg">
                              <div
                                className={`venus-progress__bar-fill ${fillClass}`}
                                style={{ width: `${percentage}%` }}
                              />
                            </div>
                            <span className="venus-progress__percentage">{percentage}%</span>
                          </div>
                        </td>
                        <td style={{ textAlign: 'right' }}>
                          <Badge tone={badgeTone} size="sm">
                            {label}
                          </Badge>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          )}
        </div>
      )}
    </ModalSheet>
  );
};
