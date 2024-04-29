from fastapi import FastAPI
import uvicorn
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, world!"}


@app.get("/a")
async def root1():
    return {"message": "Hello, world!"}


@app.get('/book/{id}')
async def book_data(id: int):
    return {"book": id}


@app.route('/book/issue/{id}')
async def book_issue(id: int):
    return {"book_issue": id}


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
