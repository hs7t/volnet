import json

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from wordalize import checkSimilarity

app = FastAPI()

async def readPuzzles():
    with open('puzzles.json', 'r') as puzzlesJSON:
        puzzles = json.load(puzzlesJSON)
    return puzzles

async def readLatestPuzzle():
    puzzles = await readPuzzles()
    latestPuzzle = next(reversed(puzzles.values()))

    return latestPuzzle

@app.get("/")
async def main():
    return "Hello!"

@app.get("/v1/puzzles/latest")
async def returnLatestPuzzle():
    return await readLatestPuzzle()

@app.get("/v1/similarity/{guess}")
async def checkGuessCloseness(guess: str, solution: str|None = None):
    if solution == None:
        solution = (await readLatestPuzzle())["word"]

    return checkSimilarity(guess, solution)

@app.get("/v1/puzzles/{time}")
async def fetchPuzzle(time: str):
    try:
        return (await readPuzzles())[time]
    except:
        raise HTTPException(status_code=404, detail="Couldn't find puzzle")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://volumes.hvii.cc",
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
