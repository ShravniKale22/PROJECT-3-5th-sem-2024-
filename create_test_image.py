import numpy as np
import cv2

# Create a 400x600 image with white background
img = np.ones((400, 600, 3), dtype=np.uint8) * 255

# Draw colored rectangles
colors = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (255, 0, 255),  # Magenta
    (0, 255, 255),  # Cyan
    (128, 0, 128),  # Purple
    (255, 165, 0)   # Orange
]

# Draw rectangles with different colors
for i, color in enumerate(colors):
    x = 50 + i * 70
    cv2.rectangle(img, (x, 50), (x + 60, 110), color, -1)
    cv2.rectangle(img, (x, 150), (x + 60, 210), color, -1)

# Add some text
cv2.putText(img, "Double click on any color to detect it", (50, 300), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

# Save the image
cv2.imwrite('test_image.jpg', img)
print("Test image created successfully as 'test_image.jpg'")