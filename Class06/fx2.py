# Determine the code type.
# Returns "Invalid Code" if not found.

def code_type(code):

    if len(code) == 7:
        return "Legacy Code"

    if code[0:1] == "9":
        return "Current Code"
    return "Invalid Code"

print(code_type("498765435"))