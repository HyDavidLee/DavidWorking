# open a text file that is in a parent folder to the current working folder
with open("C:/Users/David Lee/Desktop/Git/DavidWorking/UdemyPython/exercises.txt") as file:
    contents = file.read()
    print(contents)