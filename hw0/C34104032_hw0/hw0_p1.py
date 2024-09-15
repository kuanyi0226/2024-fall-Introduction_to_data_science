# Function to parse a polynomial string into terms
def parse_polynomial(poly_str):
    poly_str = poly_str.replace(" ", "")
    terms = []
    current_term = ""
    
    for i, char in enumerate(poly_str):
        if char in "+-" and i > 0:
            terms.append(current_term)
            current_term = char
        else:
            current_term += char
    
    terms.append(current_term)
    return terms

# Function to extract coefficient, variables, and exponents
def parse_term(term):
    if "*" not in term:
        if term[0] == '-':
            coefficient = -1
            variables = term[1:] if len(term) > 1 else ''
        elif term[0] == '+':
            coefficient = 1
            variables = term[1:] if len(term) > 1 else ''
        else:
            coefficient = 1 if term[0].isalpha() else int(term)
            variables = term if term[0].isalpha() else ''
    else:
        coefficient_part, variables = term.split("*")
        coefficient = int(coefficient_part)
    
    var_dict = {}
    current_var = ""
    for i, char in enumerate(variables):
        if char.isalpha():
            current_var = char
            var_dict[current_var] = 1
        elif char == "^":
            var_dict[current_var] = int(variables[i+1])
    
    return coefficient, var_dict

# Function to multiply two terms
def multiply_terms(term1, term2):
    coef1, vars1 = parse_term(term1)
    coef2, vars2 = parse_term(term2)
    
    new_coef = coef1 * coef2
    new_vars = vars1.copy()
    
    for var, exp in vars2.items():
        if var in new_vars:
            new_vars[var] += exp
        else:
            new_vars[var] = exp
    
    return new_coef, new_vars

# Function to convert the parsed terms back to a string format
def term_to_string(coef, vars):
    if coef == 0:
        return ""
    
    var_str = ""
    for var, exp in sorted(vars.items()):
        if exp == 1:
            var_str += var
        else:
            var_str += f"{var}^{exp}"
    
    if coef == 1 and var_str:
        return var_str
    elif coef == -1 and var_str:
        return f"-{var_str}"
    else:
        return f"{coef}*{var_str}" if var_str else f"{coef}"

# Function to multiply multiple polynomials
def multiply_polynomials(polynomials):
    result_terms = {}
    
    # Start with the first polynomial
    result_terms = {(): 1}  # Starting with 1, the neutral element for multiplication
    
    for poly in polynomials:
        poly_terms = parse_polynomial(poly)
        new_result_terms = {}
        
        for result_term in result_terms:
            for term in poly_terms:
                coef, vars = multiply_terms(term, term_to_string(result_terms[result_term], dict(result_term)))
                var_key = tuple(sorted(vars.items()))
                
                if var_key in new_result_terms:
                    new_result_terms[var_key] += coef
                else:
                    new_result_terms[var_key] = coef
        
        result_terms = new_result_terms
    
    result = ""
    for vars, coef in result_terms.items():
        term_str = term_to_string(coef, dict(vars))
        if term_str:
            if result and term_str[0] != "-":
                result += "+"
            result += term_str
    
    return result

# Main function to do p1
def polynomial_multiplication():
    input_str = input("Input the polynomials: ")
    
    # Remove the outer parentheses and split by the ")*("
    input_str = input_str[1:-1]
    polynomials = input_str.split(")(")
    
    # Multiply all the polynomials
    result = multiply_polynomials(polynomials)
    
    print(f"Output Result: {result}")

# call the function to do p1
polynomial_multiplication()
