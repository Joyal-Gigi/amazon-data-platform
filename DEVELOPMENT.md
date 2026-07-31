# Development Standards

## Purpose

This document defines the development standards followed in this project to maintain consistency and code quality.

---

# Git Workflow

- Never develop directly on the `main` branch.
- Create a feature branch for every Jira ticket.
- Merge only after code review.

Example:

feature/DE-001-ingestion

---

# Branch Naming

feature/DE-001-description

Examples

feature/DE-002-validation

feature/DE-003-bronze-layer

bugfix/DE-014-null-pointer

hotfix/INC-102-schema-failure

---

# Commit Messages

Use clear, descriptive commit messages.

Good

Initial project setup

Add Bronze layer ingestion

Implement schema validation

Write partitioned Parquet files

Avoid

update

changes

fix

latest

---

# Python Standards

- Follow PEP 8.
- Use descriptive variable names.
- Keep functions focused on one responsibility.
- Add docstrings for reusable functions.
- Avoid hardcoded values.
- Store configuration separately from business logic.

Example

orders_df

customers_df

products_df

Avoid

df1

temp

abc

---

# Project Structure

src/
Contains all application source code.

tests/
Unit and integration tests.

data/raw/
Source data (read-only).

data/bronze/
Raw ingested Parquet data.

data/silver/
Cleaned and transformed data.

data/gold/
Business-ready datasets.

logs/
Application logs.

---

# Pull Request Checklist

Before creating a Pull Request:

- Code runs successfully.
- No unnecessary files committed.
- .venv is ignored.
- Code formatted.
- Requirements updated (if needed).
- README updated (if needed).

---

# Code Reviews

Every Pull Request should answer:

- What was changed?
- Why was it changed?
- How was it tested?

---

# Future Standards

As the project evolves, this document will be updated with:

- Logging standards
- Testing standards
- Airflow conventions
- Performance guidelines
- Data quality standards