# GDPR Privacy Policy Engine

A lightweight **Privacy‑by‑Design** enforcement engine built with **FastAPI** and **Pydantic**. It validates incoming JSON data against a configurable GDPR policy (required fields, prohibited fields, retention period) and returns a compliance decision.

## Features

- Define policies declaratively using Pydantic models.
- Automatic validation of required and prohibited fields.
- Retention‑time checks based on ISO‑8601 timestamps.
- Simple HTTP API (`POST /enforce`).
- Unit tests with `pytest` and FastAPI's `TestClient`.

## Quick Start

```bash
# Clone the repo
git clone https://github.com/yourusername/gdpr-privacy-policy-engine.git
cd gdpr-privacy-policy-engine

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the API
uvicorn src.api:app --reload
```

The service will be available at `http://127.0.0.1:8000`. Open `http://127.0.0.1:8000/docs` for the interactive Swagger UI.

## Example Request

```json
POST /enforce
Content-Type: application/json

{
  "data": {
    "user_id": "12345",
    "email": "user@example.com",
    "timestamp": "2024-09-01T12:34:56"
  },
  "policy": {
    "name": "basic-gdpr",
    "required_fields": ["user_id", "email", "timestamp"],
    "prohibited_fields": ["ssn"],
    "retention_days": 365
  }
}
```

Response:

```json
{
  "compliant": true
}
```

## Running Tests

```bash
pytest
```

## License

MIT License
