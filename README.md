# Shopify API Wrapper (Demo with Mock JSON)

This project is a **FastAPI-based wrapper** that simulates Shopify API behavior using a local `db.json` file as a mock database.
It is intended for **demonstration only**. Once Shopify credentials are provided, the mock logic will be replaced with real Shopify API calls.

---

## ⚙️ Requirements

* **Python:** 3.10 or higher
* **Packages:**

  ```bash
  pip install fastapi uvicorn pydantic
  ```

---

## 🚀 Run the Project

1. Clone or download this repository.
2. Make sure `main.py` and `db.json` are in the root folder.
3. Start the server:

   ```bash
   uvicorn main:app --reload
   ```

   (or choose a custom port: `uvicorn main:app --reload --port 8080`)

---

## 📌 API Documentation

Once running, the interactive Swagger docs are available at:
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
