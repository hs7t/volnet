import json
from fastapi import FastAPI
from wordalize import checkSimilarity

app = FastAPI()

def readPuzzles():
    with open('puzzles.json', 'r') as puzzlesJSON:
        puzzles = json.load(puzzlesJSON)
    return puzzles

def readLatestPuzzle():
    puzzles = readPuzzles()
    latestPuzzle = next(reversed(puzzles.values()))

    return latestPuzzle

@app.get("/")
async def main():
    return "Hello!"

@app.get("/v1/puzzles/latest")
async def returnLatestPuzzle():
    return (await readLatestPuzzle())

@app.get("/v1/similarity/")
async def checkGuessCloseness(guess: str, solution: str|None = None): 
    if solution == None:
        solution = (await readLatestPuzzle())["word"]

    return checkSimilarity(guess, solution)

@app.get("/v1/puzzles/")
async def fetchPuzzle(time: str|int):
    # TODO: Implement
    return "im sorry"