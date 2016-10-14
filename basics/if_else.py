'''
techBytes.io
{{ PYTHON: If/Else Statement }}
Programming Fundamentals
--------------------------------
A If statement consists of:

1. The keyword -> if
2. A condition (that is, an expression that evaluates to True or False)
3. A colon (:)
4. Starting on the next line, an indented block of code (called the if clause)

'''

var = str(input("What color is a pickle? "))
# built in functions string = str and input = input and print = print
print("you entered", var)

def color(var):
	if var == "purple":
		print("Are you sure that is a pickle?")
	else: 
		print("Just remember pickles are green!")

color(var)

# Add in these 
'''
elif var == "blue":
	print("Pickles aren't blue!")
elif var == "red":
	print("When did you have a red pickle?")
'''

# Course we can make this much easier and cleaner 
''''
if var != "green":
	print("Are...")
else:
	print("That's NOT a pickle!")
''''	