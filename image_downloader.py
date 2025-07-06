# Script searches for any links to images hosted on github.com/user-attachments/assets/ (usually pasted to github .md file from clipboard),  downloads all the pictures to repo folder and updates links in .md files so repo images are used


import requests
import os
import re

repo_path = os.getcwd()
download_folder = "img"
pattern = re.compile(r'https://github.com/user-attachments/assets/[a-f0-9\-]+')


target_path = os.path.join(repo_path, download_folder)
os.makedirs(target_path, exist_ok=True)

# go through all .md files
for root, dirs, files in os.walk(repo_path):
    for file in files:
        if file.endswith(".md"):
            source_file_path = os.path.join(root, file)
            # read file and find all links to github hosted pictures
            with open(source_file_path, "r", encoding="utf-8", errors="ignore") as f:
                content_str = f.read()
            matches = pattern.findall(content_str)
            print(f"\nDEBUG: {source_file_path} -> {matches}")
            
            for idx, old_image_url in enumerate(matches, 1):
                file_index = 1
                while True:
                    target_filename = f"{file.replace('/', '_').replace('.md','')}_{file_index}.png"
                    target_filepath = os.path.join(target_path, target_filename)
                    if os.path.exists(target_filepath):
                        file_index+=1
                    else:
                        break
                        
                print(f"[DOWNLOAD] {old_image_url} -> {target_filepath}")
                r = requests.get(old_image_url)
                if r.status_code == 200:
                    with open(target_filepath, "wb") as out_file:
                        out_file.write(r.content)
                else:
                    print(f"[ERROR] Cannot download {old_image_url}")
                    
                new_image_path = f"{download_folder}/{target_filename}"
                content_str = content_str.replace(old_image_url, new_image_path)
                                
            with open(source_file_path, "w", encoding="utf-8", errors="ignore") as f:
                f.write(content_str)

print(f"Hotovo. Staženo do složky '{download_folder}'.")
input()