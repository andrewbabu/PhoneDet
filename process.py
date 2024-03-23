import os
from PIL import Image

# Function to resize and save images
def resize_and_save(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    files = os.listdir(input_folder)

    # Initialize counter for numbered filenames
    counter = 1

    # Iterate over each file in the input folder
    for filename in files:
        # Check if the file is an image
        if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
            # Open image
            image_path = os.path.join(input_folder, filename)
            img = Image.open(image_path)

            # Resize image to 640x640
            img_resized = img.resize((640, 640))

            # Save resized image with numbered filename
            output_path = os.path.join(output_folder, f"img_{counter}.jpg")
            img_resized.save(output_path)

            # Print message indicating which image is processed
            print(f"img_{counter} is processed")

            # Increment counter
            counter += 1

# Input folder containing original images
input_folder = "try"

# Output folder to store resized images
output_folder = "try_save"

# Resize and save images
resize_and_save(input_folder, output_folder)

