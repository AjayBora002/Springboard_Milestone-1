# 🌍 ClimateScope: Visualizing Global Weather Trends

![Status](https://img.shields.io/badge/Status-Milestone%201%20Complete-success)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)

[cite_start]**ClimateScope** is a data analytics project designed to analyze and visually represent global weather patterns[cite: 3]. [cite_start]By leveraging the Global Weather Repository dataset, this project aims to uncover seasonal trends, regional variations, and extreme weather events through interactive visualizations[cite: 4].

---

## 📖 Table of Contents
- [Objective](#-objective)
- [Tech Stack](#-tech-stack)
- [Dataset](#-dataset)
- [Project Structure](#-project-structure)
- [Installation & Setup](#-installation--setup)
- [Milestones](#-milestones)

---

## 🎯 Objective
[cite_start]The primary goal is to provide an accessible, data-driven platform that supports climate awareness[cite: 6].
* **Analyze:** Daily-updated worldwide weather data.
* [cite_start]**Visualize:** Comparisons of conditions across regions and continents[cite: 5].
* [cite_start]**Identify:** Anomalies, heatwaves, and extreme precipitation events[cite: 5].

---

## 🛠 Tech Stack
* [cite_start]**Language:** Python 3.x [cite: 61]
* [cite_start]**Data Handling:** Pandas, NumPy [cite: 63]
* [cite_start]**Data Acquisition:** Kaggle API [cite: 64]
* [cite_start]**Visualization (Upcoming):** Plotly, Streamlit [cite: 66, 67]

---

## 📊 Dataset
* [cite_start]**Source:** [Global Weather Repository (Kaggle)](https://www.kaggle.com/datasets/nelgiriyewithana/global-weather-repository) [cite: 10]
* **Description:** Daily weather data including temperature (Celsius), wind speed, precipitation, humidity, and atmospheric pressure.
* [cite_start]**Data Cleaning:** Duplicates removed, missing values handled, and daily data aggregated into monthly averages[cite: 81, 83].

---

## 📂 Project Structure
```text
ClimateScope/
│
├── data/                      # Data storage (ignored by git)
│   ├── clean_weather_data.csv # Processed daily data
│   └── monthly_weather_summary.csv # Aggregated monthly data
│
├── milestone1.ipynb           # Main analysis notebook
├── requirements.txt           # Python dependencies
├── .gitignore                 # Security file (API keys, data)
└── README.md                  # Project documentation



⚙️ Installation & Setup
1. Clone the Repository
Bash
git clone [https://github.com/YourUsername/ClimateScope.git](https://github.com/YourUsername/ClimateScope.git)
cd ClimateScope
2. Install Dependencies
Bash
pip install -r requirements.txt
3. Configure Kaggle API
Place your kaggle.json file in the root directory.

Note: This file is ignored by Git for security.

4. Run the Analysis
Open the Jupyter Notebook to download data and generate the clean datasets:

Bash
jupyter notebook milestone1.ipynb

🏆 Milestones

Milestone	Description	Status

Milestone 1	
Data Preparation: Fetching data via API, cleaning, and initial aggregation.
✅ Completed

Milestone 2	
Core Analysis: Statistical analysis, identifying trends and outliers.
⏳ In Progress

Milestone 3	
Visualization: Building interactive charts and maps.
📅 Planned

Milestone 4	
Dashboard: Final Streamlit dashboard deployment.
📅 Planned

Author: Ajay Bora

Internship: Infosys Springboard Data Visualization Internship