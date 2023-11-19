#!/usr/bin/bash

# directory used with ../binpack/binpack.sh needs to be added to PATH

binpack_dir=$HOME/.local/bin

if [ ! -d "$binpack_dir" ]; then
    mkdir -p "$binpack_dir"
    echo "Directory created: $binpack_dir"
else
    echo "Directory already exists: $binpack_dir"
fi


line_to_add='export PATH="$PATH:$HOME/.local/bin"'

# Check if the line already exists in .bashrc
if ! grep -qxF "$line_to_add" ~/.bashrc; then
    echo "$line_to_add" >> ~/.bashrc
    echo "Line added to .bashrc: $line_to_add"
else
    echo "Line already exists in .bashrc: $line_to_add"
fi
