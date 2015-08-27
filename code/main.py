import os
import representation as rps
import visualisation as vis

# This is main script that asks user for filename, opens that file and calls for explicit functions
# output of this script can be set to just plotting the data or creating a bunch of 'png's by replacing
# comment marks at the end

filename = input("Enter file name: ")
# filename = 'picture.jpg'
pathname = os.path.join('..', os.path.join('input_data_examples', filename))    # system-independent path
filesize = os.path.getsize(pathname)
file = open(pathname, 'rb')
try:
    if filesize < 4000:
        print("Using simple representation")
        data = rps.represent_simple(file, filesize)
    else:
        print("Using advanced PCA representation")
        data = rps.represent_PCA(file, filesize)
finally:
    file.close()

# vis.createPNGs(data)
vis.visualizeIt(data)