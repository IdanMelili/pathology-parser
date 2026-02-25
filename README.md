# Pathology Report Parser

A Python NLP pipeline that extracts structured clinical information from unstructured pathology reports.

## Background

Built as direct preparation for an upcoming NLP research internship at the Cedars-Sinai AI Campus, where I'll be working on extracting diagnostic insights from the TCGA pathology report corpus.

## What It Extracts

- Cancer type (adenocarcinoma, squamous cell carcinoma, etc.)
- Primary site (lung, breast, colon, etc.)
- Tumor size (handles cm and mm)
- TNM staging (T, N, M categories with prefix variants: p, c, y, r)
- Surgical margin status

## How It Works

1. `preprocessor.py` — cleans and normalizes raw report text
2. `extractor.py` — regex patterns + keyword matching for each field
3. `pipeline.py` — orchestrates preprocessing and extraction
4. `main.py` — runs all sample reports and prints structured output

## Setup
```bash
git clone <https://github.com/IdanMelili/pathology-parser.git>
cd pathology-parser
python3.13 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```
