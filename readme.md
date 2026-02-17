🌍 ClimateScope: Visualizing Global Weather Trends

![Status](https://img.shields.io/badge/Status-Milestone%201%20Complete-success)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)

**ClimateScope** is a data analytics project designed to analyze and visually represent global weather patterns. [cite_start]By leveraging the Global Weather Repository dataset, this project aims to uncover seasonal trends, regional variations, and extreme weather events through interactive visualizations[cite: 3].

---

## 📖 Table of Contents
- [Objective](#-objective)
- [Tech Stack](#-tech-stack)
- [Dataset](#-dataset)
- [Project Structure](#-project-structure)
- [Installation & Setup](#-installation--setup)
- [Milestones](#-milestones)
- [Reports](#-reports)

---

## 🎯 Objective
[cite_start]The primary goal is to provide an accessible, data-driven platform that supports climate awareness[cite: 6].
* [cite_start]**Analyze:** Daily-updated worldwide weather data[cite: 5].
* [cite_start]**Visualize:** Comparisons of conditions across regions and continents[cite: 5].
* [cite_start]**Identify:** Anomalies, heatwaves, and extreme precipitation events[cite: 5].

---

## 🛠 Tech Stack
* [cite_start]**Language:** Python 3.x [cite: 61]
* [cite_start]**Data Handling:** Pandas, NumPy [cite: 63]
* [cite_start]**Data Acquisition:** Kaggle API [cite: 64]
* [cite_start]**Visualization:** Matplotlib, Seaborn (Milestone 1), Plotly (Planned) [cite: 66]

---

## 📊 Dataset
* [cite_start]**Source:** [Global Weather Repository (Kaggle)](https://www.kaggle.com/datasets/nelgiriyewithana/global-weather-repository) [cite: 11]
* [cite_start]**Description:** Daily weather data including temperature (Celsius), wind speed, precipitation, humidity, and atmospheric pressure[cite: 14].
* [cite_start]**Data Cleaning:** Duplicates removed, missing values handled, and daily data aggregated into monthly averages[cite: 20].

---

## 📂 Project Structure
```text
ClimateScope/
│
├── data/                      # Data storage (ignored by git)
│   ├── clean_weather_data.csv # Processed daily data
│   └── monthly_weather_summary.csv # Aggregated monthly data
│
├── milestone1.ipynb           # Main analysis notebook with visualizations
├── Milestone1_Report.md       # Summary of data quality and schema
├── requirements.txt           # Python dependencies
├── .gitignore                 # Security file (API keys, data)
└── README.md                  # Project documentation
⚙️ Installation & Setup
1. Clone the Repository
Bash
git clone [https://github.com/AjayBora002/Springboard_Milestone1.git](https://github.com/AjayBora002/Springboard_Milestone1.git)
cd Springboard_Milestone1
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