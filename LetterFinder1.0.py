print("Enter a random sentence: ")
sentence = input()
 
letters_digits = {"Letters":0, "Digits":0}
 
for x in sentence:
    if x.isalpha():
        letters_digits["Letters"]+=1
    elif x.isdigit():
        letters_digits["Digits"]+=1
    else:
        pass
 
print("Letters", letters_digits["Letters"])
print("Digits", letters_digits["Digits"])
