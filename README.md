# CloudAlchemy

CloudAlchemy is a robust solution designed to query Parquet files stored in Google Cloud Storage using DuckDB, served via a FastAPI backend. The application is deployed on Cloud Run, with a Node.js frontend hosted on App Engine for user interaction.

![CloudAlchemy](assets/cloudalchemy.webp)

## Architecture

- **Backend**: Python, FastAPI, DuckDB, Google Cloud Storage
- **Frontend**: Node.js, Express, HTML, JavaScript
- **Deployment**: Cloud Run (Backend), App Engine (Frontend)

## Features

- Query Parquet files stored in Google Cloud Storage.
- FastAPI backend for handling query requests.
- Node.js frontend for user interaction and query submission.
- Deployed on Google Cloud Platform for scalability and reliability.

## Prerequisites

- Google Cloud SDK
- Docker
- Node.js
- Python 3.10
