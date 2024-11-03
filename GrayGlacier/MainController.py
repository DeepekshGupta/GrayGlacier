
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
import cv2
import numpy as np
import io
from Service.utilities.downloadImage import downloadImage



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

    # # Create a BytesIO object to hold the image data
    # img_byte_arr = io.BytesIO(buffer)

    # # Set the filename for the downloaded image
    # filename = "greyscale_image.png"

    # # Return the greyscale image as a streaming response with headers to download
    # return StreamingResponse(
    #     img_byte_arr,
    #     media_type="image/png",
    #     headers={"Content-Disposition": f"attachment; filename={filename}"}
    # )




from fastapi.responses import HTMLResponse


@app.get("/")
async def main():
    content = """
<body>
    <h1>Upload an Image</h1>
    <form action="http://localhost:8000/upload/" method="post" enctype="multipart/form-data">
        <input type="file" name="file" accept="image/*" required>
        <input type="submit" value="Upload">
    </form>
</body>
    """
    return HTMLResponse(content=content)

