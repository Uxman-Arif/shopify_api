# Shopify API Wrapper (Mock Demo)

A **FastAPI-based wrapper** simulating Shopify API behavior using a local `db.json` file as a mock database.

> For demonstration only. Replace mock logic with real Shopify API calls when credentials are provided.

---

## Requirements

- **Python 3.10+**
- Install dependencies:
  ```bash
  pip install fastapi uvicorn pydantic

## Run the Project
Clone or download this repository.

Make sure main.py and db.json are in the root folder.

Start the server:

```bash
uvicorn main:app --reload
```

(or choose a custom port: uvicorn main:app --reload --port 8080)

## API Documentation
Once running, the interactive Swagger docs are available at: 👉 http://127.0.0.1:8000/docs