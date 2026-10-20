// src/components/ResultsScreen.tsx
import React, { useState } from 'react';
import '../styles/screens/results-screen.css';
import { AttemptResult, Question } from '../types/quiz';
import { CircularGauge } from './charts/CircularGauge';
import { Button } from './primitives/Button';
import { Badge } from './primitives/Badge';
import { SegmentedControl } from './primitives/SegmentedControl';
import { SparklesIcon, FlameIcon } from './primitives/Icons';

interface ResultsScreenProps {
  result: AttemptResult;
  onRetryWrong: (failedQuestions: Question[]) => void;
  onNewQuiz: () => void;
  onHome: () => void;
  onOpenHistory: () => void;
}

export const ResultsScreen: React.FC<ResultsScreenProps> = ({
  result,
  onRetryWrong,
  onNewQuiz,
  onHome,
  onOpenHistory,
}) => {
  const [filter, setFilter] = useState<'all' | 'wrong' | 'correct'>('all');

  const { score, totalQuestions, percentage, timeTakenSeconds, labType, questionResults } = result;
  const isPassed = percentage >= 50;

  const failedResults = questionResults.filter((qr) => !qr.isCorrect);
  const correctResults = questionResults.filter((qr) => qr.isCorrect);

  const displayedResults = questionResults.filter((qr) => {
    if (filter === 'wrong') return !qr.isCorrect;
    if (filter === 'correct') return qr.isCorrect;
    return true;
  });

  const formatTime = (secs: number) => {
    const m = Math.floor(secs / 60);
    const s = secs % 60;
    return `${m}m ${s < 10 ? '0' : ''}${s}s`;
  };

  const getLabLabel = () => {
    if (labType === 'lab1') return 'Práctica 1 (Docker)';
    if (labType === 'lab2') return 'Práctica 2 (gRPC)';
    return 'Examen Mixto (P1 + P2)';
  };

  const handleRetryFailed = () => {
    const wrongQuestions = failedResults.map((qr) => qr.question);
    if (wrongQuestions.length > 0) {
      onRetryWrong(wrongQuestions);
    }
  };

  return (
    <div className="results-dashboard">
      {/* 1. Score Summary Hero Card */}
      <div className={`results-hero-card ${isPassed ? 'celebrate-pass' : ''}`}>
        <CircularGauge percentage={percentage} size={140} tone="dynamic" />

        <div>
          <h2 className="results-hero__title">
            {isPassed ? '¡Prueba Superada!' : 'Prueba No Superada'}
          </h2>
          <p className="results-hero__desc">
            {isPassed
              ? '¡Buen trabajo! Has alcanzado el criterio de aprobado (≥ 50%). Revisa las explicaciones para afianzar cada detalle técnico.'
              : 'Has obtenido menos del 50%. Te recomendamos revisar las justificaciones detalladas y reintentar las preguntas falladas.'}
          </p>
        </div>

        {/* Quick Stats Grid */}
        <div className="results-stats-deck">
          <div className="results-stat-box">
            <span className="results-stat-box__label">Modo</span>
            <span className="results-stat-box__value" style={{ fontSize: '15px' }}>
              {getLabLabel()}
            </span>
          </div>

          <div className="results-stat-box">
            <span className="results-stat-box__label">Tiempo</span>
            <span className="results-stat-box__value">
              {formatTime(timeTakenSeconds)}
            </span>
          </div>

          <div className="results-stat-box">
            <span className="results-stat-box__label">Aciertos</span>
            <span className="results-stat-box__value" style={{ color: 'var(--venus-accent-emerald)' }}>
              {score} / {totalQuestions}
            </span>
          </div>

          <div className="results-stat-box">
            <span className="results-stat-box__label">Fallos</span>
            <span
              className="results-stat-box__value"
              style={{ color: failedResults.length > 0 ? 'var(--venus-accent-coral)' : 'var(--venus-text-muted)' }}
            >
              {failedResults.length}
            </span>
          </div>
        </div>

        {/* Action Buttons */}
        <div className="results-actions-deck">
          {failedResults.length > 0 && (
            <Button
              variant="primary"
              size="md"
              shape="pill"
              onClick={handleRetryFailed}
              style={{ backgroundColor: 'var(--venus-accent-amber)' }}
            >
              Reintentar {failedResults.length} falladas
            </Button>
          )}

          <Button
            variant="primary"
            size="md"
            shape="pill"
            rightIcon={<SparklesIcon size={16} />}
            onClick={onNewQuiz}
          >
            Nuevo intento aleatorio
          </Button>

          <Button
            variant="secondary"
            size="md"
            shape="pill"
            rightIcon={<FlameIcon size={16} />}
            onClick={onOpenHistory}
          >
            Historial y Debilidades
          </Button>

          <Button
            variant="secondary"
            size="md"
            shape="pill"
            onClick={onHome}
          >
            Inicio
          </Button>
        </div>
      </div>

      {/* 2. Detailed Review Section */}
      <div className="review-deck">
        <div className="review-header-bar">
          <div>
            <h3 className="review-header__title">Revisión detallada de preguntas</h3>
            <span style={{ fontSize: '13px', color: 'var(--venus-text-muted)' }}>
              Comprueba tus respuestas y lee la justificación de cada distractor
            </span>
          </div>

          <SegmentedControl<'all' | 'wrong' | 'correct'>
            value={filter}
            onChange={setFilter}
            size="sm"
            options={[
              { id: 'all', label: 'Todas', badge: totalQuestions },
              { id: 'wrong', label: 'Falladas', badge: failedResults.length },
              { id: 'correct', label: 'Acertadas', badge: correctResults.length },
            ]}
          />
        </div>

        {displayedResults.length === 0 ? (
          <div
            style={{
              backgroundColor: 'var(--venus-card-bg)',
              border: '1px solid var(--venus-card-border)',
              borderRadius: '16px',
              padding: '40px',
              textAlign: 'center',
              color: 'var(--venus-text-muted)',
            }}
          >
            No hay preguntas en esta categoría.
          </div>
        ) : (
          displayedResults.map((qr) => {
            const { question: q, selectedAnswers, isCorrect } = qr;
            const originalIndex =
              questionResults.findIndex((item) => item.question.id === q.id) + 1;

            return (
              <div
                key={q.id}
                className={`review-item-card ${
                  isCorrect ? 'review-item-card--correct' : 'review-item-card--incorrect'
                }`}
              >
                {/* Item Header */}
                <div className="review-item__meta">
                  <div className="review-item__tags">
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
                <h4 className="review-item__prompt">{q.question}</h4>

                {/* Options List */}
                <div className="review-options-group">
                  {q.options.map((opt) => {
                    const isTarget = q.correct.includes(opt.id);
                    const isUserChoice = selectedAnswers.includes(opt.id);

                    let rowClass = 'review-option-row';
                    if (isTarget) rowClass += ' review-option-row--correct';
                    else if (isUserChoice) rowClass += ' review-option-row--wrong-user';

                    return (
                      <div key={opt.id} className={rowClass}>
                        <span className="review-option__marker">{opt.id.toUpperCase()}.</span>
                        <span style={{ flex: 1 }}>{opt.text}</span>
                        {isTarget && (
                          <Badge tone="success" size="sm">
                            {isUserChoice ? '✓ Tu respuesta correcta' : '✓ Correcta'}
                          </Badge>
                        )}
                        {!isTarget && isUserChoice && (
                          <Badge tone="danger" size="sm">
                            ✗ Tu elección
                          </Badge>
                        )}
                      </div>
                    );
                  })}
                </div>

                {/* Explanation Callout */}
                <div className="explanation-callout">
                  <div className="explanation-callout__header">
                    <span>💡</span>
                    <span>Justificación y Análisis de Opciones</span>
                  </div>

                  <div className="explanation-callout__correct">
                    <strong style={{ color: 'var(--venus-accent-emerald)' }}>Por qué es correcta: </strong>
                    {q.explanation.correct}
                  </div>

                  {q.explanation.wrong && Object.keys(q.explanation.wrong).length > 0 && (
                    <div className="explanation-callout__distractors">
                      <div style={{ fontWeight: 700, color: 'var(--venus-text-muted)', fontSize: '11px', textTransform: 'uppercase' }}>
                        Por qué son incorrectas las demás opciones:
                      </div>
                      {Object.entries(q.explanation.wrong).map(([optId, reason]) => (
                        <div key={optId} className="explanation-callout__distractor-item">
                          <strong>Opción {optId.toUpperCase()}:</strong> {reason}
                        </div>
                      ))}
                    </div>
                  )}

                  <div className="explanation-callout__source">
                    Referencia oficial: {q.source}
                  </div>
                </div>
              </div>
            );
          })
        )}
      </div>
    </div>
  );
};
