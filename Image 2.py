import cv2

# Use raw string to avoid escape issues
image_path = r'C:/Users/Kousimon/OneDrive/Desktop/Data Scientist/Numpy/WhatsApp Image 2025-06-05 at 19.49.10_db9d6298.jpg'

# Load the image
original = cv2.imread(image_path)

# Check if image loaded
if original is None:
    print("❌ Image not loaded. Please check the file path.")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

    # Convert to black and white using threshold
    _, black_white = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Show image
    cv2.namedWindow("Black and White Image", cv2.WINDOW_NORMAL)
    cv2.imshow("Black and White Image", black_white)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
