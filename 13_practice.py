letter = '''Dear <|Name|>,
congratulation dear you are promoted for your sucsess
you are selected!

date: <|Date|>

'''
Name = input("Enter your name\n")
Date = input("Enter the date\n")
letter = letter.replace("<|Name|>",Name)
letter = letter.replace("<|Date|>",Date)
print(letter)