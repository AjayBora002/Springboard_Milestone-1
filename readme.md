# 🌍 ClimateScope: Visualizing Global Weather Trends

![Status](https://img.shields.io/badge/Status-Milestone%202%20Complete-success)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)

**ClimateScope** is a data analytics project that analyzes and visually represents global weather patterns. By leveraging the Global Weather Repository dataset, this project uncovers seasonal trends, regional variations, and extreme weather events through statistical analysis and interactive visualizations.

---

## 📖 Table of Contents
- [Objective](#-objective)
- [Tech Stack](#-tech-stack)
- [Dataset](#-dataset)
- [Project Structure](#-project-structure)
- [Milestones](#-milestones)
- [Installation & Setup](#-installation--setup)
- [Reports](#-reports)

---

## 🎯 Objective

- **Analyze:** Daily-updated worldwide weather data across 300,000+ global observations.
- **Visualize:** Comparisons of temperature, precipitation, humidity, and wind across regions.
- **Identify:** Anomalies, heatwaves, extreme precipitation events, and seasonal patterns.

---

## 🛠 Tech Stack

| Category | Libraries |
|---|---|
| Language | Python 3.x |
| Data Handling | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly Express |
| Notebook | Jupyter Notebook |
| Data Acquisition | Kaggle API |
| Dashboard (M3) | Plotly Dash / Streamlit *(planned)* |

---

## 📊 Dataset

- **Source:** [Global Weather Repository (Kaggle)](https://www.kaggle.com/datasets/nelgiriyewithana/global-weather-repository)
- **Description:** Daily weather data including temperature (°C), wind speed (mph), precipitation (mm), humidity (%), UV index, and atmospheric pressure across thousands of global locations.
- **Data Cleaning (Milestone 1):** Duplicates removed, missing values handled, columns standardized, and daily data aggregated into monthly summaries.

---

## 📂 Project Structure

```text
Climate_Scope/
│
├── data/                              # Data storage (excluded from git)
│   ├── GlobalWeatherRepository.csv    # Raw dataset from Kaggle
│   ├── cleaned_weather_data.csv       # Processed & cleaned dataset
│   └── monthly_weather_summary.csv    # Aggregated monthly data
│
├── notebooks/
│   ├── milestone1.ipynb               # M1: Data ingestion, cleaning, EDA
│   └── milestone2_executed.ipynb      # M2: Statistical analysis & visualizations
│
├── reports/
│   ├── milestone2_report.md           # M2: Full analytical findings report
│   └── dashboard_mockup.md            # M2: Dashboard wireframe & design spec
│
├── requirements.txt                   # Python dependencies with version pins
├── .gitignore                         # Excludes data files and API keys
└── README.md                          # Project documentation
```

---

## 🏁 Milestones

### ✅ Milestone 1 — Data Acquisition & Cleaning
- Downloaded Global Weather Repository via Kaggle API
- Cleaned 300,000+ records: removed duplicates, handled nulls, standardized column types
- Generated `cleaned_weather_data.csv` and `monthly_weather_summary.csv`
- **Notebook:** [`notebooks/milestone1.ipynb`](notebooks/milestone1.ipynb)

### ✅ Milestone 2 — Core Analysis & Visualization Design
- **Statistical Analysis:** Descriptive stats, correlation matrix, skewness/IQR, seasonal trends
- **Extreme Weather Events:** Identified top-1% heat, precipitation, and wind events (Z-score & percentile methods)
- **Regional Comparisons:** Top 10 hottest/coldest countries, most humid and highest-precipitation regions
- **Visualization Selection:** Choropleth maps, Line charts, Scatterplots, Heatmaps, Box plots, Histograms
- **Dashboard Design:** Full wireframe with 4-page interactive layout ([`reports/dashboard_mockup.md`](reports/dashboard_mockup.md))
- **Notebook:** [`notebooks/milestone2_executed.ipynb`](notebooks/milestone2_executed.ipynb)
- **Report:** [`reports/milestone2_report.md`](reports/milestone2_report.md)

### 🔜 Milestone 3 — Interactive Dashboard (Upcoming)
- Build interactive dashboard using Plotly Dash or Streamlit
- Embed choropleth maps, filtered time-series views, and extreme event alert thresholds

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/AjayBora002/Springboard_Milestine1.git
cd Springboard_Milestine1
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Kaggle API
Place your `kaggle.json` file in the root directory.
> ⚠️ This file is listed in `.gitignore` and will **not** be committed to Git.

### 4. Run the Analysis

**Milestone 1 — Data Cleaning:**
```bash
jupyter notebook notebooks/milestone1.ipynb
```

**Milestone 2 — Statistical Analysis & Visualizations:**
```bash
jupyter notebook notebooks/milestone2_executed.ipynb
```

---

## 📄 Reports

| Report | Description |
|---|---|
| [`reports/milestone2_report.md`](reports/milestone2_report.md) | Full Milestone 2 analytical findings — statistics, extreme events, regional comparisons, visualization rationale |
| [`reports/dashboard_mockup.md`](reports/dashboard_mockup.md) | Dashboard wireframe & interaction design for Milestone 3 |