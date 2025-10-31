import os
import csv

# --- Folder where CSV will be saved ---
folder_path = r"Price/day wise price"
os.makedirs(folder_path, exist_ok=True)

# --- Full file path ---
file_path = os.path.join(folder_path, "serial_numbers.csv")

# --- Write serial numbers 1 to 1000 ---
with open(file_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Serial_Number"])
    for i in range(1, 1001):
        writer.writerow([i])

print(f"✅ File created: {file_path}")
