import math
import cv2
import numpy as np

def detect_arrow(image_path):
    # Read the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

    # Apply Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Perform edge detection using Canny
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)

        if len(approx) == 7:  # Arrows, depicted as polygons typically have 7 sides
            cv2.drawContours(image, [approx], 0, (0, 255, 0), 3)
            print("Arrow detected!")

            # Calculate bounding box
            x, y, w, h = cv2.boundingRect(approx)
            perceived_width = max(w, h)

            # Find distance (function call)
            distance_cm = distance(perceived_width)
            print(f"Estimated Distance: {distance_cm:.2f} cm")

    # Show the result
    cv2.imshow('Detected Arrow', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def distance(actualwidth_px):
    img_height_px = 720
    img_width_px = 1280
    real_arrow_width_cm = 17.0  # The real width of arrow
    FOV_degree = 55  # Field of View of the camera in degrees

    # Diagonal resolution of the image
    diagonal_reso_px = math.sqrt(img_width_px**2 + img_height_px**2)

    # Focal length in pixels using pinhole camera model
    focal_px = diagonal_reso_px / (2 * math.tan(math.radians(FOV_degree) / 2))

    # Distance estimation formula
    distance_cm = (real_arrow_width_cm * focal_px) / actualwidth_px
    return distance_cm

# Provide the path to your image
image_path = 'arrow.jpg'
detect_arrow(image_path)
