import json, os

print("Welcome to the File Processing Program.")
print()
#prompt user for directory and name of file
foundDir = "0"
while foundDir == "0":
	userDir = input("Please specify the directory of the file: ")
	print()
	CHECK_FOLDER = os.path.isdir(userDir)
	if not CHECK_FOLDER:
		print("I'm sorry, that directory doesn't exist. Please try again.")
		print()
	else:
		foundDir = "1"	
userFilename = input("Please specify the name of the file to create: ")
print()
#prompt for name/addr/phone
userName = input("May I have your name, please? ")
print()
userAddr = input("May I have your address, please? ")
print()
userPhone = input("May I have your phone number please? ")
print()
fileLine = str(userName) + ", " + str(userAddr) + ", " + str(userPhone)
#write to file
with open(userFilename, 'w') as f:
	json.dump(fileLine, f)
print("We've written your data to a file. Let's load it back and print it out: ")
print("")
with open(userFilename) as f:
	fileRead = json.load(f)
print(f"Here's the data we have: {fileRead}")	
print()
print("Thank you for using the File Processing Program.")