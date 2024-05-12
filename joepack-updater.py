import os
import shutil
import urllib.request

def main():
    if os.path.exists("joepack"):
        print("You already have Joepack!")
        print("Please delete the 'joepack' folder before updating.")
        input("Press Enter to exit...")  # Wait for user confirmation before closing
    else:
        download_repo()
        input("Press Enter to exit...")  # Wait for user confirmation before closing

def download_repo():
    print("Downloading Joepack...")
    url = "https://github.com/Episode353/joepack/archive/main.zip"
    zip_file = "joepack-main.zip"
    urllib.request.urlretrieve(url, zip_file)

    print("Extracting Joepack...")
    shutil.unpack_archive(zip_file, ".")  # Extract directly into the current directory


    os.remove(zip_file)
    # Rename the extracted folder to "joepack"
    os.rename("joepack-main", "joepack")
    print("Joepack downloaded successfully.")



if __name__ == "__main__":
    main()
