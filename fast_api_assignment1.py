"""
FastAPI Assignment 1: REST API Calculator
=========================================
Features:
1. Pydantic Request & Response Models for validation.
2. Multiple endpoint styles:
   - POST /calculate (Request body with JSON)
   - GET /calculate/{operation}/{a}/{b} (Path parameters)
   - GET /add, /subtract, /multiply, /divide (Query parameters)
3. HTTP Status Codes & Error Handling (HTTPException for Division by Zero & Invalid Operations).
4. Auto-generated Interactive Documentation at /docs (Swagger UI) and /redoc.

How to run:
    uvicorn fast_api_assignment1:app --reload
"""

from enum import Enum
from typing import Optional
from fastapi import FastAPI, HTTPException, Query, Path
from pydantic import BaseModel, Field

# Initialize FastAPI App with metadata for Swagger UI
app = FastAPI(
    title="FastAPI Calculator REST API - Assignment 1",
    description="A comprehensive REST API Calculator supporting arithmetic operations via JSON body, Path parameters, and Query parameters.",
    version="1.0.0"
)


# --- 1. Enumerations & Pydantic Models ---

class OperationType(str, Enum):
    ADD = "add"
    SUBTRACT = "subtract"
    MULTIPLY = "multiply"
    DIVIDE = "divide"
    POWER = "power"
    MODULUS = "modulus"


class CalculationRequest(BaseModel):
    num1: float = Field(..., description="First number", example=20.5)
    num2: float = Field(..., description="Second number", example=5.0)
    operation: OperationType = Field(..., description="Arithmetic operation to perform", example=OperationType.ADD)


class CalculationResponse(BaseModel):
    status: str = "success"
    operation: str
    num1: float
    num2: float
    result: float
    message: Optional[str] = None


# --- Helper Function for Core Calculation Logic ---

def perform_calculation(a: float, b: float, operation: str) -> float:
    op = operation.lower()
    if op in ["add", "addition", "+"]:
        return a + b
    elif op in ["subtract", "subtraction", "-"]:
        return a - b
    elif op in ["multiply", "multiplication", "*"]:
        return a * b
    elif op in ["divide", "division", "/"]:
        if b == 0:
            raise HTTPException(
                status_code=400,
                detail="Division by zero is not allowed."
            )
        return a / b
    elif op in ["power", "pow", "^", "**"]:
        return a ** b
    elif op in ["modulus", "mod", "%"]:
        if b == 0:
            raise HTTPException(
                status_code=400,
                detail="Modulus by zero is not allowed."
            )
        return a % b
    else:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported operation '{operation}'. Supported operations: add, subtract, multiply, divide, power, modulus."
        )


# --- 2. REST API Endpoints ---

@app.get("/", tags=["General"])
async def root():
    """
    Root Welcome Endpoint.
    """
    return {
        "message": "Welcome to the FastAPI Calculator REST API (Assignment 1)!",
        "documentation": "Visit /docs for the interactive Swagger UI or /redoc for ReDoc.",
        "endpoints": [
            "POST /calculate",
            "GET /calculate/{operation}/{a}/{b}",
            "GET /add?a={num}&b={num}",
            "GET /subtract?a={num}&b={num}",
            "GET /multiply?a={num}&b={num}",
            "GET /divide?a={num}&b={num}"
        ]
    }


# Endpoint 1: POST Request with JSON Body (Pydantic Model)
@app.post(
    "/calculate",
    response_model=CalculationResponse,
    tags=["Calculator Operations"],
    summary="Universal Calculation via JSON Body"
)
async def calculate_post(request: CalculationRequest):
    """
    Calculates result based on JSON request body:
    - **num1**: First numeric value
    - **num2**: Second numeric value
    - **operation**: One of `add`, `subtract`, `multiply`, `divide`, `power`, `modulus`
    """
    res = perform_calculation(request.num1, request.num2, request.operation.value)
    return CalculationResponse(
        status="success",
        operation=request.operation.value,
        num1=request.num1,
        num2=request.num2,
        result=res
    )


# Endpoint 2: GET Request using Path Parameters
@app.get(
    "/calculate/{operation}/{a}/{b}",
    response_model=CalculationResponse,
    tags=["Path Parameter Endpoints"],
    summary="Calculate using URL Path Parameters"
)
async def calculate_path(
    operation: OperationType = Path(..., description="Operation: add, subtract, multiply, divide, power, modulus"),
    a: float = Path(..., description="First number"),
    b: float = Path(..., description="Second number")
):
    """
    Example: `/calculate/multiply/6/7` returns `42.0`
    """
    res = perform_calculation(a, b, operation.value)
    return CalculationResponse(
        status="success",
        operation=operation.value,
        num1=a,
        num2=b,
        result=res
    )


# Endpoint 3: Direct GET Endpoints using Query Parameters
@app.get("/add", response_model=CalculationResponse, tags=["Query Parameter Endpoints"])
async def add_query(
    a: float = Query(..., description="First number"),
    b: float = Query(..., description="Second number")
):
    """Add two numbers: `GET /add?a=10&b=20`"""
    return CalculationResponse(status="success", operation="add", num1=a, num2=b, result=a + b)


@app.get("/subtract", response_model=CalculationResponse, tags=["Query Parameter Endpoints"])
async def subtract_query(
    a: float = Query(..., description="First number"),
    b: float = Query(..., description="Second number")
):
    """Subtract two numbers: `GET /subtract?a=30&b=10`"""
    return CalculationResponse(status="success", operation="subtract", num1=a, num2=b, result=a - b)


@app.get("/multiply", response_model=CalculationResponse, tags=["Query Parameter Endpoints"])
async def multiply_query(
    a: float = Query(..., description="First number"),
    b: float = Query(..., description="Second number")
):
    """Multiply two numbers: `GET /multiply?a=6&b=7`"""
    return CalculationResponse(status="success", operation="multiply", num1=a, num2=b, result=a * b)


@app.get("/divide", response_model=CalculationResponse, tags=["Query Parameter Endpoints"])
async def divide_query(
    a: float = Query(..., description="First number"),
    b: float = Query(..., description="Second number")
):
    """Divide two numbers: `GET /divide?a=100&b=4`"""
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
    return CalculationResponse(status="success", operation="divide", num1=a, num2=b, result=a / b)
