# Milestone 1 Report: Data Acquisition & Preprocessing

**Project:** Climate Scope — Global Weather Pattern Analysis  
**Dataset:** `GlobalWeatherRepository.csv` (Raw) → `cleaned_weather_data.csv` (Processed)  
**Date:** February 2026

---

## 1. Executive Summary

This report documents the completion of **Milestone 1** for the Climate Scope project. The primary objective of this phase was to acquire the initial "Global Weather Repository" dataset and perform rigorous data cleaning and preprocessing. The resulting clean dataset forms the reliable foundation required for the statistical analysis and dashboard development planned in subsequent milestones.

---

## 2. Data Acquisition

The raw dataset was sourced directly from Kaggle via the Kaggle API. 

- **Source:** Global Weather Repository
- **Initial Volume:** ~300,000+ daily weather observations across thousands of global locations.
- **Key Metrics Included:** Temperature (°C), Wind Speed (mph), Precipitation (mm), Humidity (%), UV Index, Air Quality (PM2.5), and Categorical Weather Conditions (e.g., "Sunny", "Overcast").

---

## 3. Data Cleaning & Preprocessing Steps

To ensure downstream analytical accuracy, a robust data cleaning pipeline was implemented in `notebooks/milestone1.ipynb`.

### 3.1 Handling Missing and Duplicate Data
- **Duplicates:** The dataset was scanned for identical row entries based on unique `(country, location_name, last_updated)` combinations. All duplicates were systematically removed to prevent aggregational skewing.
- **Null Values:** Missing numerical values (e.g., occasional missing UV index or pressure readings) were imputed or dropped based on their frequency and impact on the overall dataset integrity.

### 3.2 Data Type Standardization
Several columns required type casting to ensure they could be manipulated mathematically:
- `last_updated` was converted from a standard string/object type into a native Python `datetime` object.
- Numerical columns imported as strings (due to hidden artifacts) were forcibly cast to `float64` or `int64`.

### 3.3 Feature Engineering (Date Extraction)
To prepare for upcoming Time Series analysis, the `last_updated` datetime column was decomposed into several distinct analytical features:
- `date`: Plucked out for daily aggregation.
- `month` / `month_name`: Extracted for seasonal analysis.
- `hour`: Extracted to analyze diurnal temperature cycles.

---

## 4. Deliverables Generated

The successful execution of the cleaning pipeline resulted in the generation of two core artifacts located in the `data/` directory:

1. **`cleaned_weather_data.csv`**: The master dataset, fully sanitized and enhanced with new datetime features, ready for exploratory data analysis (EDA).
2. **`monthly_weather_summary.csv`**: A pre-aggregated dataset summarizing average key metrics at the month-level to expedite high-level seasonal plotting.

---

## 5. Conclusion

The data infrastructure is now sound. With the data cleaned, normalized, and correctly typed, the project is officially positioned to move into **Milestone 2**, which will involve extracting statistical insights, mapping extreme events, and identifying geospatial weather correlations.
