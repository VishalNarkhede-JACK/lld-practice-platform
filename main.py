from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict

from models import Problem, Submission, SubmissionStatus
from db import PROBLEMS_DB, SUBMISSIONS_DB, EVALUATIONS_DB
from evaluator import evaluate_submission

app = FastAPI(title="LLD Practice Platform API")

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/problems", response_model=List[Problem])
def get_problems():
    """Returns the list of available LLD problems."""
    return PROBLEMS_DB

@app.get("/problems/{problem_id}", response_model=Problem)
def get_problem(problem_id: str):
    """Gets a specific problem by its ID."""
    for p in PROBLEMS_DB:
        if p.id == problem_id:
            return p
    raise HTTPException(status_code=404, detail="Problem not found")

# --- Async Background Task ---
async def process_evaluation(submission_id: str, problem: Problem, solution_text: str):
    """Background task that runs the AI evaluation."""
    try:
        SUBMISSIONS_DB[submission_id].status = SubmissionStatus.EVALUATING
        
        # Call the Gemini AI
        evaluation_result = await evaluate_submission(problem, solution_text)
        
        # Save the result
        EVALUATIONS_DB[submission_id] = evaluation_result
        SUBMISSIONS_DB[submission_id].status = SubmissionStatus.COMPLETED
        SUBMISSIONS_DB[submission_id].evaluation = evaluation_result
        
    except Exception as e:
        SUBMISSIONS_DB[submission_id].status = SubmissionStatus.FAILED
        SUBMISSIONS_DB[submission_id].error_message = str(e)


@app.post("/submit", response_model=Submission)
def submit_solution(problem_id: str, solution_text: str, background_tasks: BackgroundTasks):
    """
    Accepts a new submission. 
    It saves the submission immediately as PENDING, and triggers the AI evaluation in the background.
    This fulfills the engineering requirement: "do not block the main submission request unnecessarily."
    """
    # Find the problem
    problem = next((p for p in PROBLEMS_DB if p.id == problem_id), None)
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")

    # Create the submission
    new_submission = Submission(
        problem_id=problem_id,
        solution_text=solution_text
    )
    
    # Save to "Database"
    SUBMISSIONS_DB[new_submission.id] = new_submission
    
    # Start the AI grading in the background!
    background_tasks.add_task(process_evaluation, new_submission.id, problem, solution_text)
    
    return new_submission

@app.get("/submissions/{submission_id}", response_model=Submission)
def get_submission_status(submission_id: str):
    """Allows the frontend to check if the AI is done grading."""
    if submission_id not in SUBMISSIONS_DB:
        raise HTTPException(status_code=404, detail="Submission not found")
    return SUBMISSIONS_DB[submission_id]

@app.get("/")
def serve_frontend():
    """Serves the minimalist HTML frontend."""
    return FileResponse("index.html")