from fastapi import FastAPI

app = FastAPI(
    title="Vitae",
    description="Resume-as-a-Service REST API built on the JSON Resume standard",
    version="0.1.0",
)


@app.get("/health")
async def health():
    return {"status": "ok"}
