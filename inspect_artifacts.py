from PIL import Image

def inspect_regions(path):
    img = Image.open(path).convert("RGBA")
    width, height = img.size
    print(f"Image Size: {width}x{height}")
    
    # Define regions to scan based on user feedback
    # Region 1: Bottom-Left Shadow
    # Estimating x: 0 to 250, y: height-200 to height
    print("\n--- Scanning Bottom-Left Region ---")
    for y in range(height - 200, height, 20):
        row_colors = []
        for x in range(0, 250, 20):
            color = img.getpixel((x, y))
            if color[3] > 0: # Non-transparent
                row_colors.append(f"({x},{y}):{color}")
        if row_colors:
            print(f"Row {y}: {', '.join(row_colors)}")

    # Region 2: Right Artifact
    # Estimating x: width-100 to width, y: 100 to 400
    print("\n--- Scanning Right Region ---")
    for y in range(100, 400, 20):
        row_colors = []
        for x in range(width - 100, width, 10):
            color = img.getpixel((x, y))
            if color[3] > 0:
                row_colors.append(f"({x},{y}):{color}")
        if row_colors:
            print(f"Row {y}: {', '.join(row_colors)}")

if __name__ == "__main__":
    inspect_regions("images/hero-book.png")
