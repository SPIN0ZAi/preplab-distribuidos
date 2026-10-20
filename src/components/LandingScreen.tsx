// src/components/LandingScreen.tsx
import React, { useState } from 'react';
import '../styles/screens/landing-screen.css';
import { TimerPreset } from '../types/quiz';
import { LandingScreenProps } from '../types/screens';
import { storage } from '../services/storage';
import { Button } from './primitives/Button';
import { Badge } from './primitives/Badge';
import { TextInput } from './primitives/TextInput';
import { RoundedBarChart } from './charts/RoundedBarChart';
import { AreaSparkline } from './charts/AreaSparkline';
import {
  SparklesIcon,
  BookOpenIcon,
  FlameIcon,
} from './primitives/Icons';

export const LandingScreen: React.FC<LandingScreenProps> = ({
  onStartQuiz,
  onResumeQuiz,
  hasActiveSession = false,
  onOpenHistory,
  selectedLab: propSelectedLab,
  onSelectLab: propOnSelectLab,
}) => {
  const [username, setUsername] = useState<string>(() => storage.getUsername() || '');
  const [internalSelectedLab, setInternalSelectedLab] = useState<'lab1' | 'lab2' | 'mixed'>('lab1');

  const selectedLab = propSelectedLab !== undefined ? propSelectedLab : internalSelectedLab;
  const setSelectedLab = (lab: 'lab1' | 'lab2' | 'mixed') => {
    if (propOnSelectLab) {
      propOnSelectLab(lab);
    } else {
      setInternalSelectedLab(lab);
    }
  };
  const [timerPreset, setTimerPresetState] = useState<TimerPreset>(() => storage.getTimerPreset());
  const [isCustomTimer, setIsCustomTimer] = useState<boolean>(false);
  const [customMinutes, setCustomMinutes] = useState<number>(() => storage.getCustomTimerMinutes());

  const attempts = storage.getAttempts();
  const totalAttempts = attempts.length;
  const avgScore = totalAttempts > 0
    ? Math.round(attempts.reduce((acc, att) => acc + att.percentage, 0) / totalAttempts)
    : 0;

  const handleUsernameChange = (val: string) => {
    setUsername(val);
    storage.setUsername(val);
  };

  const handleSelectPreset = (preset: TimerPreset) => {
    setIsCustomTimer(false);
    setTimerPresetState(preset);
    storage.setTimerPreset(preset);
  };

  const handleCustomMinutesChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const val = parseInt(e.target.value, 10);
    const valid = isNaN(val) || val <= 0 ? 1 : Math.min(180, val);
    setCustomMinutes(valid);
    storage.setCustomTimerMinutes(valid);
  };

  const handleStart = () => {
    let duration: number | null = null;
    if (isCustomTimer) {
      duration = customMinutes * 60;
    } else if (timerPreset > 0) {
      duration = timerPreset;
    }
    onStartQuiz(selectedLab, duration);
  };

  return (
    <div className="landing-dashboard">
      {/* 1. Resume Active Session Banner */}
      {hasActiveSession && onResumeQuiz && (
        <div className="resume-banner">
          <div>
            <div className="resume-banner__title">
              ⚡ Tienes una sesión de examen en curso sin finalizar
            </div>
            <div className="resume-banner__desc">
              Tus respuestas y tiempo restante han sido guardados automáticamente.
            </div>
          </div>
          <Button variant="primary" size="md" shape="pill" onClick={onResumeQuiz}>
            Reanudar Intento
          </Button>
        </div>
      )}

      {/* 2. Venus Stat Metrics Grid */}
      <div className="metrics-grid">
        <div className="metric-card">
          <div className="metric-card__icon-wrap metric-card__icon-wrap--indigo">
            <SparklesIcon size={24} />
          </div>
          <div className="metric-card__info">
            <span className="metric-card__label">Banco Oficial</span>
            <span className="metric-card__value">520 Qs</span>
          </div>
        </div>

        <div className="metric-card">
          <div className="metric-card__icon-wrap metric-card__icon-wrap--emerald">
            <BookOpenIcon size={24} />
          </div>
          <div className="metric-card__info">
            <span className="metric-card__label">Lab 1: Docker</span>
            <span className="metric-card__value">260 Qs</span>
          </div>
        </div>

        <div className="metric-card">
          <div className="metric-card__icon-wrap metric-card__icon-wrap--amber">
            <BookOpenIcon size={24} />
          </div>
          <div className="metric-card__info">
            <span className="metric-card__label">Lab 2: gRPC</span>
            <span className="metric-card__value">260 Qs</span>
          </div>
        </div>

        <div className="metric-card">
          <div className="metric-card__icon-wrap metric-card__icon-wrap--purple">
            <FlameIcon size={24} />
          </div>
          <div className="metric-card__info">
            <span className="metric-card__label">Media de Acierto</span>
            <span className="metric-card__value">{totalAttempts > 0 ? `${avgScore}%` : 'N/A'}</span>
          </div>
        </div>
      </div>

      {/* 3. Analytics Charts Deck (Venus Rounded Bars + Area Spline) */}
      <div className="analytics-deck">
        <div className="analytics-card">
          <div className="analytics-card__header">
            <h3 className="analytics-card__title">Distribución Semanal de Actividad</h3>
            <Badge tone="indigo" size="sm">Venus Metrics</Badge>
          </div>
          <RoundedBarChart
            data={[
              { label: 'Lun', value: 45 },
              { label: 'Mar', value: 65 },
              { label: 'Mié', value: 90, highlighted: true },
              { label: 'Jue', value: 50 },
              { label: 'Vie', value: 75 },
              { label: 'Sáb', value: 85 },
              { label: 'Dom', value: 60 },
            ]}
            height={160}
          />
        </div>

        <div className="analytics-card">
          <div className="analytics-card__header">
            <h3 className="analytics-card__title">Evolución de Rendimiento</h3>
            <Badge tone="success" size="sm">Tendencia</Badge>
          </div>
          <AreaSparkline
            data={
              attempts.length >= 3
                ? attempts.slice(-6).map((a, i) => ({ label: `T${i + 1}`, value: a.percentage }))
                : [
                    { label: 'P1', value: 55 },
                    { label: 'P2', value: 68 },
                    { label: 'P3', value: 62 },
                    { label: 'P4', value: 84 },
                    { label: 'P5', value: 90 },
                  ]
            }
            height={160}
          />
        </div>
      </div>

      {/* 4. Lab Mode Selector Cards */}
      <div className="launch-grid">
        {/* Lab 1 */}
        <div
          className={`launch-card ${selectedLab === 'lab1' ? 'launch-card--selected' : ''}`}
          onClick={() => setSelectedLab('lab1')}
        >
          <div>
            <div className="launch-card__top">
              <Badge tone="indigo" size="md">Práctica 1</Badge>
              <span style={{ fontSize: '1.6rem' }}>🐳</span>
            </div>
            <h4 className="launch-card__title">Dockerización de Aplicaciones</h4>
            <p className="launch-card__desc">
              Contenedores vs VMs, Dockerfile, multi-stage builds, redes bridge, volúmenes, Compose y CORS.
            </p>
            <ul className="launch-card__topics">
              <li className="launch-card__topic-item">
                <span className="launch-card__topic-bullet" />
                <span>Dockerización de TodoApi (.NET 10)</span>
              </li>
              <li className="launch-card__topic-item">
                <span className="launch-card__topic-bullet" />
                <span>Frontend TodoApp con Blazor y Nginx</span>
              </li>
              <li className="launch-card__topic-item">
                <span className="launch-card__topic-bullet" />
                <span>Políticas CORS en ASP.NET Core</span>
              </li>
            </ul>
          </div>
          <div className="launch-card__footer">
            <span>260 preguntas</span>
            <Badge tone={selectedLab === 'lab1' ? 'indigo' : 'neutral'} size="sm">
              {selectedLab === 'lab1' ? '✓ Seleccionado' : 'Elegir'}
            </Badge>
          </div>
        </div>

        {/* Lab 2 */}
        <div
          className={`launch-card ${selectedLab === 'lab2' ? 'launch-card--selected' : ''}`}
          onClick={() => setSelectedLab('lab2')}
        >
          <div>
            <div className="launch-card__top">
              <Badge tone="warning" size="md">Práctica 2</Badge>
              <span style={{ fontSize: '1.6rem' }}>⚡</span>
            </div>
            <h4 className="launch-card__title">gRPC y Concurrencia en .NET</h4>
            <p className="launch-card__desc">
              Llamadas RPC, Protocol Buffers, HTTP/2 sin TLS, sincronización con lock, semáforos y colas.
            </p>
            <ul className="launch-card__topics">
              <li className="launch-card__topic-item">
                <span className="launch-card__topic-bullet" />
                <span>Stubs y Skeletons en C#</span>
              </li>
              <li className="launch-card__topic-item">
                <span className="launch-card__topic-bullet" />
                <span>Sistema distribuido del Restaurante</span>
              </li>
              <li className="launch-card__topic-item">
                <span className="launch-card__topic-bullet" />
                <span>SemaphoreSlim y ConcurrentQueue</span>
              </li>
            </ul>
          </div>
          <div className="launch-card__footer">
            <span>260 preguntas</span>
            <Badge tone={selectedLab === 'lab2' ? 'warning' : 'neutral'} size="sm">
              {selectedLab === 'lab2' ? '✓ Seleccionado' : 'Elegir'}
            </Badge>
          </div>
        </div>

        {/* Mixed */}
        <div
          className={`launch-card ${selectedLab === 'mixed' ? 'launch-card--selected' : ''}`}
          onClick={() => setSelectedLab('mixed')}
        >
          <div>
            <div className="launch-card__top">
              <Badge tone="success" size="md">Simulacro Global</Badge>
              <span style={{ fontSize: '1.6rem' }}>🎓</span>
            </div>
            <h4 className="launch-card__title">Examen Mixto (P1 + P2)</h4>
            <p className="launch-card__desc">
              Simula el examen final combinando 10 preguntas de Docker y 10 preguntas de gRPC y Concurrencia.
            </p>
            <ul className="launch-card__topics">
              <li className="launch-card__topic-item">
                <span className="launch-card__topic-bullet" />
                <span>10 preguntas aleatorias de Lab 1</span>
              </li>
              <li className="launch-card__topic-item">
                <span className="launch-card__topic-bullet" />
                <span>10 preguntas aleatorias de Lab 2</span>
              </li>
              <li className="launch-card__topic-item">
                <span className="launch-card__topic-bullet" />
                <span>Desglose de debilidad al finalizar</span>
              </li>
            </ul>
          </div>
          <div className="launch-card__footer">
            <span>520 preguntas totales</span>
            <Badge tone={selectedLab === 'mixed' ? 'success' : 'neutral'} size="sm">
              {selectedLab === 'mixed' ? '✓ Seleccionado' : 'Elegir'}
            </Badge>
          </div>
        </div>
      </div>

      {/* 5. Configuration Section */}
      <div className="config-card">
        <div className="config-card__row">
          <div className="config-card__field">
            <label className="config-card__label" htmlFor="student-name-input">
              Nombre o alias del estudiante
            </label>
            <TextInput
              id="student-name-input"
              value={username}
              onChange={handleUsernameChange}
              placeholder="Introduce tu nombre o apodo..."
              maxLength={40}
            />
          </div>

          <div className="config-card__field" style={{ flex: 2 }}>
            <span className="config-card__label">Temporizador de Examen</span>
            <div className="timer-pill-group">
              <Button
                variant={!isCustomTimer && timerPreset === 0 ? 'primary' : 'secondary'}
                size="sm"
                shape="pill"
                onClick={() => handleSelectPreset(0)}
              >
                Sin tiempo
              </Button>
              <Button
                variant={!isCustomTimer && timerPreset === 600 ? 'primary' : 'secondary'}
                size="sm"
                shape="pill"
                onClick={() => handleSelectPreset(600)}
              >
                10 min
              </Button>
              <Button
                variant={!isCustomTimer && timerPreset === 1200 ? 'primary' : 'secondary'}
                size="sm"
                shape="pill"
                onClick={() => handleSelectPreset(1200)}
              >
                20 min (Recomendado)
              </Button>
              <Button
                variant={!isCustomTimer && timerPreset === 1800 ? 'primary' : 'secondary'}
                size="sm"
                shape="pill"
                onClick={() => handleSelectPreset(1800)}
              >
                30 min
              </Button>
              <Button
                variant={!isCustomTimer && timerPreset === 2700 ? 'primary' : 'secondary'}
                size="sm"
                shape="pill"
                onClick={() => handleSelectPreset(2700)}
              >
                45 min
              </Button>
              <Button
                variant={isCustomTimer ? 'primary' : 'secondary'}
                size="sm"
                shape="pill"
                onClick={() => setIsCustomTimer(true)}
              >
                Personalizado...
              </Button>
            </div>

            {isCustomTimer && (
              <div style={{ marginTop: '10px', display: 'flex', alignItems: 'center', gap: '8px' }}>
                <span style={{ fontSize: '13px', color: 'var(--venus-text-muted)' }}>Minutos:</span>
                <input
                  type="number"
                  min={1}
                  max={180}
                  className="input-text"
                  style={{
                    width: '100px',
                    padding: '8px 12px',
                    borderRadius: '10px',
                    border: '1px solid var(--venus-card-border)',
                    backgroundColor: 'var(--venus-bg-canvas)',
                    color: 'var(--venus-text-headline)',
                  }}
                  value={customMinutes}
                  onChange={handleCustomMinutesChange}
                />
              </div>
            )}
          </div>
        </div>
      </div>

      {/* 6. Primary Action Buttons */}
      <div style={{ display: 'flex', justifyContent: 'center', gap: '16px', flexWrap: 'wrap', paddingBottom: '20px' }}>
        <Button
          variant="primary"
          size="lg"
          shape="pill"
          rightIcon={<SparklesIcon size={20} />}
          onClick={handleStart}
          style={{ minWidth: '280px' }}
        >
          Comenzar Práctica (20 Preguntas)
        </Button>

        <Button
          variant="secondary"
          size="lg"
          shape="pill"
          rightIcon={<FlameIcon size={20} />}
          onClick={onOpenHistory}
        >
          Historial y Debilidades
        </Button>
      </div>
    </div>
  );
};
