from fastapi import FastAPI
import uvicorn


app = FastAPI()

## @ means python decorator add some additional functionalities to existing functionalities
@app.get("/hello")
def read_root():
    return {"message": "Hello from Jupyter"}

## Add this at the bottom
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)


