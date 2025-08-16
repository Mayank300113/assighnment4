w=input("Enter text to write to the file:")

file=open("Output.txt","r+")
wfile=file.write(f"{w}\n")
file.close()
print("Data successfully written to Output.txt")

ap=input("Enter additional text to append:")

file=open("Output.txt","a")
apile=file.write(ap)
file.close()
print("Data successfully appended to Output.txt")

file=open("Output.txt","r")
apl=file.read()
print(apl)

input("Press enter to exit")#just for downloading purposes