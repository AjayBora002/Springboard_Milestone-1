# Dashboard Wireframe & Mockup: Climate Scope

**Final Deliverable — Integrated Analytical Platform**

---

## Dashboard Overview

The **Climate Scope v2.0** dashboard is a high-performance, dark-themed analytics platform featuring **seven specialized panels**. It bridges the gap between massive historical datasets (300k+ records) and real-time environmental decision-making via OpenWeatherMap API integration.

**Technology Stack:** Streamlit, Plotly, Pandas, OpenWeatherMap API, Custom Glassmorphism CSS (Premium Redesign v2.0).

---

## Layout Architecture (7-Panel View)

```
┌────────────────────────────────────────────────────────────┐
│  🌍 CLIMATE SCOPE      v2.0 Presentation Mode (No Toolbar) │
│  [Navigation Menu]     [Global Feature Filters]            │
├──────────────────┬─────────────────────────────────────────┤
│                  │                                         │
│   SIDERBAR       │   MAIN ANALYTICS STAGE                  │
│   (Gradients)    │   (Animated Page Transitions)           │
│                  │                                         │
│ > Overview       │   ┌──────────────────────────────────┐  │
│ > Temp/Humidity  │   │      Premium KPI Hero Banner     │  │
│ > Rain/Wind      │   └──────────────────────────────────┘  │
│ > Extremes       │   ┌──────────────┐    ┌──────────────┐  │
│ > Live Search    │   │ [Chart Slot] │    │ [Chart Slot] │  │
│ > Travel Risk    │   └──────────────┘    └──────────────┘  │
│ > Predictive     │                                         │
└──────────────────┴─────────────────────────────────────────┘
```

---

## Category 1: Historical Insights (Milestones 1-2)

### Page 1-4: Descriptive Analytics
- **Global Overview:** Interactive choropleth maps and regional distribution KPIs.
- **Deep-Dive Views:** Specializing in Temperature, Precipitation/Wind, and Extreme Event anomalies using **99th percentile** threshold detection.
- **Interaction:** Synchronized filters for month-of-year and regional granularity.

---

## Category 2: Real-Time & Forecasting (Milestones 3-4)

### Page 5: 📡 Live Global Search
- **Functionality:** Direct API bridge to OpenWeatherMap.
- **Features:** Instant weather retrieval, local sunrise/sunset, and localized time display for any city globally.

### Page 6: 🧳 Travel Risk Monitor
- **Fusion Logic:** Combines historical seasonal profiles with a **5-Day Live Forecast**.
- **Advisory:** Smart weather advice (Packing, Safety, Comfort Scores) generated from historical stability patterns.

### Page 7: 🔮 Predictive Outlook
- **Predictive Intelligence:** Seasonal projections with **Uncertainty Bands (Standard Deviation)**.
- **Risk Assessment:** Forward-looking hazard cards (Heatwave, Flood, Solar Capacity) for long-term strategic planning.

---

## Visualization & Interaction Summary

| Component | Implementation | Feature |
|---|---|---|
| **Design System** | Glassmorphism v2.0 | Absolute clean mode (hidden Streamlit UI) |
| **KPI Cards** | Custom CSS + SVG | Animated hover scales & focus rings |
| **Trend Lines** | Plotly GO | Multi-line seasonal overlays with highlight bands |
| **Forecasts** | HTML Component | Responsive 5-day grid with weather-sync icons |
| **Animations** | CSS Keyframes | Sequential fade-in on page navigation |

---

## Design Evolution Notes (v2.0)

- **Presentation Ready:** All Streamlit native "Deploy" and "Stop" buttons are programmatically hidden.
- **Responsive Font:** Plus Jakarta Sans with fluid `clamp()` sizing for headings.
- **Ambient Lighting:** Contextual radial glows on cards based on weather severity (Danger/Warning/Success).
- **Metric Stability:** Fixed container widths to prevent UI jumping during data reloads.
