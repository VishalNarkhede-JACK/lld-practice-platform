# 🚀 LLD Practice Platform (MVP)

A monolithic backend and minimalist frontend platform designed for candidates to practice Low-Level Design (LLD) and receive immediate, structured feedback from an AI evaluator.

Built as an MVP for the Internship Assignment.

## ✨ Key Features & Engineering Decisions

* **Asynchronous AI Evaluation:** Uses FastAPI's `BackgroundTasks` to process Gemini AI grading on a separate thread, ensuring the main submission request is never blocked.
* **Structured AI Outputs:** Leverages Google's `gemini-3.8-flash` model and the new `google-genai` SDK with strict JSON schema enforcement to ensure deterministic, structured grading (not just raw text).
* **Clean Domain Design (LLD):** Decoupled entities using Pydantic models (`Problem`, `Submission`, `EvaluationResult`) to clearly separate state tracking from the evaluation logic.
* **Minimalist Monolith:** A single FastAPI server that acts as the API and serves a vanilla HTML/JS frontend without the overhead of heavy frameworks like React.

## 🛠 Tech Stack

* **Backend:** Python, FastAPI, Uvicorn, Pydantic
* **AI/LLM:** Google GenAI SDK (`gemini-3.8-flash`)
* **Frontend:** Vanilla HTML5, CSS3, JavaScript (Fetch API)
* **Storage:** In-memory Python dictionaries (MVP scale)

## ⚙️ How to Run Locally

python -m venv venv

# Windows
.\venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

pip install fastapi uvicorn pydantic python-dotenv google-genai