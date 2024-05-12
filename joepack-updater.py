import os
import shutil
import subprocess

def download_github_repo(repo_url, folder_path):
    # Check if folder exists
    if os.path.exists(folder_path):
        print(f"The folder '{folder_path}' already exists.")
        print(f"Make sure '{folder_path}' is unequipped in the resource packs, then delete it.")
        input(f"Please delete the '{folder_path}' folder and try again ")
        return

    # Clone the GitHub repo
    subprocess.run(["git", "clone", repo_url, folder_path])

if __name__ == "__main__":
    repo_url = "https://github.com/Episode353/joepack"
    folder_path = "joepack"

    download_github_repo(repo_url, folder_path)

# to build use command
# pyinstaller joepack-updater.py --onefile