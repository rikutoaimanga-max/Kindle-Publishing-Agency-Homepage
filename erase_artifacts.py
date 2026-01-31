from PIL import Image

def erase_artifacts(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    width, height = img.size
    pixels = img.load()
    
    print(f"Processing {width}x{height} image")
    
    # 1. Erase Bottom-Left Shadow
    # User circled the bottom left.
    # Based on scan, shadow is roughly x < 160 and y > 580.
    # The book starts around x=160 at the bottom.
    # We will be conservative: erase x < 150, y > 550.
    
    print("Erasing bottom-left shadow...")
    for y in range(550, height):
        for x in range(0, 155):
            # Check if it's the book (dark) or shadow (light)
            r, g, b, a = pixels[x, y]
            if a > 0:
                # Shadow is usually light gray (e.g. > 100)
                # Book is dark (e.g. < 50)
                # But let's just erase the region if it's not super dark
                if r > 80 and g > 80 and b > 80:
                    pixels[x, y] = (0, 0, 0, 0)
                elif x < 100: # Far left is definitely shadow
                    pixels[x, y] = (0, 0, 0, 0)

    # 2. Erase Right Artifact
    # User circled a detached artifact on the right.
    # Let's find where the book ends on the right.
    # Scan from right to left at y=400 (middle)
    book_right_edge = width
    for x in range(width-1, 0, -1):
        r, g, b, a = pixels[x, 400]
        if a > 0:
            book_right_edge = x
            break
    print(f"Book appears to end around x={book_right_edge}")
    
    # If the artifact is detached, it might be to the right of this edge?
    # Or maybe the artifact IS what I found?
    # Let's assume the artifact is in the rightmost 50px.
    # We'll erase everything x > book_right_edge + 20 (buffer)
    
    erase_start_x = book_right_edge + 20
    if erase_start_x < width:
        print(f"Erasing right artifacts starting at x={erase_start_x}")
        for y in range(0, height):
            for x in range(erase_start_x, width):
                pixels[x, y] = (0, 0, 0, 0)
    
    # Also specifically check the top-right area where artifacts often hide
    # x > 700, y < 400
    for y in range(0, 400):
        for x in range(740, width):
             pixels[x, y] = (0, 0, 0, 0)

    img.save(output_path)
    print(f"Saved to {output_path}")

if __name__ == "__main__":
    erase_artifacts("images/hero-book.png", "images/hero-book.png")
