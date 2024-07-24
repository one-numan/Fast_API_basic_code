from fastapi import FastAPI
import uvicorn
app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Hello, world!"}


@app.get('/book/{id}')
async def book_data(id: int):
    return {"book": id}

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
