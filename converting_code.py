import subprocess
import os

def convert_heic_to_jpeg(heic_path, jpeg_path):
    subprocess.run(["magick", heic_path, jpeg_path])

# Directory containing the HEIC files
directory = '/Users/modilafta/Documents/python_test/'

# New folder for the JPEG files
jpeg_directory = os.path.join(directory, "jpg")

# Create the "jpg" directory if it doesn't exist
if not os.path.exists(jpeg_directory):
    os.makedirs(jpeg_directory)

# List all HEIC files in the directory
heic_files = [file for file in os.listdir(directory) if file.endswith('.heic')]

# Loop through the HEIC files and convert each to JPEG
for heic_file in heic_files:
    # Construct HEIC file path
    heic_path = os.path.join(directory, heic_file)
    # Construct JPEG file path in the new "jpg" directory
    jpeg_path = os.path.join(jpeg_directory, os.path.splitext(heic_file)[0] + '.jpg')
    
    # Convert the file
    convert_heic_to_jpeg(heic_path, jpeg_path)
    print(f"Converted '{heic_path}' to '{jpeg_path}'")
