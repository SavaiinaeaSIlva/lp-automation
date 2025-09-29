from PIL import Image
import sys

# --- Configuration ---
# Get the filename from the command line, default to 'logo.png'
input_filename = sys.argv[1] if len(sys.argv) > 1 else 'logo.png'
output_filename = 'logo_cropped.png'

try:
    # Open the original image
    with Image.open(input_filename) as img:
        print(f"✅ Successfully opened '{input_filename}'")

        # Get the bounding box of the non-background pixels.
        # This function scans the image and finds the coordinates of the actual content.
        bbox = img.getbbox()

        if bbox:
            print(f"Found content at coordinates: {bbox}")
            
            # Crop the image using the bounding box coordinates
            cropped_img = img.crop(bbox)

            # Save the new, cropped image
            cropped_img.save(output_filename)
            
            print(f"✨ Success! Cropped image saved as '{output_filename}'")
            print("\nNext step: Rename 'logo_cropped.png' to 'logo.png' to use it on your website.")
        else:
            # This happens if the image is completely blank
            print("⚠️ Could not find any content to crop. The image might be empty.")

except FileNotFoundError:
    print(f"❌ Error: The file '{input_filename}' was not found.")
    print("Please make sure this script is in the same folder as your logo file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
