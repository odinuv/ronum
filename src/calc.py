def calculate(operation: str, memory: int, input_argument: int) -> int:
    if operation == "+":
        return memory + input_argument
    elif operation == "-":
        return memory - input_argument
    elif operation == "*":
        return memory * input_argument
    elif operation == "/":
        return memory // input_argument
    else:
        raise ValueError(f"Unknown operation: {operation}")

def validate(number: int) -> int:
    if number >= 0 and number <= 4000:
        return 0
    elif number > -1000 and number < 10000:
        return 1
    else:
        return 2
