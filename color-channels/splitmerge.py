import cv2
import os

# Specify the relative or absolute path to the image
relative_image_path = 'opencv-stuff/Photos/park.jpg'

# Get the absolute path to the image
image_path = os.path.abspath(relative_image_path)

# Check if the file exists
if not os.path.isfile(image_path):
    print(f"Error: The file {image_path} does not exist.")
else:
    # Load the image
    img = cv2.imread(image_path)

    # Check if the image was loaded correctly
    if img is None:
        print(f"Error: Unable to load image at {image_path}")
    else:
        # Display the original image
        cv2.imshow('Original Image', img)

        # Split the image into its color channels
        b, g, r = cv2.split(img)

        # Display each channel
        cv2.imshow('Blue Channel', b)
        cv2.imshow('Green Channel', g)
        cv2.imshow('Red Channel', r)

        # Merge the channels back
        merged = cv2.merge((b, g, r))
        cv2.imshow('Merged Image', merged)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
