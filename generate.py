import os
import io
import math
import shutil
import hashlib
from PIL import Image
import cairosvg
import xml.etree.ElementTree as ET

ET.register_namespace("", "http://www.w3.org/2000/svg")

# === PRESET CONFIGURATION ===
PRESETS = {
    "light-thin":  {
        "stroke": "#E6E0FF", "fill": "#E6E0FF", "grid_bg": (230, 224, 255, 255),
    },
    "light-bold": {
        "stroke": "#000000", "fill": "#E6E0FF", "grid_bg": (230, 224, 255, 255),
    },
    "dark-thin": {
        "stroke": "#000000", "fill": "#000000", "grid_bg": (30, 30, 30, 255),
    },
    "dark-bold": {
        "copy_original": True, "grid_bg": (30, 30, 30, 255),
    }
}
# Get the current script directory (safe and robust for relative paths)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Define relative paths
INPUT_FOLDER = os.path.join(SCRIPT_DIR, "../Resources/Sustyicons")
BASE_OUTPUT_FOLDER = os.path.join(SCRIPT_DIR, "../Resources/Sustyicons")
GRID_OUTPUT_FOLDER = os.path.join(BASE_OUTPUT_FOLDER, "demo-pics")
ICON_SIZE = 128
COLUMNS = 12

os.makedirs(GRID_OUTPUT_FOLDER, exist_ok=True)

# === UTILITY: Get hash of file ===
def file_hash(filepath):
    with open(filepath, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

# === STEP 1: Process all presets ===
for name, config in PRESETS.items():
    print(f"\n🔧 Processing preset: {name}")
    preset_output_folder = os.path.join(BASE_OUTPUT_FOLDER, f"Sustyicons-{name}")
    os.makedirs(preset_output_folder, exist_ok=True)

    svg_files = [f for f in os.listdir(INPUT_FOLDER) if f.endswith(".svg")]
    change_detected = False
    hash_cache_path = os.path.join(preset_output_folder, ".hashcache")

    # Load old hash cache
    old_hashes = {}
    if os.path.exists(hash_cache_path):
        with open(hash_cache_path, "r") as f:
            for line in f:
                svg_name, hashval = line.strip().split(",")
                old_hashes[svg_name] = hashval
    new_hashes = {}

    for svg_file in svg_files:
        input_path = os.path.join(INPUT_FOLDER, svg_file)
        output_path = os.path.join(preset_output_folder, svg_file)
        current_hash = file_hash(input_path)
        new_hashes[svg_file] = current_hash

        # Skip if no change
        if svg_file in old_hashes and old_hashes[svg_file] == current_hash:
            continue

        change_detected = True

        # === Preset: dark-bold is a copy ===
        if config.get("copy_original"):
            shutil.copy2(input_path, output_path)
            print(f"📄 Copied '{svg_file}' for dark-bold.")
            continue

        # === Modify SVG ===
        tree = ET.parse(input_path)
        root = tree.getroot()

        for elem in root.iter():
            if 'stroke' in elem.attrib:
                elem.attrib['stroke'] = config["stroke"]
            if 'fill' in elem.attrib:
                elem.attrib['fill'] = config["fill"]

        tree.write(output_path)
        print(f"🎨 Modified '{svg_file}' for preset '{name}'.")

    # Save updated hash cache
    with open(hash_cache_path, "w") as f:
        for svg_file, hashval in new_hashes.items():
            f.write(f"{svg_file},{hashval}\n")

    if not change_detected:
        print(f"✅ No changes for preset '{name}'. Grid generation skipped.")
        continue

    # === STEP 2: Generate Grid ===
    print(f"🧱 Generating grid for preset '{name}'...")
    png_images = []
    svg_files = sorted([f for f in os.listdir(preset_output_folder) if f.endswith(".svg")])

    for svg_file in svg_files:
        svg_path = os.path.join(preset_output_folder, svg_file)
        png_bytes = cairosvg.svg2png(url=svg_path, output_width=ICON_SIZE, output_height=ICON_SIZE)
        img = Image.open(io.BytesIO(png_bytes)).convert("RGBA")
        png_images.append(img)

    rows = math.ceil(len(png_images) / COLUMNS)
    grid_width = COLUMNS * ICON_SIZE
    grid_height = rows * ICON_SIZE
    grid_img = Image.new("RGBA", (grid_width, grid_height), config["grid_bg"])

    for index, img in enumerate(png_images):
        x = (index % COLUMNS) * ICON_SIZE
        y = (index // COLUMNS) * ICON_SIZE
        grid_img.paste(img, (x, y), img)

    grid_path = os.path.join(GRID_OUTPUT_FOLDER, f"{name}-grid.webp")
    grid_img.save(grid_path, format="WEBP")
    print(f"🖼️ Grid saved: {grid_path}")

print("\n✅ All processing complete.")
