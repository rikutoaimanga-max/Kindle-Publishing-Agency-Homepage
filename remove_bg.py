from PIL import Image
import numpy as np

def remove_white_background(input_path, output_path, threshold=240):
    img = Image.open(input_path).convert("RGBA")
    data = np.array(img)
    
    # Extract RGB channels
    r, g, b, a = data.T
    
    # Identify white pixels (where all R, G, B are above threshold)
    white_areas = (r > threshold) & (g > threshold) & (b > threshold)
    
    # Set alpha to 0 for white pixels
    data[..., 3][white_areas.T] = 0
    
    # Create new image from modified data
    new_img = Image.fromarray(data)
    new_img.save(output_path)
    print(f"Processed {input_path} and saved to {output_path}")

if __name__ == "__main__":
    input_file = "images/hero-book.png"
    output_file = "images/hero-book.png"
    try:
        remove_white_background(input_file, output_file)
    except Exception as e:
        print(f"Error: {e}")
