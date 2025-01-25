import cv2
import numpy as np

def detect_traffic_signals(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply Canny edge detection
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours in the image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through the contours
    for contour in contours:
        # Calculate the contour area
        area = cv2.contourArea(contour)

        # Filter out small contours
        if area > 1000:
            # Get the bounding rectangle of the contour
            x, y, w, h = cv2.boundingRect(contour)

            # Draw a rectangle around the contour
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Check the color of the detected signal
            signal_color = get_signal_color(image, x, y, w, h)
            if signal_color == 'red':
                return 'The light is red'
            elif signal_color == 'yellow':
                return 'The light is yellow'
            elif signal_color == 'green':
                return 'The light is green'

    return 'No traffic signal detected'

def get_signal_color(image, x, y, w, h):
    # Extract the region of interest (ROI) containing the signal
    roi = image[y:y+h, x:x+w]

    # Perform color analysis on the ROI to determine the signal color
    # Use color thresholding to identify the dominant color

    # Define color thresholds for red, green, and yellow
    red_lower = np.array([0, 0, 100], dtype=np.uint8)
    red_upper = np.array([80, 80, 255], dtype=np.uint8)
    green_lower = np.array([0, 100, 0], dtype=np.uint8)
    green_upper = np.array([80, 255, 80], dtype=np.uint8)
    yellow_lower = np.array([0, 100, 100], dtype=np.uint8)
    yellow_upper = np.array([80, 255, 255], dtype=np.uint8)

    # Apply color thresholds to the ROI
    red_mask = cv2.inRange(roi, red_lower, red_upper)
    green_mask = cv2.inRange(roi, green_lower, green_upper)
    yellow_mask = cv2.inRange(roi, yellow_lower, yellow_upper)

    # Count the number of pixels in each color range
    red_pixels = cv2.countNonZero(red_mask)
    green_pixels = cv2.countNonZero(green_mask)
    yellow_pixels = cv2.countNonZero(yellow_mask)

    # Determine the dominant color based on the number of pixels
    if red_pixels > green_pixels and red_pixels > yellow_pixels:
        return 'red'
    elif green_pixels > red_pixels and green_pixels > yellow_pixels:
        return 'green'
    else:
        return 'yellow'

# # Test with custom image
# image_path = 'redlight.png'
# image = cv2.imread(image_path)
# result = detect_traffic_signals(image)
# print(result)



# Test with camera input
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    result = detect_traffic_signals(frame)
    print(result)
    cv2.imshow('Result', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



