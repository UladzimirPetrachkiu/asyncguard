# AsyncGuard

**AsyncGuard** is a FastAPI-based service designed to handle asynchronous tasks with concurrency control. The application ensures that only one instance of the `work` function (which simulates a 3-second task) is executed at a time, using an asyncio lock mechanism. This is ideal for scenarios where you need to process one request at a time, avoiding concurrent execution.

## Features

- FastAPI framework for fast and scalable APIs.
- Asyncio-based task management.
- Concurrency control using asyncio locks.
- Simple and efficient design.
- Dockerized for easy deployment.

## How It Works

AsyncGuard exposes a single endpoint:

- `GET /test`: Triggers an asynchronous task (`work`) that "sleeps" for 3 seconds. The service ensures that multiple concurrent requests are handled sequentially, meaning only one task can be running at any given time. It returns the actual time taken to process the request.

Each request is guaranteed to run with at least a 3-second gap between requests due to the locking mechanism.

### Example Response

```json
{
  "elapsed": 3.0012345
}
```

This response contains the actual time elapsed to process the request, which should always be around 3 seconds.

## Requirements

To run this application, you need to have the following installed:

- Python 3.9 or later
- Docker (optional, if you want to run it in a container)

## Installation and Setup

### 1. Cloning the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/UladzimirPetrachkiu/asyncguard.git
cd asyncguard
```

### 2. Install Dependencies

If you're running the application locally, you'll need to install the necessary Python packages. You can do this by running:

```bash
pip install -r requirements.txt
```

### 3. Running the Application

#### Locally

Run the FastAPI server using Uvicorn:

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

By default, the application will be available at `http://localhost:8000`. You can access the `/test` endpoint by visiting `http://localhost:8000/test` in your browser or using a tool like `curl` or `Postman`.

#### Using Docker

If you prefer to run the application in a Docker container:

1. Build the Docker image:

    ```bash
    docker build -t asyncguard .
    ```

2. Run the container:

    ```bash
    docker run -p 8000:8000 asyncguard
    ```

The service will now be available at `http://localhost:8000/test`.

### 4. Testing the Application

You can test the functionality by making concurrent requests. Here's an example using `curl`:

```bash
curl http://localhost:8000/test
```

Run multiple requests in parallel and observe the `elapsed` time in the response. You should see a minimum of 3 seconds between each response, proving that concurrency is being controlled effectively.

## Project Structure

```
.
├── app.py              # Main FastAPI application file
├── Dockerfile          # Dockerfile for containerization
├── requirements.txt    # Python dependencies
├── .dockerignore       # Ignore unnecessary files for Docker
├── .gitignore          # Ignore unnecessary files for Git
├── LICENSE.md          # License file
└── README.md           # This file
```

## FAQ

### Why is there a lock in the code?

The `asyncio.Lock()` ensures that only one request can execute the `work()` function at a time. Without the lock, multiple concurrent requests would run simultaneously, defeating the purpose of this application. The lock ensures that requests are processed sequentially.

### What is the purpose of the `elapsed` time in the response?

The `elapsed` time shows how long it took to process the request. Since the `work()` function takes 3 seconds to complete, the elapsed time will always be close to 3 seconds. The purpose is to demonstrate that tasks are being executed one at a time, with a minimum delay of 3 seconds between tasks.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/UladzimirPetrachkiu/asyncguard/issues) if you have any suggestions.

## License

This project is licensed under the MIT License.
