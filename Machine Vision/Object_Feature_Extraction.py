import cv2

def extract_features(image, keypoints):
  # Extract features like shape, size, color, texture
  # Example: Calculate bounding boxes
  boxes = []
  for kp in keypoints:
    x, y = int(kp.pt[0]), int(kp.pt[1])
    s = int(kp.size)
    boxes.append((x - s, y - s, x + s, y + s))
  return boxes
