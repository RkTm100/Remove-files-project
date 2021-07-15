import os
import shutil
import time

def main():
    deleted_files=0
    deleted_folders=0
    path="C:\Users\asish\OneDrive\Desktop\backup files for class\backfiles removing folder testing"
    days=30
    seconds=time.time(-days*24*60*60)
    if os.path.exists(path):
        for root_folder, folders, files in os.walk(path):
            if seconds >= get_file_or_folder_age(root_folder):
                remove_folder(root_folder)
                deleted_folders+=1
                break
            else:
                for folder in folders:
                    folder_path=os.path.join(root_folder,folder)
                    if seconds >= get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)
                        deleted_folders+=1
                for file in files:
                    file_path=os.path.join(root_folder,file)
                    if seconds >= get_file_or_folder_age(file_path):
                        remove_file(file_path)
                        deleted_files+=1
    else:
        print("there is no files or folders")
    print(f"total folders deleted:  + {deleted_folders}")
    print(f"total files deleted: + {deleted_files}")
    main()
                    
                    
                    


    