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
    width = int(np.ceil(total_bytes ** 0.5))
    height = int(np.ceil(total_bytes / width))

    # Create a new array with the calculated dimensions and fill it
    padded_array = np.zeros((height, width), dtype=np.uint8)
    padded_array.flat[:total_bytes] = byte_array

    # Convert the NumPy array into an image (you can apply other image transformations here if needed)
    _, img_encoded = cv2.imencode('.png', padded_array)

    # Convert the encoded image back to bytes and return it
    # img_byte_arr = io.BytesIO(img_encoded)

    return img_encoded



def file_to_image_1(file_path, output_image_path):
    # Read the binary data from the file
    with open(file_path, 'rb') as f:
        file_data = f.read()

    # Convert the binary data to a NumPy array
    byte_array = np.frombuffer(file_data, dtype=np.uint8)
    size = 720
    # Calculate dimensions for the image
    total_bytes = len(byte_array)
    sq_size = (size**2)
    print("units: ", total_bytes/sq_size)
    print("int units: ", int(np.ceil(total_bytes/sq_size)))
    n = int(np.ceil(total_bytes/sq_size))
    print("int units: ", n)
    k = total_bytes
    print("sq_size: ", sq_size)
    print("total allocated size: ", sq_size*n)
    print("total required size: ", total_bytes)
    print("total remaining size: ", sq_size*n - total_bytes)

    # print(sq_size*n-1)
    # print(sq_size*494.01236304012343)
    # print(sq_size*495)
    # print(sq_size*495 - sq_size*494.01236304012343)

    for i in range(n):
        # print(str(total_bytes) + " - " + str(sq_size) + " x " + str(i) +" = " + str(total_bytes - sq_size*i))
        
        # Create a new array with the calculated dimensions and fill it
        padded_array = np.zeros((size, size), dtype=np.uint8)
        print("--------------------------------")
        print(len(padded_array.flat))
        print(str(len(byte_array[sq_size*i:])) + " < " + str(len(padded_array.flat)))
        print(sq_size*i)
        print(sq_size*(i+1))
        print(len(padded_array.flat[sq_size*i:sq_size*(i+1)]))
        if len(byte_array[sq_size*i:]) < len(padded_array.flat):
            print(True)
            print(padded_array.size)
            print(byte_array.size)
            print( padded_array.size - byte_array.size)
            byte_array = np.pad(byte_array, (0, padded_array.size - byte_array[sq_size*i:sq_size*(i+1)].size), mode="constant", constant_values=255)
            print(byte_array)
            # return True
        padded_array.flat = byte_array[sq_size*i:sq_size*(i+1)]
        # print(i)
        # print(sq_size*i)
        # print(sq_size*(i+1))

        # print(byte_array[sq_size*i:sq_size*(i+1)])
        # print(padded_array)
        # Save the image
        cv2.imwrite(output_image_path + "_" + str(i) + ".png", padded_array)


    


    # width = int(np.ceil(total_bytes ** 0.5))
    # height = int(np.ceil(total_bytes / width))

    # # Create a new array with the calculated dimensions and fill it
    # padded_array = np.zeros((height, width), dtype=np.uint8)
    # padded_array.flat[:total_bytes] = byte_array

    # # Save the image
    # cv2.imwrite(output_image_path, padded_array)
    return f"Image saved as {output_image_path}"



# Example usage
if __name__ == "__main__":
    file_path = r'GrayGlacier\Service\example.txt'  # Replace with your file path
    output_image_path = r'output\output_image'
    print(file_to_image_1(file_path, output_image_path))

