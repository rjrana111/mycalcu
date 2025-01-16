from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

fastapi_server = FastAPI()

static_folder_path = Path(__file__).parent / "static"
fastapi_server.mount("/static", StaticFiles(directory=static_folder_path), name="static")

@fastapi_server.get("/", response_class=HTMLResponse)
async def root():
    html_path = static_folder_path / "index.html"
    return HTMLResponse(content=html_path.read_text(), status_code=200)

@fastapi_server.get("/calculate")
async def calculate(operation: str, num1: float, num2: float):
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero")
        result = num1 / num2
    else:
        raise HTTPException(status_code=400, detail="Invalid operation")
    
    return {"operation": operation, "num1": num1, "num2": num2, "result": result}
