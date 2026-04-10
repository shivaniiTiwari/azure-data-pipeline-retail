# 🚀 Azure Data Engineering Pipeline Project

## 📌 Overview
This project demonstrates an end-to-end data engineering pipeline using Azure services and Databricks.

The pipeline ingests raw retail data, processes it using PySpark, and stores the transformed data in a structured format for analysis.

---

## 🏗️ Architecture
ADF → ADLS → Databricks → Delta

---

## ⚙️ Tech Stack
- Azure Data Factory (ADF)
- Azure Data Lake Storage (ADLS)
- Databricks (PySpark)
- Delta Lake

---

## 🔄 Pipeline Flow

1. **Data Ingestion (ADF)**
   - Data is ingested from source into ADLS

2. **Storage (ADLS)**
   - Raw data stored in data lake

3. **Data Processing (Databricks)**
   - Data cleaned and transformed using PySpark
   - Column formatting and typ
