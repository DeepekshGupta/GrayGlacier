
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
import cv2
import numpy as np
import io
from Service.downloadImage import downloadImage
from Service.FileBinerizer import file_to_image_API


app = FastAPI()

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    # Read the uploaded file
    contents = await file.read()
    
    # --------------IMAGE PROCESSING-----------------------------------------
    np_array = np.frombuffer(contents, np.uint8)

    # Decode the image
    image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

    # Check if the image was successfully decoded
    if image is None:
        return {"error": "Failed to decode image."}

    # Convert the image to greyscale
    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Encode the greyscale image back to PNG format
    is_success, buffer = cv2.imencode(".png", grey_image)
    if not is_success:
        return {"error": "Image conversion failed."}
# --------------------------DOWNLOAD IMAGE-----------------------------------------------
    return downloadImage(buffer)


@app.post("/binerize/")
async def upload_image(file: UploadFile = File(...)):
    # Read the uploaded file and process it into an image buffer
    buffer = await file_to_image_API(file)

    # Return the greyscale image as a downloadable file without saving it to disk
    return downloadImage(buffer, file.filename)







from fastapi.responses import HTMLResponse


@app.get("/")
async def main():
    content = """
<body>
    <h1>Upload an Image to create a binary</h1>
    <form action="http://localhost:8000/binerize/" method="post" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <input type="submit" value="Upload">
    </form>
</body>
    """
    return HTMLResponse(content=content)

