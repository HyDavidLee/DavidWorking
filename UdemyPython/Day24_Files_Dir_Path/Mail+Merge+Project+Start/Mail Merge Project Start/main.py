#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Mail Merge Project Start/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("./Mail Merge Project Start/Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()
    
    for name in names:
        remove_nl = name.strip()
        new_letter = letter.replace("[name]", remove_nl)
        print(new_letter)
        with open(f"./Mail Merge Project Start/Output/ReadyToSend/letter_for{remove_nl}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
    
    