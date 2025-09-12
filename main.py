import json
from fastapi import FastAPI

app = FastAPI()

def readPuzzles():
    with open('puzzles.json', 'r') as puzzlesJSON:
        puzzles = json.load(puzzlesJSON)
    return puzzles

@app.get("/")
async def main():
    return "Hello!"

@app.get("/v1/puzzles/latest")
async def fetchCurrentPuzzle():
    puzzles = readPuzzles()
    latestPuzzle = next(reversed(puzzles.values()))

    return latestPuzzle


@app.get("/v1/puzzles/")
async def fetchPuzzle(time: str|int):
    # TODO: Implement
    return "im sorry"