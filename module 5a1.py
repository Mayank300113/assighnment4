try:
    file=open("Sample_File.txt","r")
    r_file=file.read()
    print(r_file)
    file.close()
except FileNotFoundError:
    print("Error: the File was not found")
input("Press enter to exit")#for downloading purpose only


