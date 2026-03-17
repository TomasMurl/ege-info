#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="${1:-.}"

find "$ROOT_DIR" -type d -depth | while read -r dir; do
    base="$(basename "$dir")"
    parent="$(dirname "$dir")"

    # Проверка формата DD_MM
    if [[ "$base" =~ ^[0-9]{2}_[0-9]{2}$ ]]; then
        day="${base%%_*}"
        month="${base##*_}"

        target_dir="$parent/$month/$day"

        echo "Processing: $dir -> $target_dir"

        mkdir -p "$parent/$month"

        if [[ -e "$target_dir" ]]; then
            echo "Skip (already exists): $target_dir"
            continue
        fi

        mv "$dir" "$target_dir"
    fi
done