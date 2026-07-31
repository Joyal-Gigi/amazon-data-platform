"""
Centralized configuration constants for the data engineering project.

Contains reusable file paths and project-level constants.
"""

from pathlib import Path

#project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data directories
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
BRONZE_DIR = DATA_DIR / "bronze"
SILVER_DIR = DATA_DIR / "silver"
GOLD_DIR = DATA_DIR / "gold"

# Raw data file paths
ORDERS_CSV = RAW_DIR / "olist_orders_dataset.csv"
CUSTOMERS_CSV = RAW_DIR / "olist_customers_dataset.csv"
PRODUCTS_CSV = RAW_DIR / "olist_products_dataset.csv"
PAYMENTS_CSV = RAW_DIR / "olist_order_payments_dataset.csv"
ORDER_ITEMS_CSV = RAW_DIR / "olist_order_items_dataset.csv"

# Log directory
LOGS_DIR = PROJECT_ROOT / "logs"

# Application name
APP_NAME = "Data Engineering Pipeline"