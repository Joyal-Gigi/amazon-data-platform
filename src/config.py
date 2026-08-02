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
BRONZE_ORDERS_DIR = BRONZE_DIR / "orders"
BRONZE_CUSTOMERS_DIR = BRONZE_DIR / "customers"
BRONZE_PRODUCTS_DIR = BRONZE_DIR / "products"
BRONZE_PAYMENTS_DIR = BRONZE_DIR / "payments"
BRONZE_ORDER_ITEMS_DIR = BRONZE_DIR / "order_items"

SILVER_DIR = DATA_DIR / "silver"
SILVER_ORDERS_DIR = SILVER_DIR / "orders"
SILVER_CUSTOMERS_DIR = SILVER_DIR / "customers"
SILVER_PRODUCTS_DIR = SILVER_DIR / "products"
SILVER_PAYMENTS_DIR = SILVER_DIR / "payments"
SILVER_ORDER_ITEMS_DIR = SILVER_DIR / "order_items"

GOLD_DIR = DATA_DIR / "gold"
GOLD_ORDERS_DIR = GOLD_DIR / "orders"
GOLD_CUSTOMERS_DIR = GOLD_DIR / "customers"
GOLD_PRODUCTS_DIR = GOLD_DIR / "products"
GOLD_PAYMENTS_DIR = GOLD_DIR / "payments"
GOLD_ORDER_ITEMS_DIR = GOLD_DIR / "order_items"

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