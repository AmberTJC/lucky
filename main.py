with open("raw.githubusercontent.com_catnap-amuck_august_main_mydefaults.ini.txt") as ini_file:
    data = ini_file.read()

letters = len( [letter for letter in data if letter.isalpha])
print (letters)