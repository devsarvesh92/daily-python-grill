def valid_parentheses(*, input: str) -> bool:
    matching_parentheses: dict[str, str] = {"(": ")", "{": "}", "[": "]"}
    stack: list[str] = []

    for c in input:
        if c in matching_parentheses:
            stack.append(c)
        else:
            last_parentheses = stack.pop()
            if c != matching_parentheses[last_parentheses]:
                return False

    return True
