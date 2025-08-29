from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
async def root():
    msgs = [
        {"reference": "Today, we're teaching poodles how to fly!"},
        {"reference": "Megatron must be stopped — no matter the cost."},
        {"reference": "You're a real blue flame special, aren't ya, son?"}
    ]

    msg = random.choice(msgs)

    return msg
