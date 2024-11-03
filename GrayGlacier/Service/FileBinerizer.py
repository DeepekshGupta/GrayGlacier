import cv2
import numpy as np

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

# Example usage
if __name__ == "__main__":
    file_path = r'C:\Projects\GrayGlacier\Experimental\NEED for KNEAD v12.zip'  # Replace with your file path
    output_image_path = 'output_image.png'
    print(file_to_image(file_path, output_image_path))
