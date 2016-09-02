import shutil
import os

def rename_files():
    # Get file names from a folder
    # For each file, rename file

    in_path = r"/Users/jdrsteiny/Documents/Udacity Projects/StripNumbersFromFilenames/StripNumbersFromFilenames/prank/"
    out_path = r"/Users/jdrsteiny/Documents/Udacity Projects/StripNumbersFromFilenames/StripNumbersFromFilenames/result/"

    file_list = os.listdir(in_path)

    for file_name in file_list:
        if ( file_name.split(".")[-1] == "jpg" ):
            new_name = file_name.translate(None, "0123456789")

            print("Old File = "+file_name+" New File = "+new_name)
            
            shutil.copyfile( in_path+file_name, out_path+new_name )        

rename_files()
