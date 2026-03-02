# Dashboard Wireframe & Mockup: Climate Scope

**Milestone 2 Deliverable — Interactive Dashboard Design**

---

## Dashboard Overview

The Climate Scope dashboard will be a **multi-panel, interactive analytics interface** with four pages. The primary goal is to give users a clear, visual exploration of global weather patterns, extreme events, and regional comparisons.

**Technology Stack (planned for Milestone 3):** Plotly Dash or Streamlit

---

## Layout Architecture

```
┌────────────────────────────────────────────────────────────┐
│  🌍 CLIMATE SCOPE                          [Filters Panel] │
│  Global Weather Analytics Dashboard                        │
├──────────────────┬─────────────────────────────────────────┤
│                  │                                         │
│   SIDE NAV       │   MAIN CONTENT AREA                     │
│                  │                                         │
│ > Overview       │                                         │
│ > Temperature    │                                         │
│ > Precipitation  │                                         │
│ > Extreme Events │                                         │
│                  │                                         │
└──────────────────┴─────────────────────────────────────────┘
```

---

## Page 1: Overview / Global Map

**Purpose:** Give a bird's eye view of temperature and climate across the globe.

```
┌────────────────────────────────────────────────────────────────────────┐
│  PAGE: OVERVIEW                                                        │
│                                                                        │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │                                                                  │  │
│  │          🗺  CHOROPLETH MAP: Global Avg Temperature               │  │
│  │                (Color scale: Blue → Red)                         │  │
│  │          Hover: Country | Avg Temp | Avg Humidity                │  │
│  │                                                                  │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                        │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐           │
│  │  KPI CARD 1    │  │  KPI CARD 2    │  │  KPI CARD 3    │           │
│  │ 🌡 Global      │  │ 💧 Avg          │  │ 🌬 Avg Wind     │           │
│  │  Avg Temp      │  │  Precipitation │  │  Speed         │           │
│  │    17.4°C      │  │    0.04 mm     │  │   12.3 mph     │           │
│  └────────────────┘  └────────────────┘  └────────────────┘           │
│                                                                        │
│  Filters: [Country Multiselect ▼]  [Month Slider: Jan ──── Dec]       │
└────────────────────────────────────────────────────────────────────────┘
```

**Visualization:** Choropleth Map (Plotly Express `choropleth`)
**Interaction:** Click country → filters all charts on page. Month slider → updates map dynamically.

---

## Page 2: Temperature & Seasonal Trends

**Purpose:** Explore temperature distributions and seasonal patterns.

```
┌────────────────────────────────────────────────────────────────────────┐
│  PAGE: TEMPERATURE ANALYSIS                                            │
│                                                                        │
│  ┌──────────────────────────────┐  ┌──────────────────────────────┐   │
│  │ 📈 LINE CHART                │  │ 📊 HISTOGRAM                 │   │
│  │ Avg Temperature by Month     │  │ Distribution of Temperature  │   │
│  │ (multiple countries overlay) │  │ with KDE curve               │   │
│  │                              │  │                              │   │
│  │  Y: Temp (°C)                │  │  X: Temp range               │   │
│  │  X: Month (Jan-Dec)          │  │  Y: Frequency count          │   │
│  └──────────────────────────────┘  └──────────────────────────────┘   │
│                                                                        │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │ 🟦 HEATMAP: Correlation Matrix of Weather Variables               │  │
│  │  (Temp, Humidity, Wind, UV, Precipitation)                       │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                        │
│  Filters: [Region ▼]  [Date Range: Month Slider]                      │
└────────────────────────────────────────────────────────────────────────┘
```

**Visualizations:** Line Chart, Histogram+KDE, Correlation Heatmap

---

## Page 3: Extreme Weather Events

**Purpose:** Highlight and explore notable extreme weather observations.

```
┌────────────────────────────────────────────────────────────────────────┐
│  PAGE: EXTREME EVENTS                                                  │
│                                                                        │
│  [Toggle: 🌡 Extreme Heat | 🌧 Heavy Rain | 🌬 High Wind]              │
│                                                                        │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │         🗺  MAP: Locations of Extreme Events (Scatter Geo)        │  │
│  │         (Each dot = one extreme event; color by type)            │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                        │
│  ┌──────────────────────────────┐  ┌──────────────────────────────┐   │
│  │ 📦 BOX PLOT                  │  │ 📋 TABLE: Top 10 Events       │   │
│  │ Temp distribution by region  │  │ Country | Loc | Value | Date  │   │
│  │ with outliers visible        │  │ (sortable, filtered by type)  │   │
│  │                              │  │                              │   │
│  └──────────────────────────────┘  └──────────────────────────────┘   │
│                                                                        │
│  Threshold Sliders: [Heat > __ °C]  [Rain > __ mm]  [Wind > __ mph]  │
└────────────────────────────────────────────────────────────────────────┘
```

**Visualizations:** Scatter Geo Map, Box Plot, Sortable Table

---

## Page 4: Regional Comparison

**Purpose:** Side-by-side comparison of weather conditions across countries/regions.

```
┌────────────────────────────────────────────────────────────────────────┐
│  PAGE: REGIONAL COMPARISON                                             │
│                                                                        │
│  [Select Countries: India, USA, Brazil, Russia ▼]                     │
│  [Select Metric: Temperature ▼]                                        │
│                                                                        │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │ 📊 HORIZONTAL BAR CHART                                          │  │
│  │ Average [selected metric] by Country — sorted descending         │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                        │
│  ┌──────────────────────────────┐  ┌──────────────────────────────┐   │
│  │ 🎻 VIOLIN PLOT               │  │ 🔵 SCATTERPLOT               │   │
│  │ Temperature distribution     │  │ Temperature vs Humidity      │   │
│  │ by selected countries        │  │ (coloured by country)        │   │
│  └──────────────────────────────┘  └──────────────────────────────┘   │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

**Visualizations:** Bar Chart, Violin Plot, Scatterplot

---

## Visualization Type Summary

| Dashboard Panel | Chart Type | Library |
|---|---|---|
| Global temperature map | Choropleth Map | Plotly Express |
| Seasonal trends | Line Chart | Seaborn / Plotly |
| Temperature distribution | Histogram + KDE | Seaborn |
| Variable correlations | Correlation Heatmap | Seaborn |
| Extreme events map | Scatter Geo Map | Plotly Express |
| Distribution by region | Box Plot / Violin Plot | Plotly / Seaborn |
| Regional comparison | Horizontal Bar Chart | Plotly / Seaborn |
| Temp vs. Humidity | Scatterplot | Seaborn / Plotly |

---

## Interaction & Filter Design

| Filter | Location | Effect |
|---|---|---|
| Country/Region Dropdown | Top-right filter panel | All charts update for selected region |
| Month Slider | Top-right filter panel | All charts filter to selected month range |
| Extreme Event Toggle | Page 3 header | Toggles between heat / rain / wind extreme views |
| Metric Selector | Page 4 header | Switches the metric shown in comparison charts |
| Threshold Sliders | Page 3 bottom | Adjusts what counts as "extreme" for each variable |

---

## Color Scheme / Design Notes

- **Background:** Dark (#0F172A) with bright, vibrant accent colors
- **Temperature color scale:** Blue (cold) → Yellow → Red (hot) — perceptually intuitive
- **Card background:** Semi-transparent glass effect (#1E293B)
- **Font:** Inter or Roboto
- **Interactive elements:** Hover tooltips on all charts
