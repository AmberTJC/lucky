with open("raw.githubusercontent.com_catnap-amuck_august_main_mydefaults.ini.txt") as ini_file:
    data = ini_file.read()

letters = 0
for alpha in data:
    if (alpha.isalpha()):
        letters += 1
print (f"the number of letters is {letters}")
