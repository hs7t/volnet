from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def main():
    return "Hello!"

@app.get("/v1/puzzles/latest")
async def fetchCurrentPuzzle():
    return {
        "snippets": [
            {
                "content": 'I bet on {losing} dogs',
                "source": '"Puberty"',
                "by": 'Mitski',
                "date": '2016',
            },
            {
                "content": "I'm {losing} my temper",
                "source": 'Trust me bro',
                "by": 'Me',
                "date": '2025',
            },
        ],
        "solution": 'losing',
    }


@app.get("/v1/puzzles/")
async def fetchPuzzle(time: str|int):
    return {
        "snippets": [
            {
                "content": 'I bet on {losing} dogs',
                "source": '"Puberty"',
                "by": 'Mitski',
                "date": '2016',
            },
            {
                "content": "I'm {losing} my temper",
                "source": 'Trust me bro',
                "by": 'Me',
                "date": '2025',
            },
        ],
        "solution": 'losing',
    }
