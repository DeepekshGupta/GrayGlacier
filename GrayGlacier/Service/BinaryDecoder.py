import cv2
import numpy as np

def image_to_file(image_path, output_file_path):
    # Read the image as a grayscale image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Flatten the image to get the binary data
    binary_data = image.flatten()

    # Write the binary data back to the original file
    with open(output_file_path, 'wb') as f:
        f.write(binary_data)

    return f"File restored as {output_file_path}"

# Example usage
if __name__ == "__main__":
    input_image_path = 'output_image.png'  # The image created from the file
    restored_file_path = 'restored_example.zip'
    print(image_to_file(input_image_path, restored_file_path))
