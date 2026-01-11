import os
from PIL import Image, ImageEnhance

def process_png(path, output_path=None):
    """
    Convert a PNG image to grayscale while preserving transparency
    and enhancing contrast.
    """
    img = Image.open(path).convert("RGBA")  # Ensure image has alpha channel

    # Split into RGB and Alpha channels
    r, g, b, a = img.split()

    # Convert RGB to grayscale using luminosity method
    gray = Image.merge("RGB", (r, g, b)).convert("L")

    # Enhance contrast
    enhancer = ImageEnhance.Contrast(gray)
    gray = enhancer.enhance(1.2)  # Adjust factor as needed

    # Merge grayscale with original alpha
    result = Image.merge("RGBA", (gray, gray, gray, a))

    # Save the result
    save_path = output_path if output_path else path
    result.save(save_path)
    print(f"Processed: {save_path}")

def process_folder(folder_path):
    """
    Recursively process all PNG files in a folder and its subfolders.
    """
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".png"):
                full_path = os.path.join(root, file)
                process_png(full_path)

if __name__ == "__main__":
    folder = input("Enter the folder path to process PNGs: ").strip()
    if os.path.isdir(folder):
        process_folder(folder)
        print("All PNGs processed successfully.")
    else:
        print("Invalid folder path.")
