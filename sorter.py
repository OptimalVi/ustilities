#!/bin/python3
import os
import exifread
from collections import defaultdict
from datetime import datetime

originalDir = './'
extensioins = [".dng", ".gpeg"]



def get_content_year_month_created(file_path):
    with open(file_path, 'rb') as f:
        tags = exifread.process_file(f, details=False)
        tag = ''

        if 'Image DateTimeOriginal' in tags:
            tag = 'Image DateTimeOriginal'
        elif 'EXIF DateTimeOriginal' in tags:
            tag = 'Exif DateTimeOriginal'
        else: return None

        createdAt = datetime.strptime(str(tags[tag]), "%Y:%m:%d %H:%M:%S")
        
        return f"{createdAt.year}_{createdAt.month}"

def move_file(originalDir, folder, filename):
    resultDir = os.path.join(originalDir, folder)
    if not os.path.exists(resultDir): os.mkdir(resultDir)
    filePath= os.path.join(originalDir, filename)
    if not os.path.exists: print(f"file does not exist {filePath}")
    os.rename(
        filePath,
        os.path.join(resultDir, filename)
        )    

def main(originalDir, extensions):
    for filename in os.listdir(extensioins):
        if filename.lower().endswith():
            folder = get_content_year_month_created(os.path.join(originalDir, filename))
            print(folder)
            move_file(originalDir, folder, filename)

    print("Grouping completed.")

main(originalDir, extensioins)

