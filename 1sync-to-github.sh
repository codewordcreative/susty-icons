#!/bin/bash

echo "Starting SVG processing and grid generation..."

# Step 1: Run processing scripts
python "generate.py"

echo "SVG processing complete."

# Step 3: Stage all changes
git add .

# Step 4: Commit with timestamp
git commit -m "Updated via script on $(date +'%Y-%m-%d %H:%M:%S')"

# Step 5: Push to GitHub
git push origin main

echo "✅ All done! Changes synced to GitHub."
