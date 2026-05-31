from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Phase 0 setup successful"}