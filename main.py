import json
from fastapi import FastAPI, HTTPException
from wordalize import checkSimilarity
from timekeeping import dateFromYMD

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
async def fetchPuzzle(time: str|int):
    try:
        return (await readPuzzles())[dateFromYMD(str(time))]
    except:
        raise HTTPException(status_code=404, detail="Couldn't find puzzle")