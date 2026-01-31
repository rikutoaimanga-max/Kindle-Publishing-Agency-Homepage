$path = "c:\Users\PC_User\OneDrive\デスクトップ\kindle出版制作代行HP\css\style.css"
$content = Get-Content -Path $path -Raw
$newBlock = "/* Video Section */
.video-section {
    padding: 80px 0 40px;
    background: var(--background-color);
    text-align: center;
}

.video-wrapper {
    position: relative;
    width: 100%;
    max-width: 700px;
    aspect-ratio: 16 / 9;
    margin: 0 auto;
    border-radius: 20px;
    box-shadow: var(--shadow-xl);
    background: #000;
    overflow: hidden;
}

"
# Regex to match from "/* Video Section */" up to ".video-wrapper iframe"
# We use [regex]::Escape for the start and end markers to be safe, but we need to match the content in between.
# The content in between contains newlines, so we use (?s) single-line mode (dot matches newline).
$pattern = "(?s)/\*\s*Video Section\s*\*/.*?(?=\.video-wrapper iframe)"

if ($content -match $pattern) {
    $newContent = $content -replace $pattern, $newBlock
    Set-Content -Path $path -Value $newContent -Encoding UTF8
    Write-Host "CSS updated successfully."
} else {
    Write-Host "Pattern not found."
    exit 1
}
