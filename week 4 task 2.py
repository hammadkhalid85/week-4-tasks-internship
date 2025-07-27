expression = input("Enter a Python expression (e.g., 2 + 3 * 4): ")

# Create a variable to store result
result_var = "result"
exec(f"{result_var} = {expression}")
print("Result of your expression:", locals()[result_var])
