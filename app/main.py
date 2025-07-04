from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

DEEPAI_API_KEY = os.getenv("DEEPAI_API_KEY")

if not DEEPAI_API_KEY:
    raise ValueError("DEEPAI_API_KEY not set in environment variables")


@app.post("/moderate")
async def moderate_image(file: UploadFile = File(...)):
    if not file.filename.lower().endswith((".jpg", ".jpeg", ".png")):
        raise HTTPException(status_code=400, detail="Invalid file format. Only JPG and PNG allowed.")

    try:
        response = requests.post(
            "https://api.deepai.org/api/nsfw-detector",
            files={"image": (file.filename, await file.read())},
            headers={"api-key": DEEPAI_API_KEY}
        )

        print("DEEPAI RESPONSE:", response.status_code, response.text)


        if response.status_code != 200:
            raise HTTPException(status_code=502, detail="Error from DeepAI API")

        result = response.json()
        nsfw_score = result["output"]["nsfw_score"]

        if nsfw_score > 0.7:
            return JSONResponse(status_code=200, content={"status": "REJECTED", "reason": "NSFW content"})

        return {"status": "OK"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
