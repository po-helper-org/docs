---
nexus: market
node_id: aip-3-overview
node_type: step-overview
paf_step: 3
sprint_phase: null
kind: normative
owner: Portfolio Manager
confidence: 1.0
sources: ["[S1]", "[S2]", "[S3]", "[S4]", "RB-STEP-3"]
updated: 2026-06-20
ttl_days: 365
ripeness: fresh
tags: []
---

# overview — Step 3: Market

> Веха Discovery · Линза: **Strategy** · Fit-точка: — (первый гейт — Need/Value Fit в конце Step 4)
> Источник: [operating-model](../operating-model.md) (5 столпов, 3PL, CP, роли) · Термины — по naming_conventions.
> Версия Нексуса рынка: **v0.x (Stage 1) → v1.0 (Stage 3, CR ≥ 60%)**.

---

## 🎯 Цель шага в PAF-оптике

Насытить **Нексус рынка** верифицированными Узлами до **Спелости контекста (Context Ripeness) ≥ 60–75%**, достаточной для скаутинга возможностей/угроз (Принцип 5) и поднятия CP рыночных гипотез до **CP-gate стратегической линзы**. На выходе:

1. **7 типов Узлов** Нексуса рынка: **Force** (Porter/PESTEL) · **Trend** · **Constant** · **TAM-SAM-SOM** · **Competitor** · **Gap** · **Bet** (Strategy Lens).
2. **TAM/SAM/SOM → потенциал mNSM/NPV** (Принцип 6): SOM переводится в потенциал монетизируемой ценности; для AI-продуктов учитывается **COGS токенов**.
3. **Ставки (Bets)** — Bet-узлы Strategy Lens как элементы стратегического сценария: Strategic Sprint = долгосрочные цели + Нексус рынка → Ставки/Bets [S1] VI.1.

> **Сначала Нексус, потом Кортекс** [S1] IX — без спелого контекста Кортекс «усиливает мусор». Узел без источника (URL+дата) → CP=0, в Нексус не принимается.

---

## 🗡️ Карта фаз Sprint (активны в Step 3)

Шесть фаз цикла Product Sprint [S1] VI.4–VI.5 крутятся и здесь, но две — **тяжёлые** (рынок насыщается на SCOUT и кристаллизуется в BUNCH):

| Фаза | Активность в Step 3 | Вес |
|---|---|---|
| **PULSE** | Фиксация состояния Нексуса рынка (CR v0.x из Stage 1), гэп → intent | лёгкая |
| **SCOUT** | **ТЯЖЁЛАЯ.** Скаутинг рыночной среды через 3 Линзы: Force-узлы (Porter/PESTEL), Trend/Constant-узлы, TAM/SAM/SOM-узел, Competitor/Gap-узлы. Und-фаза Und-Id-Ex. | 🔴 |
| **BUNCH** | **ТЯЖЁЛАЯ.** Bet-узлы (Ставки) Strategy Lens; CP-gate по колесу Гилада + стоимость риска; GO/NO-GO/PIVOT. | 🔴 |
| **PITCH** | Pitching of Trust: защита Bet-узла, рост CP | средняя |
| **EXECUTE** | Лёгкая на discovery-этапе: фиксация Нексуса рынка v1.0; допущения → на верификацию в Customer Validation (RB-STEP-4) | лёгкая |
| **HARVEST** | Инкремент контекста: Нексус рынка v1.0 в Карту Целей; профиль потребителя v0.2 enriched рыночным контекстом | средняя |

---

## 📥 Вход / 📤 Выход

**Вход (из Step 0–2):**
- Нексус рынка v0.x (декларативный, из Stage 1 1.1 Нексус Рынка) + Нексус потребителя (сегменты, гипотеза mNSM из Step 2).
- Карта Целей (Goal Map) [S1] VI.1 — связь 3 Линз.
- Область потребностей конкретного сегмента (не «рынок в целом»).

**Выход (в Step 4):**
- **Нексус рынка v1.0** (CR ≥ 60–75%): 7 типов Узлов с метаданными (`источник[]`, `CP`, `timestamp`, `статус увядания`).
- **Bet-узлы** с `decision: GO | NO-GO | PIVOT` — Ставки Strategy Sprint.
- **mNSM/NPV-потенциал SOM** + явные `assumptions_to_verify` для RB-STEP-4.
- Профиль потребителя v0.2 enriched рыночным контекстом.

> **NO-GO — валидный осознанный отказ** (не провал): PAF — «сэкономил месяцы разработки».

---

## 👥 Роли

Step 3 = объект **Strategy Lens** [S1] VI.1 → **ведущая роль — Portfolio Manager** при поддержке Product Engineer и Product Ops.

| Роль | Функция на Step 3 | Зона |
|---|---|---|
| **Product Engineer** | Насыщает Нексус рынка через Кортекс; формулирует область потребностей и ключевой бизнес-кейс клиента; переводит Gap/Constant-узлы в аргументы Банча; защищает Bet на Pitching. | продукт |
| **Product Ops** | Строит инфраструктуру Нексуса (7 типов Узлов, RAG-индексы, 8 агентов, live-метрика CR); двигает команду по модели зрелости Кортекса [S1] VII. | product operations |
| **Portfolio Manager** | **Владелец Bet-узлов** (Ставки); максимизация NPV портфеля; баланс маржинальности/каннибализации; решение go/no-go/pivot. | портфель |

> ⚠️ **Зона человека (не делегируется ИИ) [S2] III.4:** стратегические Ставки (распределение ресурсов), формулировка констант, решение go/no-go, верификация рыночных цифр (метапознание). Агенты — инструменты, не акторы.

---

## 🤖 Кортекс: 8 агентов Step 3

Из `AI-TRANSFORMATION/RB-STEP-3-MARKET-RESEARCH/` (3.0–3.7):

1. **Nexus-Builder Agent** (рынок) — `3.0` — создаёт Узлы 7 типов, считает live-CR, event-based refresh.
2. **Агент рыночных сил** (Porter/PESTEL → Force-узлы) — `3.1`.
3. **Агент-трекер трендов и констант** — `3.2`.
4. **Агент-оценщик TAM/SAM/SOM** — `3.3` (top-down/bottom-up, правило ФРИИ 10%).
5. **Агент-верификатор рыночных цифр** (критический анти-workslop) — `3.3`.
6. **Агент-парсинг конкурентов** + **Агент-teardown** — `3.4`.
7. **Агент-скаутинг/скоринг** — `3.5` (веса = Рычаги, SAM «от конкурентов»).
8. **Агент-CP-gate** + **Агент-Bet (Bet Architect)** — `3.6` (колесо Гилада, стоимость риска).

---

## 🛡️ Главный риск шага: TAM-галюцинации

**Workslop-зона №1 всей библиотеки** (reformation §3.9): ИИ генерирует «правдоподобные» рыночные цифры. Защита:
- Каждая рыночная цифра → **URL+дата**. Без источника → **CP=0**, флаг «галюцинация», в расчёт не принимается.
- Маркировка **факт** / **гипотеза** / **бенчмарк** на каждом Узле.
- Иллюзия точности = workslop: «SAM = 487 356 000 ₽» без источника — иллюзия; «SAM ≈ 500 млн ₽ ± 50%» — корректно.
- Запрет на «рынок в целом»: оценка только в контексте области потребностей.

---

## 🔗 Референсы

- **Методы:** index + 3.1 (рыночная среда) · 3.2 (тренды) · 3.3 (TAM/SAM/SOM) · 3.4 (конкуренты) · 3.5 (скоринг) · 3.6 (фиксация).
- **«Почему»:** [3.0 instruction](../../ai-transformation/RB-STEP-3-MARKET-RESEARCH/3.0-instruction.md) · [3.1 instruction](../../ai-transformation/RB-STEP-1-IDEA/3.1-instruction.md) · [3.2 instruction](../../ai-transformation/RB-STEP-1-IDEA/3.2-instruction.md) · [3.3 instruction](../../ai-transformation/RB-STEP-1-IDEA/3.3-instruction.md) · [3.4 instruction](../../ai-transformation/RB-STEP-3-MARKET-RESEARCH/3.4-instruction.md) · [3.5 instruction](../../ai-transformation/RB-STEP-3-MARKET-RESEARCH/3.5-instruction.md) · [3.6 instruction](../../ai-transformation/RB-STEP-3-MARKET-RESEARCH/3.6-instruction.md) · [3.7 instruction](../../ai-transformation/RB-STEP-3-MARKET-RESEARCH/3.7-instruction.md) · [reformation §3](../../ai-transformation/reformation.md).
- Фазы шага: [1.pulse](1.pulse.md) · [2.scout](2.scout.md) · [3.bunch](3.bunch.md) · [4.pitch](4.pitch.md) · [5.execute](5.execute.md) · [6.harvest](6.harvest.md).
- Назад: [overview](../STEP-2-CUSTOMER/overview.md) · Дальше: overview (Need/Value Fit).

---

## 🧩 Skill Map / профстандарт

- **Skill Map [S3]:** сектор **1 Discovery & Researches** (качественные и количественные исследования рынка) + сектор **6 Sales & Economics** (оценка объёма рынка TAM/SAM/SOM, NPV-потенциал).
- **Профстандарт 06.012 [S4]:** обобщённая функция **D** «Управление портфелем», уровень 7, трудовая функция **D/01.7 «исследования новых рынков»** (Portfolio Manager / CPO; интерпретативная связка по [S3]+[S4]). Функция **B/01.5 «продуктовые исследования»** — Product Engineer (teardown, скоринг).

> ⚠️ Связка стандарт ↔ PAF — **интерпретативная** [S3]. PAF переопределяет **способ** работы на каждом уровне — через Нексус и Кортекс, не вручную [S1].

---
**Version:** 1.0 · **Last updated:** 2026-06-20 · **Maintained by:** AI-KORTEX
