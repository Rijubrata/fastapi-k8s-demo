from fastapi import FastAPI

app = FastAPI(title="FastAPI K8s Demo")


@app.get("/")
def root():
    return {
        "message": "Hello from FastAPI",
        "version": "v2.0.0",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}