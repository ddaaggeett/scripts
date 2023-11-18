#!/usr/bin/bash

file_path="$HOME/.bash_aliases"

# Create the file if it doesn't exist
touch "$file_path"

# Lines to add
lines_to_add=(
    "alias gl='git log --oneline --decorate --graph --all'"
    "alias off='systemctl -i suspend'"
    "alias reboot='systemctl -i reboot'"
    "alias poweroff='systemctl -i poweroff'"
)

# Check if each line exists before adding
for line in "${lines_to_add[@]}"; do
    if ! grep -qF "$line" "$file_path"; then
        echo "$line" >> "$file_path"
        echo "Added: $line"
    else
        echo "Skipped: $line (already exists)"
    fi
done
