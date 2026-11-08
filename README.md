# Mini RAG

This is a minimal implementation of a Retrieval-Augmented Generation (RAG) model for question answering.

## Requirements

- Python 3.11 or later
- [uv](https://docs.astral.sh/uv/)

## Installation

### 1. Install uv

If you haven't installed uv yet, run:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Restart your terminal or reload your shell configuration.

Verify the installation:

```bash
uv --version
```

### 2. Clone the repository

```bash
git clone <repository-url>
cd MINI-RAG-APP
```

### 3. Install Python

Install Python 3.12:

```bash
uv python install 3.12
```

### 4. Create a virtual environment

```bash
uv venv --python 3.12
```

### 5. Activate the environment

**Linux / macOS:**

```bash
source .venv/bin/activate
```

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

### 6. Install dependencies

If the repository contains `pyproject.toml` and `uv.lock`:

```bash
uv sync
```

### 7. Environment Variables

Create your environment file by copying the example:

**Linux / macOS:**

```bash
cp .env.example .env
```

**Windows:**

```powershell
copy .env.example .env
```

Open `.env` and replace the placeholder values with your actual configuration and API keys.

**Important:** Never commit your `.env` file or expose your API keys publicly.


### 8. Run the application

```bash
uv run python main.py
```

## Managing Dependencies

Add a new package:

```bash
uv add package-name
```

Remove a package:

```bash
uv remove package-name
```

Update dependencies:

```bash
uv lock --upgrade
uv sync
```

## run fast api server

```bash
uv run uvicorn main:app --reload --host 0.0.0.0 --port 5000
```


## Project Structure

```text
MINI-RAG-APP/
│
├── .venv/
├── src/
├── pyproject.toml
├── uv.lock
├── .python-version
├── README.md
└── .gitignore
```
