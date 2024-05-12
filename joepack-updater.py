import os
import shutil
import urllib.request

def main():
    if os.path.exists("joepack"):
        print("Please delete the 'joepack' folder before continuing.")
    else:
        download_repo()
        input("Press Enter to exit...")  # Wait for user confirmation before closing

def download_repo():
    url = "https://github.com/Episode353/joepack/archive/main.zip"
    zip_file = "joepack-main.zip"
    urllib.request.urlretrieve(url, zip_file)
    shutil.unpack_archive(zip_file, ".")  # Extract directly into the current directory
    os.remove(zip_file)
    # Rename the extracted folder to "joepack"
    os.rename("joepack-main", "joepack")
    print("Repository downloaded successfully.")



if __name__ == "__main__":
    main()
