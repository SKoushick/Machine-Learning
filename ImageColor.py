import cv2

# Load the original image
image_path = 'C:/Users/Kousimon/OneDrive/Desktop/Data Scientist/Numpy/WhatsApp Image 2025-05-30 at 14.27.45_233f0cb1.jpg'
original = cv2.imread(image_path)

# Step 1: Resize (downframe) the image — keeping aspect ratio
target_size = 512  # Desired maximum dimension
height, width = original.shape[:2]
scaling_factor = target_size / max(height, width)
new_size = (int(width * scaling_factor), int(height * scaling_factor))
resized = cv2.resize(original, new_size, interpolation=cv2.INTER_AREA)

# Step 2: Convert to grayscale
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

# Step 3: Apply threshold to get a black-and-white effect
_, black_white = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Display the original, resized, and black-and-white image
cv2.imshow("Original", original)
cv2.imshow("Downframed Resized", resized)
cv2.imshow("Black and White Design", black_white)

cv2.waitKey(0)
cv2.destroyAllWindows()
