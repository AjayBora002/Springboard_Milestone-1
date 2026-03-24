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
├── data/
│   ├── raw/                           # Raw datasets (excluded from git)
│   │   └── GlobalWeatherRepository.csv
│   └── processed/                     # Cleaned & aggregated data
│       ├── cleaned_weather_data.csv
│       └── monthly_weather_summary.csv
│
├── src/                               # Source code
│   ├── dashboard.py                   # Main Streamlit app
│   └── services/                      # API & helper services
│       └── weather_service.py
│
├── notebooks/
│   ├── milestone1.ipynb               # M1: Data ingestion, cleaning, EDA
│   └── milestone2.ipynb               # M2: Statistical analysis & visualizations
│
├── reports/                           # Analytical findings & mockups
├── requirements.txt                   # Python dependencies
├── .env.example                       # API configuration template
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

### ✅ Milestone 3 — Interactive Dashboard & Live API
- Built interactive dashboard using Streamlit
- Integrated OpenWeatherMap API for real-time global weather
- Added Travel Assistant with live climate check
- Reorganized project into a clean `src/` architecture

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/AjayBora002/Climate_Scope.git
cd Climate_Scope
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API Keys
- Place your `kaggle.json` in the root directory.
- Create a `.env` file in the root directory and add your OpenWeatherMap API key:
  ```text
  OPENWEATHER_API_KEY=your_actual_key_here
  ```

### 4. Run the Dashboard
```bash
streamlit run src/dashboard.py
```

---

## 🚀 Streamlit Cloud Deployment

To deploy this project on Streamlit Cloud:

1. **GitHub Setup:** Ensure all your code (including `requirements.txt` and `src/dashboard.py`) is pushed to your GitHub repository.
2. **Streamlit Cloud:** Sign in to [Streamlit Cloud](https://share.streamlit.io/) using your GitHub account.
3. **Deploy App:** Click "New app", select your `Climate_Scope` repository and the `Ajay_Bora` branch.
4. **Main File Path:** Set the "Main file path" to `src/dashboard.py`.
5. **Secrets:** In the app settings on Streamlit Cloud, go to "Secrets" and add your API key:
   ```toml
   OPENWEATHER_API_KEY = "your_open_weather_api_key_here"
   ```
   *Note: Streamlit Cloud will automatically handle the mapping between these secrets and your `os.getenv` calls.*

---

## 📄 Reports

| Report | Description |
|---|---|
| [`reports/milestone2_report.md`](reports/milestone2_report.md) | Full Milestone 2 analytical findings — statistics, extreme events, regional comparisons, visualization rationale |
| [`reports/dashboard_mockup.md`](reports/dashboard_mockup.md) | Dashboard wireframe & interaction design for Milestone 3 |