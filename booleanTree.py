import itertools

def is_valid_expression(expression):
    for i in expression:
        if i.isalpha():
            return True
        elif i in ['&', '|', '!']:
            return True
    return False

def find_variables(expression):
    return sorted(set([x for x in expression if x.isalpha() and x.isupper()]))

def boolean_parser(expression, variable_value):
    expr = expression.replace('&&', "and").replace('||', "or").replace('!', "not")
    for var, value in variable_value.items():
        expr = expr.replace(var, str(value))

    def evaluate_expression(expr):

        if expr == "True":
            return True
        if expr == "False":
            return False
        
        if "not" in expr:
            return not evaluate_expression(expr.replace("not", "", 1).strip())

        if "and" in expr:
            parts = expr.split("and")
            return evaluate_expression(parts[0].strip()) and evaluate_expression(parts[1].strip())

        if "or" in expr:
            parts = expr.split("or")
            return evaluate_expression(parts[0].strip()) or evaluate_expression(parts[1].strip())

        return bool(expr)

    return evaluate_expression(expr)

def generate_table(expression):
    if not is_valid_expression(expression):
        print("The expression contains illegal symbols.")
        return
    
    variables = find_variables(expression)

    if not variables:
        print("There are no variables in the expression.")
        return
    
    combinations = list(itertools.product([False, True], repeat=len(variables)))
    
    header = " | ".join(variables) + " | Result"
    print(header)
    print("-" * len(header))

    for combo in combinations:
        variable_value = dict(zip(variables, combo))
        result = boolean_parser(expression, variable_value)
        
        row = " | ".join(str(int(variable_value[var])) for var in variables) + f" | {int(result)}"
        print(row)

try:
    expression = input("Enter boolean expression: ").strip()
    generate_table(expression)            
except Exception as e:
    print(e)
