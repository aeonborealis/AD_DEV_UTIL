import operator

# Define a dictionary of mathematical operators and their symbols
operators = {
    "plus": operator.add,
    "minus": operator.sub,
    "multiplied by": operator.mul,
    "divided by": operator.truediv
}

# Define a function that parses the input and generates a math problem
def generate_math_problem(input_string):
    # Split the input into words
    words = input_string.split()

    # Find the operator in the input
    operator_word = next((word for word in words if word in operators), None)

    if not operator_word:
        raise ValueError("No mathematical operator found in input")

    # Find the indices of the two numbers in the input
    operator_index = words.index(operator_word)
    num1_index = operator_index - 1
    num2_index = operator_index + 1

    # Convert the words to numbers
    num1 = float(words[num1_index])
    num2 = float(words[num2_index])

    # Apply the operator to the numbers
    result = operators[operator_word](num1, num2)

    # Generate the math problem as a string
    problem = f"{num1} {operator_word} {num2} = {result}"

    return problem

# Example usage
input_string = "What is 5 multiplied by 7?"
problem = generate_math_problem(input_string)
print(problem)
