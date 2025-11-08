from fastapi import FastAPI
from fastapi.responses import Response
import httpx

app = FastAPI()

@app.get("/api")
async def proxy(url: str):
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
    headers = dict(r.headers)
    headers["Access-Control-Allow-Origin"] = "*"
    return Response(
        content=r.content,
        headers=headers,
        media_type=r.headers.get("content-type")
    )
