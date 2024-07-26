import cv2

def capture_image():
  # Capture image from camera or load from file
  cap = cv2.VideoCapture(0)  # Replace 0 with your camera index
  ret, frame = cap.read()
  if not ret:
    print("Error capturing image")
    return None
  return frame

def preprocess_image(image):
  # Convert to grayscale, apply noise reduction, etc.
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  blurred = cv2.GaussianBlur(gray, (5, 5), 0)
  return blurred
