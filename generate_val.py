  
import os

image_files = []
os.chdir(os.path.join("data", "val"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        image_files.append("data/val/" + filename)
os.chdir("..")
with open("val.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")