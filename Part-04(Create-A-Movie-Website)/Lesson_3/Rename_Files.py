import os
import string

def rename_files():
    # (1) Get files name from a folder
    file_list = os.listdir(r"C:\Users\DELL\Documents\prank\prank")
    #print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is " + saved_path)
    os.chdir(r"C:\Users\DELL\Documents\prank\prank")

    # (2) For each files , rename filename

    for file_name in file_list:
        print("Old Name - " + file_name)
        translation_table = str.maketrans("0123456789", "          ", "0123456789")
        print("New Name - " + file_name.translate(translation_table))
        os.rename(file_name,file_name.translate(translation_table))
    os.chdir(saved_path)
rename_files()
