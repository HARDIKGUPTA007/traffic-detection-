# Traffic Signal Detection Using OpenCV

## Overview

This project focuses on detecting traffic signals (red, yellow, and green) using computer vision techniques implemented in Python with the OpenCV library. It uses real-time video input or static images to identify the state of traffic lights and provide corresponding feedback.

## Features

- **Real-Time Detection**: Analyze video feeds to detect and classify traffic lights.
- **Signal Color Identification**: Accurately distinguish between red, yellow, and green signals.
- **Contour Detection**: Identify signal boundaries using contour detection and color thresholding.
- **Versatile Input**: Supports both live camera feeds and image files for detection.

## How It Works

1. **Preprocessing**:
   - Convert the image to grayscale to simplify the analysis.
   - Apply Gaussian blur to reduce noise.
   - Use Canny edge detection to highlight object boundaries.
2. **Contour Analysis**:
   - Find and filter contours to locate potential traffic light signals.
   - Draw bounding boxes around detected signals.
3. **Color Analysis**:
   - Use predefined color thresholds to analyze the region of interest (ROI) for red, yellow, or green dominance.
   - Classify the traffic light based on the dominant color.
4. **Output**:
   - Display the detected traffic signal's color in real time or through image processing.

## Prerequisites

- Python 3.x
- OpenCV (`cv2`)
- NumPy

Install the dependencies:
```bash
pip install opencv-python numpy
```

## Usage

### 1. Real-Time Detection via Webcam
Run the script to analyze live video feed from your camera:
```bash
python traffic_signal_detection.py
```
Press `q` to quit the live feed.

### 2. Static Image Detection
Uncomment the section in the script to test with a static image:
```python
image_path = 'path_to_image.png'
image = cv2.imread(image_path)
result = detect_traffic_signals(image)
print(result)
```

### Output Example
The program will output:
- `The light is red` if a red signal is detected.
- `The light is yellow` if a yellow signal is detected.
- `The light is green` if a green signal is detected.
- `No traffic signal detected` if no signal is found.

## Customization

- **Thresholds**: Modify the `red_lower`, `red_upper`, `green_lower`, etc., in the `get_signal_color` function to fine-tune detection.
- **Contour Filtering**: Adjust the `area > 1000` condition to change the sensitivity of the contour detection.
- **Resolution**: Use `cv2.resize` to adjust the input resolution for better performance on different hardware.

## Challenges and Improvements

### Current Limitations:
- May struggle in low-light or noisy environments.
- Requires proper tuning for thresholds based on the environment.

### Potential Improvements:
1. **Enhanced ROI Detection**: Incorporate advanced techniques like Haar cascades or deep learning models for precise detection.
2. **Night Mode**: Implement adaptive thresholding for nighttime or poorly lit scenes.
3. **Multi-Signal Detection**: Extend the script to detect multiple traffic lights in a single frame.

## Acknowledgments

- OpenCV for its powerful computer vision capabilities.
- Numpy for array operations and image manipulation.

## License

This project is open-sourced under the MIT License.
