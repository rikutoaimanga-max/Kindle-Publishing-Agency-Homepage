from PIL import Image

def inspect_colors(path):
    img = Image.open(path).convert("RGBA")
    width, height = img.size
    
    points = [
        (0, 0),
        (width//2, 0),
        (0, height//2),
        (width-1, height-1),
        (width//10, height//10), # Inner-ish
        (width//2, height//2)    # Center (Book)
    ]
    
    print(f"Image Size: {width}x{height}")
    for x, y in points:
        color = img.getpixel((x, y))
        print(f"Color at ({x}, {y}): {color}")

if __name__ == "__main__":
    inspect_colors("images/hero-book.png")
