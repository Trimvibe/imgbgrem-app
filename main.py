from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
import uvicorn
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "API is running"}

@app.post("/remove-background")
async def remove_background(file: UploadFile = File(...)):
    from rembg import remove   
    input_bytes = await file.read()
    output_bytes = remove(input_bytes)
    return Response(content=output_bytes, media_type="image/png")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)