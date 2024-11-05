from fastapi.responses import StreamingResponse
import io


def downloadImage(imageBuffer, filename: str):
      # Create a BytesIO object to hold the image data
    img_byte_arr = io.BytesIO(imageBuffer)

    # Set the filename for the downloaded image
    filename = filename.split(".")[0]
    filename = str(filename) + "_binary_image.png"

    # Return the greyscale image as a streaming response with headers to download
    return StreamingResponse(
        img_byte_arr,
        media_type="image/png",
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )
