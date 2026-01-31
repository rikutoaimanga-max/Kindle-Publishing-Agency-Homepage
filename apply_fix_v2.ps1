$path = "c:\Users\PC_User\OneDrive\デスクトップ\kindle出版制作代行HP\css\style.css"
$content = Get-Content -Path $path -Raw

# The target string to replace. We use the exact lines we saw.
# Note: We use regex to be slightly flexible with whitespace just in case, but specific enough.
# Pattern: padding-bottom... comment... height: 0;
$pattern = "padding-bottom: 56\.25%;\s+/\* 16:9 Aspect Ratio \*/\s+height: 0;"

$replacement = "width: 100%;
    aspect-ratio: 16 / 9;"

if ($content -match $pattern) {
    $newContent = $content -replace $pattern, $replacement
    Set-Content -Path $path -Value $newContent -Encoding UTF8
    Write-Host "Success: CSS updated."
} else {
    Write-Host "Error: Pattern not found."
    # Print a snippet to debug
    $lines = $content -split "`r`n"
    for ($i=410; $i -lt 425; $i++) {
        if ($i -lt $lines.Count) {
            Write-Host "$($i+1): $($lines[$i])"
        }
    }
}
