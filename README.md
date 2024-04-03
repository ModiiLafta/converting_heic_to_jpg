
# converting heic image to jpg


This Python script automates the process of converting HEIC image files to JPEG format. It's designed to efficiently handle multiple HEIC files within a specified directory, converting each to its JPEG equivalent and saving the results in a separate folder.

## Requirements

- Python 3
- ImageMagick
- subprocess module (standard with Python)

## Installation

### Python 3

Ensure Python 3 is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### ImageMagick

ImageMagick is required for the conversion process. It can be installed via Homebrew on macOS:

**For Intel Mac:**

```bash
brew install imagemagick
```


**For Apple Silicon (M1, M2, etc.) Mac:**
```
arch -arm64 brew install imagemagick
```
For other operating systems, please refer to the ImageMagick download page for installation instructions.

**For other operating systems**, please refer to the ImageMagick [download page](https://imagemagick.org/script/download.php) for installation instructions.

## Usage

1. Place your HEIC images in a designated directory.
2. Update the `directory` variable in the script to point to your designated directory.
3. Run the script:

```
python3 convert_heic_to_jpeg.py
```

The script will automatically create a new folder named `jpg` within the specified directory and save the converted JPEG images there.

## Contributing

Feel free to fork this repository and submit pull requests to contribute to this project. If you encounter any issues or have suggestions for improvement, please open an issue in this repository.

