import cv2
import numpy as np
import io
from fastapi import UploadFile


def file_to_image(file_path, output_image_path):
    # Read the binary data from the file
    with open(file_path, 'rb') as f:
        file_data = f.read()

    # Convert the binary data to a NumPy array
    byte_array = np.frombuffer(file_data, dtype=np.uint8)

    # Calculate dimensions for the image
    total_bytes = len(byte_array)
    width = int(np.ceil(total_bytes ** 0.5))
    height = int(np.ceil(total_bytes / width))

    # Create a new array with the calculated dimensions and fill it
    padded_array = np.zeros((height, width), dtype=np.uint8)
    padded_array.flat[:total_bytes] = byte_array

    # Save the image
    cv2.imwrite(output_image_path, padded_array)
    return f"Image saved as {output_image_path}"



async def file_to_image_API(uploaded_file: UploadFile):
    # Read the binary data from the uploaded file
    file_data = await uploaded_file.read()

    # Convert the binary data to a NumPy array
    byte_array = np.frombuffer(file_data, dtype=np.uint8)

    # Calculate dimensions for the image
    total_bytes = len(byte_array)
    print("total_bytes: " + str(total_bytes))
    width = int(np.ceil(total_bytes ** 0.5))
    height = int(np.ceil(total_bytes / width))
    print("width: " + str(width))
    print("height: " + str(height))

    # Create a new array with the calculated dimensions and fill it
    padded_array = np.zeros((height, width), dtype=np.uint8)
    padded_array.flat[:total_bytes] = byte_array

    # Convert the NumPy array into an image (you can apply other image transformations here if needed)
    _, img_encoded = cv2.imencode('.png', padded_array)

    # Convert the encoded image back to bytes and return it
    # img_byte_arr = io.BytesIO(img_encoded)

    return img_encoded



# Example usage
# if __name__ == "__main__":
#     file_path = r'example.txt'  # Replace with your file path
#     output_image_path = 'output_image.png'
#     print(file_to_image(file_path, output_image_path))
