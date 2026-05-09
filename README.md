# Vitae

Resume-as-a-Service REST API built on the JSON Resume standard.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Run

```bash
uvicorn app.main:app --reload
```

API docs: http://localhost:8000/docs
