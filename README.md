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
- [x] Sprint 1 - Bronze Layer
- [x] Sprint 2 - Silver Layer
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

## Data Architecture

The project follows a Bronze → Silver data processing architecture.

### Bronze Layer

The Bronze layer stores validated incoming Orders data in Parquet format.

The ingestion pipeline:

1. Reads Orders data from CSV
2. Applies an explicit Spark schema
3. Validates incoming records
4. Separates valid and invalid records
5. Writes valid records to the Bronze layer as Parquet

### Silver Layer

The Silver layer contains cleansed and transformed Orders data.

The Silver pipeline:

1. Reads Bronze Parquet data
2. Removes duplicate Orders using `order_id`
3. Trims whitespace from string fields
4. Normalizes `order_status` to lowercase
5. Applies the defined null-handling strategy
6. Adds `silver_processed_timestamp`
7. Writes the resulting data to Silver Parquet

### Pipeline

Bronze:

CSV → Explicit Schema → Validation → Bronze Parquet

Silver:

Bronze Parquet → Cleansing → Null Handling → Transformation → Silver Parquet

## Data Quality Rules

### Schema

Orders data is loaded using an explicit Spark schema rather than automatic schema inference.

The following fields are defined:

| Column | Data Type |
|---|---|
| `order_id` | String |
| `customer_id` | String |
| `order_status` | String |
| `order_purchase_timestamp` | Timestamp |
| `order_approved_at` | Timestamp |
| `order_delivered_carrier_date` | Timestamp |
| `order_delivered_customer_date` | Timestamp |
| `order_estimated_delivery_date` | Timestamp |

### Validation

The following fields are treated as mandatory:

- `order_id`
- `customer_id`
- `order_status`
- `order_purchase_timestamp`

Records missing mandatory fields are classified as invalid and separated from valid records.

### Cleansing

The Silver cleansing process:

- Removes duplicate records using `order_id` as the business key
- Trims leading and trailing whitespace from string columns
- Normalizes `order_status` to lowercase

### Null Handling

Mandatory fields are handled during validation.

Optional nullable business fields are preserved as `NULL` where appropriate rather than being replaced with arbitrary values.

## Application Logging

The pipeline uses structured application logging to trace execution.

Logs capture:

- Pipeline start and completion
- Bronze data reads
- Data cleansing
- Duplicate record counts
- Null handling
- Transformations
- Silver data writes
- Silver layer verification
- Pipeline failures and error details

## Project Status

### Completed

- [x] Orders CSV ingestion
- [x] Explicit Orders schema
- [x] Incoming record validation
- [x] Bronze Parquet ingestion
- [x] Data cleansing
- [x] Null handling strategy
- [x] Deduplication
- [x] Silver transformation pipeline
- [x] Application logging
- [x] Unit tests for validation, cleansing, and transformation logic
- [x] Bronze → Silver pipeline verification

## Author

**Joyal Gigi**
