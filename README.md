# URL Shortener Backend

A minimalistic URL shortener API built with **FastAPI** and in-memory storage.

---

## Requirements

- **Python**: `3.15.0` (or `>= 3.10`)
- **Docker**: `29.8.2` (optional for local deployment)

---

## Quick Start (Local Setup)

### 1. Create and Activate Virtual Environment

**On Windows (PowerShell):**
> *Note: If you encounter an execution policy error, run `Set-ExecutionPolicy Unrestricted -Scope Process` first.*

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

---

### 2. Install Dependencies

Install the project in editable mode using `pyproject.toml`:

```bash
pip install -e .
```

---

### 3. Run the Backend

Start the development server with auto-reload:

```bash
uvicorn main:app --reload
```

---

## Interactive API Documentation (Swagger)

Once the server is running, open your browser and navigate to:

👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**