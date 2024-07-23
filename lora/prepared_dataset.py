import os
import shutil
import json

# Define your source and target directories
source_dir = 'train'
target_dir = 'folder/train'
metadata_file = os.path.join(target_dir, 'metadata.jsonl')

# Create the target directory if it doesn't exist
os.makedirs(target_dir, exist_ok=True)

# Prepare to write to the metadata.jsonl file
with open(metadata_file, 'w') as metafile:
    # Walk through the source directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.png'):
                # Extract category from the path
                category = os.path.basename(root)
                # Construct the new file name and path
                new_file_path = os.path.join(target_dir, file)
                # Move file to the new directory
                shutil.move(os.path.join(root, file), new_file_path)
                # Create a metadata entry
                metadata = {
                    "file_name": file,
                    "additional_feature": f"sketch of {category}"
                }
                # Write the JSON line to the file
                metafile.write(json.dumps(metadata) + '\n')

print("Dataset preparation is complete.")
