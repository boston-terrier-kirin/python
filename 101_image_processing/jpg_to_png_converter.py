import sys
import os
from PIL import Image

if len(sys.argv) != 3:
    print("Invalid args")
    exit()

args = sys.argv[1:]
from_dir = args[0]
to_dir = args[1]

if not os.path.exists(to_dir):
    os.mkdir(to_dir)

jpgs = os.listdir(from_dir)

for jpg in jpgs:
    from_file_path = f"./{from_dir}/{jpg}"

    to_file_name = os.path.splitext(jpg)[0] + ".png"
    to_file_path = f"./{to_dir}/{to_file_name}"

    print(f"Converting {jpg}...")
    img = Image.open(from_file_path)
    img.save(to_file_path, "png")
