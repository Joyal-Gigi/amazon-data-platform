# Amazon Data Platform

A portfolio-grade Data Engineering project that simulates the data platform of a large-scale e-commerce company using PySpark and modern lakehouse architecture.

---

## Project Goals

- Build production-style ETL pipelines using PySpark
- Implement data validation and cleansing
- Store data efficiently using Parquet
- Perform analytics using Spark SQL
- Orchestrate pipelines with Apache Airflow
- Prepare data for reporting tools like Microsoft Fabric and Power BI

---

## Tech Stack

- Python
- PySpark
- SQL
- Parquet
- Git & GitHub
- Docker *(Upcoming)*
- Apache Airflow *(Upcoming)*
- Microsoft Fabric *(Upcoming)*

---

## Project Structure

```text
amazon-data-platform/
│
├── data/
│   ├── raw/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── src/
├── tests/
├── notebooks/
├── logs/
├── requirements.txt
└── README.md
```

---

## Setup

Clone the repository:

```bash
git clone <repository-url>
cd amazon-data-platform
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Roadmap

- [x] Sprint 0 - Project Setup
- [ ] Sprint 1 - Bronze Layer
- [ ] Sprint 2 - Silver Layer
- [ ] Sprint 3 - Gold Layer
- [ ] Sprint 4 - Incremental Processing
- [ ] Sprint 5 - Apache Airflow
- [ ] Sprint 6 - Performance Optimization
- [ ] Sprint 7 - Microsoft Fabric Integration

---

## Dataset

This project uses the **Brazilian E-Commerce Public Dataset by Olist**.

The dataset is publicly available on Kaggle and is not included in this repository.

Download it from Kaggle and place the required CSV files inside:

```text
data/raw/
```

## Author

**Joyal Gigi**
