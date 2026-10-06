import os
import subprocess

pieces = ["wP","wR","wN","wB","wQ","wK",
          "bP","bR","bN","bB","bQ","bK"]

input_dir  = os.path.join("assets", "pieces", "svg")
output_dir = os.path.join("assets", "pieces")
os.makedirs(output_dir, exist_ok=True)

for name in pieces:
    src = os.path.join(input_dir, f"{name}.svg")
    dst = os.path.join(output_dir, f"{name}.png")
    subprocess.run([
        "rsvg-convert",
        "-w", "80", "-h", "80",
        "-o", dst,
        src
    ])
    print(f"Converted {name}")

print("Done!")