from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum
import uuid

# 1. State machine for submissions
class SubmissionStatus(str, Enum):
    PENDING = "PENDING"
    EVALUATING = "EVALUATING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

# 2. Problem representation
class Problem(BaseModel):
    id: str
    title: str
    description: str
    requirements: List[str]

# 3. Rubric Criterion evaluated by AI
class RubricCriterion(BaseModel):
    criterion: str          # e.g., "Class Responsibilities", "Coupling & Cohesion"
    score: int              # Score out of 5
    evidence: str           # What the learner wrote that justifies this score
    concern: str            # What is weak or missing
    suggestion: str         # Concrete step to fix it

# 4. Complete Evaluation output
class EvaluationResult(BaseModel):
    overall_score: int
    rubric_breakdown: List[RubricCriterion]
    key_strengths: List[str]
    areas_for_improvement: List[str]

# 5. Submission entity tracking state and history
class Submission(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    problem_id: str
    solution_text: str
    status: SubmissionStatus = SubmissionStatus.PENDING
    evaluation: Optional[EvaluationResult] = None
    error_message: Optional[str] = None