import glob
import os

def getFileList(directory):
    files = []
    # 5Mb max
    maxFileSizeInBytes = 5000 * 1024
    for file in glob.glob(directory + "**/*.dds"):
        if (os.path.getsize(os.path.join(directory, file)) > maxFileSizeInBytes):
            files.append(os.path.join(directory, file))
    print("Found Files:\n")
    print(files)
    return files

def processFiles(directory):
    file_list = getFileList(directory)
    for file in file_list:
        img = gimp.pdb.file_dds_load(file, file, 0, 1)
        if (img.width > 1024 and img.height > 1024):
            img.scale(img.width / 2, img.height / 2)
            lay = img.layers[0]
            gimp.pdb.file_dds_save(img, lay, img.filename, img.filename, 1, 1, 0, 0, -1, 0, 0, 1, 1, 2.2, 0, 0, 0.0)
            print("Exported: " + img.filename)

#Example function call
#processFiles("C:\\TextureDir")
