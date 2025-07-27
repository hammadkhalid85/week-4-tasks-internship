user_input = input("Enter any value: ")

# Show its data type
print("Data type of your input is:", type(user_input))

# Example of exec()
code_to_execute = "print('Hello from exec!')"
exec(code_to_execute)  # Executes the string as Python code
