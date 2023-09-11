import os

# Simulate user input
user_input = input("Enter a file name: ")

# Insecurely construct a command
command = "cat " + user_input

# Execute the command
result = os.system(command)
