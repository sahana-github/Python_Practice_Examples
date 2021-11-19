letter = '''Dear <|Name|>, 
Greetings from abc coding house i am happy to tell you that
you are selected!
have a great day ahead!
Thanks and regards,
Bill
Date:<|date|>'''
name = input("Enter your Name\n")
date = input("Enter Date\n")
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|date|>", date)
print(letter)
