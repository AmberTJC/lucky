with open("raw.githubusercontent.com_catnap-amuck_august_main_mydefaults.ini.txt") as ini_file:
    data = ini_file.read()

letters = 0
numbers = 0
for alpha in data:
    if (alpha.isalpha()):
        letters += 1
print (f"the number of letters is {letters}")

for num in data:
    if (num.isdigit()):
        numbers += 1
print (f"The number of digits is {numbers}")

output = open("outputs.txt", "w")
output.write("The number of letters is 486")
output.write ("the number of digits is 1")
output.close