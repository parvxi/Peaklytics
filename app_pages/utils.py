import base64
import json
import os

# Helper function to convert a local image to base64
def get_base64_image(image_path):
    # Get the directory of the current file
    current_dir = os.path.dirname(__file__)
    # Create an absolute path for the image
    full_image_path = os.path.join(current_dir, image_path)

    # Open the image and convert it to base64
    with open(full_image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# Helper function to load a Lottie animation
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
