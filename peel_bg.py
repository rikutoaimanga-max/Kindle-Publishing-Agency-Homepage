from PIL import Image, ImageDraw
import numpy as np

def peel_background(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    width, height = img.size
    
    # Max iterations to avoid infinite loops
    for i in range(10):
        bbox = img.getbbox()
        if not bbox:
            print("Image is empty!")
            break
            
        print(f"Iteration {i}: BBox {bbox}")
        
        # Check midpoints of the bbox edges
        left, top, right, bottom = bbox
        
        # Points to check: midpoints of the 4 sides of the bbox
        # We move 1 pixel inside to ensure we hit the content
        check_points = [
            (left, top + (bottom-top)//2),   # Left edge
            (right-1, top + (bottom-top)//2), # Right edge
            (left + (right-left)//2, top),   # Top edge
            (left + (right-left)//2, bottom-1) # Bottom edge
        ]
        
        changed = False
        for x, y in check_points:
            # Ensure coordinates are within bounds
            x = max(0, min(x, width-1))
            y = max(0, min(y, height-1))
            
            color = img.getpixel((x, y))
            
            # Heuristic: If it's light (background), flood fill it
            # Book is dark blue, so R,G,B should be low.
            # Backgrounds are usually > 200.
            # Let's say if any channel is > 150, it's suspicious?
            # Or if it's close to white/gray.
            # (233, 235, 237) is definitely background.
            
            if color[3] > 0 and (color[0] > 180 and color[1] > 180 and color[2] > 180):
                print(f"  Found background {color} at ({x}, {y}). Flood filling...")
                ImageDraw.floodfill(img, (x, y), (0, 0, 0, 0), thresh=50)
                changed = True
                
        if not changed:
            print("  No more background found at edges.")
            break
            
    # Final Crop to BBox
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
        print(f"Final Crop to {bbox}")
        
    img.save(output_path)
    print(f"Saved to {output_path}")

if __name__ == "__main__":
    input_file = "images/hero-book.png"
    output_file = "images/hero-book.png"
    try:
        peel_background(input_file, output_file)
    except Exception as e:
        print(f"Error: {e}")
