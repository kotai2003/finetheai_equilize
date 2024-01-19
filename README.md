# Image Histogram Equalization Project

## Overview
This project includes a Python script that searches for image files within a specified directory, applies histogram equalization to enhance their contrast, and saves the modified images in a new subdirectory. It automates image processing tasks and helps in improving the contrast of images.

## Setup
Before running this script, ensure that you have a Python environment set up and the required libraries installed.

To install the necessary library, run the following command:


## Usage
1. Download the script.
2. Set the `test_dir` variable in the `list_full_paths_in_subfolders` function to the path of your target directory.
3. Execute the script.

Upon execution, the script will search for all image files in the specified directory, equalize their histograms, and save them in a subfolder named `equilized_hist`.

## Code Explanation
- The `list_full_paths_in_subfolders` function searches for the paths of image files within the specified directory and returns a list of these paths.
- The script loads each image file in grayscale and uses the `cv2.equalizeHist` function to equalize its histogram.
- The equalized images are saved in a new subfolder named `equilized_hist`, located in the same directory as the original images.

## License
[MIT License](LICENSE)

## Contributing
If you are interested in contributing to this project, please submit a pull request or report any issues.


