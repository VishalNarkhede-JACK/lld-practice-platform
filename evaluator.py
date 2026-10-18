import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from models import EvaluationResult, Problem

# Load environment variables
load_dotenv()

# Initialize the new Google GenAI async client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

async def evaluate_submission(problem: Problem, solution_text: str) -> EvaluationResult:
    """
    Evaluates an LLD submission against the problem requirements using Gemini.
    Forces the LLM to return a strict JSON output matching our EvaluationResult model.
    """
    
    # We provide a very strict prompt so the AI acts like a grader, not a chatbot
    system_instruction = (
        "You are an expert Software Architect interviewing a candidate for a backend engineering role. "
        "Your task is to evaluate their Low-Level Design (LLD) submission. "
        "Focus on class responsibilities, domain boundaries, encapsulation, and extensibility. "
        "Do not write code for them. Point out flaws and give actionable architectural suggestions."
    )
    
    prompt = f"""
    Problem Title: {problem.title}
    Problem Description: {problem.description}
    Requirements: {", ".join(problem.requirements)}
    
    Candidate's LLD Submission:
    {solution_text}
    """
    
    try:
        # Call the async client, forcing the output to strictly match our Pydantic model
        response = await client.aio.models.generate_content(
            model='gemini-3.8-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.2, # Low temperature for more analytical grading
                response_mime_type="application/json",
                response_schema=EvaluationResult,
            )
        )
        
        # The SDK automatically handles the JSON string response, but Pydantic parses it safely
        return EvaluationResult.model_validate_json(response.text)
        
    except Exception as e:
        print(f"Error during AI evaluation: {e}")
        # In a real system, you'd log this and maybe retry, but for the MVP we will handle it in the router
        raise