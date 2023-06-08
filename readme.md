# Apache Beam Pipeline

This is an Apache Beam pipeline that processes transactions data to filter and summarize transactions based on specific criteria.

## Overview

The Apache Beam pipeline reads transaction data from a CSV file, applies filters and transformations, and writes the processed data to a JSONL file. The pipeline uses Apache Beam's data processing capabilities and can be run on various execution engines, such as Apache Flink, Apache Spark, or Google Cloud Dataflow.

The pipeline performs the following steps:

1. Reads the transaction data from a CSV file.
2. Filters and maps the transactions to key-value pairs based on certain criteria.
3. Combines the transactions by date and calculates the sum of transaction amounts.
4. Formats the output as JSON objects.
5. Writes the JSON objects to a compressed JSONL (JSON Lines) file.

## Prerequisites

To run the pipeline, you need the following:

- Python 3.7 or above
- Apache Beam (Python SDK)
- Apache Beam dependencies (e.g., `apache-beam[gcp]` for running on Google Cloud Dataflow)
- Apache Beam runners compatible with your execution environment (e.g., Apache Flink, Apache Spark, or Google Cloud Dataflow)

## Getting Started

1. Clone this repository:

   ```bash
   git clone <repository_url>

1. Run the pipeline using the run.bat script:

   ```bash
   .\run.bat
