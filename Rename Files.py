import os
def rename_files():
    #1 Get filenames from folder
    file_list = os.listdir("/Users/tamjeff/Downloads/prank")
    print(file_list)
    saved_path = os.getcwd()
    print(saved_path)
    os.chdir("/Users/tamjeff/Downloads/prank")

    #2 Rename files
    for file_name in file_list:
        print("Renaming "+ file_name + " to " + file_name.translate(None, "123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))

    os.chdir(saved_path)
    
rename_files()
