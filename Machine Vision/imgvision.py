import cv2
import numpy as np

def detect_objects(image_path):
  # Load the image
  img = cv2.imread(image_path)

  # Preprocess the image (optional)
  # Convert to grayscale, apply blur, etc.
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  blurred = cv2.GaussianBlur(gray, (5, 5), 0)

  # Object detection method (choose one)
  # Option 1: Blob detection
  params = cv2.SimpleBlobDetector_Params()
  # Adjust parameters for desired blob size, color, etc.
  detector = cv2.SimpleBlobDetector_create(params)
  keypoints = detector.detect(blurred)
  img_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

  # Option 2: Contour detection
  # Find contours, filter based on area, shape, etc.

  # Option 3: Machine learning-based object detection
  # Load a pre-trained model (e.g., YOLO, SSD) and use it for detection

  # Display the image with detected objects
  cv2.imshow("Detected Objects", img_with_keypoints)
  cv2.waitKey(0)

if __name__ == "__main__":
  image_path = "image.jpg"
  detect_objects(image_path)
