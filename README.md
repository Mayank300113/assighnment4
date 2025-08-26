# assignment 4
Task 1:

file=open("Sample_File.txt","r")
    r_file=file.read()
    print(r_file)
This program opens the txt file Sample_File.txt and then reads the data written and prints it.

except FileNotFoundError:
    print("Error: the File was not found")
input("Press enter to exit")#for downloading purpose only
Over here if the file Sample_File,txt is not foumd it will print:
Error: the File was not found

Task 2:
w=input("Enter text to write to the file:")

file=open("Output.txt","r+")
wfile=file.write(f"{w}\n")
file.close()
print("Data successfully written to Output.txt")

In this program it writes the given text input to the user in the txt file: Output.txt

ap=input("Enter additional text to append:")

file=open("Output.txt","a")
apile=file.write(ap)
file.close()
print("Data successfully appended to Output.txt")

Over here if the user wants to add some text to the existing file he/she can do it and then it print's: Data successfully appended to Output.txt 

























