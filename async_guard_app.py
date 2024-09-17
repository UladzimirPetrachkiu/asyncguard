import asyncio
import uvicorn
from asyncio import Lock
from time import monotonic
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel

"""
FastAPI service that provides a single endpoint '/test'.
This endpoint ensures that only one request can execute the async `work` function at a time.
The `work` function simulates some work by sleeping for 3 seconds.
The service returns the actual time spent processing each request.
"""

# Create FastAPI app and APIRouter instance
app = FastAPI()
router = APIRouter()

# Lock to prevent concurrent execution of `work`
work_lock = Lock()

class TestResponse(BaseModel):
    """
    Response model to capture the elapsed time for processing a request.
    """
    elapsed: float

async def work() -> None:
    """
    Simulates an asynchronous task by sleeping for 3 seconds.
    """
    await asyncio.sleep(3)

@router.get("/test", response_model=TestResponse)
async def handler() -> TestResponse:
    """
    Handles GET requests to the `/test` endpoint.
    
    - Ensures that only one request at a time can execute the `work` function.
    - Measures and returns the time taken to process the request.
    
    Returns:
        TestResponse: Object containing the elapsed time for processing the request.
    """
    ts1 = monotonic()
    
    # Only one request can execute the work function at a time
    async with work_lock:
        await work()
    
    ts2 = monotonic()
    
    # Return the elapsed time for this request
    return TestResponse(elapsed=ts2 - ts1)

# Include the router in the FastAPI app
app.include_router(router)

if __name__ == "__main__":
    # Entry point for running the FastAPI app
    uvicorn.run(app, host="0.0.0.0", port=8000)
