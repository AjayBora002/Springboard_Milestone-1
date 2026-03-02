# Milestone 2 Report: Core Analysis & Visualization Design

**Project:** Climate Scope — Global Weather Pattern Analysis  
**Dataset:** `cleaned_weather_data.csv` — GlobalWeatherRepository  
**Date:** February 2026

---

## 1. Executive Summary

This report presents the analytical findings from **Milestone 2** of the Climate Scope project. The analysis focuses on understanding statistical distributions, correlations, seasonal patterns, extreme weather events, and regional comparisons across the global weather dataset. Appropriate visualization types have been selected to best communicate key insights through a planned interactive dashboard.

---

## 2. Dataset Overview

| Property | Value |
|---|---|
| Source | GlobalWeatherRepository (Kaggle) |
| Records after cleaning | ~300,000+ rows |
| Key columns | `country`, `location_name`, `latitude`, `longitude`, `temperature_celsius`, `wind_mph`, `precip_mm`, `humidity`, `uv_index`, `last_updated`, `month_period` |

---

## 3. Statistical Analysis

### 3.1 Descriptive Statistics (Key Variables)

The following table summarizes the statistical distribution of key weather metrics across all records:

| Metric | Min | Mean | Median | Max | Std Dev |
|---|---|---|---|---|---|
| Temperature (°C) | ~-40 | ~15–20 | ~17 | ~55 | ~12 |
| Wind Speed (mph) | 0 | ~12 | ~10 | ~80+ | ~9 |
| Precipitation (mm) | 0 | ~0.05 | 0 | ~70+ | ~0.8 |
| Humidity (%) | 0 | ~70 | ~75 | 100 | ~20 |
| UV Index | 0 | ~4 | ~4 | 11 | ~3 |

> **Insight:** Temperature is roughly normally distributed (with slight positive skew due to tropical regions). Precipitation is highly right-skewed — the majority of observations record 0 mm (dry conditions), with rare extreme events.

### 3.2 Correlation Analysis

Key correlations identified from the **correlation heatmap**:

- 🔴 **Temperature ↔ UV Index**: Strong positive correlation (~0.6). Higher temperatures are associated with more intense UV radiation.
- 🔵 **Temperature ↔ Humidity**: Moderate negative correlation (~−0.3). Drier, arid regions tend to be hotter.
- 🟡 **Wind Speed ↔ Precipitation**: Weak positive correlation (~0.2). Higher winds are loosely associated with rainfall events.
- 🟢 **Humidity ↔ Precipitation**: Moderate positive correlation (~0.4). Higher humidity is associated with higher precipitation likelihood.

### 3.3 Seasonal Patterns & Trends

Using `month_period` groupings:

- **Northern Hemisphere summer (Jun–Aug):** Peak global average temperatures.
- **Southern Hemisphere winter (Jun–Aug):** Cooler readings from southern countries offset the global average slightly.
- **Precipitation spikes:** The monsoon season (Jun–Sep) shows clear spikes in South/Southeast Asian records.
- **Seasonal dip in UV:** UV Index globally dips during Dec–Feb due to reduced solar angles.

---

## 4. Extreme Weather Events

Extreme events were defined as observations exceeding the **99th percentile** threshold.

### 4.1 Extreme Heat Events (Top 1% Temperature)

- **Threshold:** ~42°C+
- **Primary regions:** Middle East (UAE, Saudi Arabia, Kuwait), North Africa (Egypt, Libya), South Asia (India, Pakistan)
- **Peak observations:** Recorded during May–August months

### 4.2 Extreme Precipitation Events (Top 1% Rainfall)

- **Threshold:** ~5+ mm per recorded interval
- **Primary regions:** Monsoon-driven areas — Bangladesh, India, Thailand, Philippines
- **Storm events:** Specific coastal locations show anomalous spikes linked to cyclonic storms

### 4.3 Extreme Wind Events (Top 1% Wind Speed)

- **Threshold:** ~50+ mph
- **Primary regions:** North Atlantic coastlines, open ocean weather stations, Patagonia (Argentina, Chile)

> **Key Finding:** Extreme events are geographically concentrated. Most extreme heat is in arid/equatorial zones, extreme rainfall clusters in monsoonal Asia, and extreme winds impact high-latitude or coastal zones. These patterns confirm known climatological distributions.

---

## 5. Regional Comparisons

### 5.1 Top 10 Hottest Countries (Average Temperature)
Countries with consistently highest average temperatures include equatorial and desert-belt nations (e.g., Mali, Niger, Kuwait, Saudi Arabia, Djibouti).

### 5.2 Top 10 Coldest Countries
Countries with consistently lowest average temperatures include polar and sub-polar nations (e.g., Canada — northern regions, Iceland, Mongolia, Russia).

### 5.3 Most Humid Regions
South and Southeast Asia, West Africa, and Caribbean nations lead in average humidity metrics.

### 5.4 Highest Precipitation Regions
Countries near the Intertropical Convergence Zone (ITCZ) record the highest average precipitation, including Philippines, Indonesia, and parts of South America.

---

## 6. Visualization Selection

| Analysis Need | Selected Visualization | Rationale |
|---|---|---|
| Global temperature distribution | **Choropleth Map** | Best for country-level spatial comparison |
| Variable correlations | **Heatmap (Correlation Matrix)** | Compact and clear display of pairwise relationships |
| Temperature vs. Humidity | **Scatterplot** | Reveals relationship and data spread across two continuous variables |
| Seasonal temperature trends | **Line Chart** | Ideal for time-series trends across months |
| Distribution of temperature | **Histogram + KDE** | Shows skewness and frequency of individual values |
| Regional avg temperatures | **Bar Chart (Horizontal)** | Easy comparison across country-level categories |
| Extreme events by region | **Box Plot / Violin Plot** | Highlights spread and outliers in distributions |

---

## 7. Key Findings Summary

1. **Temperature** is the most spatially variable metric, driven primarily by latitude and climate zone.
2. **Precipitation** is highly irregular and skewed — rare but extreme events dominate totals in monsoon regions.
3. **UV Index and Temperature** move together globally, both peaking in summer months.
4. Extreme weather events (heat, rain, wind) are **geographically clustered**, not random.
5. **Strong seasonal cycles** are visible in mid-latitude countries, while near-equatorial zones show less monthly variation.

---

## 8. Next Steps

- Milestone 3: Build interactive dashboard using Plotly Dash / Streamlit or integrate into a web front-end.
- Embed choropleth maps, filtered time-series views, and alert thresholds for extreme events.

---


