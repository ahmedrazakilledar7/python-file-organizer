import os

def arrange(files,ext):
    files_with_ext = [file for file in files if file.endswith(ext)]
    print(files_with_ext)

    for i,file in enumerate(files_with_ext):
        os.rename(file,f"image{i+1}{ext}")

if __name__ == "__main__":
        files = os.listdir()
        arrange(files,".jpg")