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



    
def checkForFillerValues(img):
    row = np.where(img == 255)[0]
    if row.size == 0:
        return False
    else:
        for i in row:
            if np.all(img[i:] == 255):
                print(img[i:])
                return i
            else:
                return -1

         

def writeFile(binary_data, output_file_path):
    # Write the binary data back to the original file
    with open(output_file_path, 'ab') as f:
        f.write(binary_data)

    return f"File restored as {output_file_path}"


def image_to_file_2(image_path, output_file_path):
    # Read the image as a grayscale image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Flatten the image to get the binary data
    binary_data = image.flatten()
    indexOfFillerValues = checkForFillerValues(binary_data)
    print(indexOfFillerValues)
    if indexOfFillerValues == -1:
        print("No Filler Values")
        writeFile(binary_data, output_file_path)
    else:
        print("Filler Values DETECTED!")
        writeFile(binary_data[:indexOfFillerValues], output_file_path)
    return f"File restored as {output_file_path}"




import os
def processFiles(input_image_path, restored_file_path):
    dir_list = os.listdir(r'output')
    dir_list = sorted(dir_list, key=lambda x: int(''.join(filter(str.isdigit, x))))
    print(dir_list)
    for file in dir_list:
        file_path = input_image_path + "\\" + file
        print(file_path)
        image_to_file_2(file_path, restored_file_path)
        # os.remove(file_path)




# Example usage
if __name__ == "__main__": 
    input_image_path = r'output'  # The image created from the file
    restored_file_path = r'restored_example.zip'
    # print(image_to_file_2("output/output_image_493.png", restored_file_path))
    print(processFiles(input_image_path, restored_file_path))

