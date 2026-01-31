
import os

file_path = "css/style.css"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Define replacements
# 1. Simplify .hero-book-img
old_block_1 = """.hero-book-img {
    max-width: 100%;
    height: auto;
    filter: drop-shadow(0 20px 30px rgba(0, 0, 0, 0.3));
    transition: all 0.5s ease;
}"""

new_block_1 = """.hero-book-img {
    max-width: 100%;
    height: auto;
}"""

# 2. Remove .hero-book-img:hover and @keyframes sway
old_block_2 = """.hero-book-img:hover {
    filter: drop-shadow(0 30px 50px rgba(194, 155, 64, 0.4));
    animation: sway 2s ease-in-out infinite;
}

@keyframes sway {
    0% {
        transform: translateX(0);
    }
    25% {
        transform: translateX(-10px);
    }
    75% {
        transform: translateX(10px);
    }
    100% {
        transform: translateX(0);
    }
}"""

new_block_2 = ""

# Perform replacements
if old_block_1 in content:
    content = content.replace(old_block_1, new_block_1)
    print("Replaced block 1")
else:
    print("Block 1 not found")

if old_block_2 in content:
    content = content.replace(old_block_2, new_block_2)
    print("Replaced block 2")
else:
    print("Block 2 not found")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
