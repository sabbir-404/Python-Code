def arithmetic(data):
    def _factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * _factorial(n - 1)
    
    def evaluate_factorials(expr):
        result = []
        i = 0
        while i < len(expr):
            if expr[i] == '!':
                num = result.pop()
                while i < len(expr) and expr[i] == '!':
                    num = _factorial(num)
                    i += 1
                result.append(num)
            else:
                result.append(int(expr[i]) if expr[i].isdigit() else expr[i])
                i += 1
        return result
    
    def evaluate_expression(expr):
        stack = []
        num = 0
        sign = '+'
        
        i = 0
        while i < len(expr):
            if isinstance(expr[i], int):
                num = expr[i]
            if i == len(expr) - 1 or expr[i] in "+x":
                if sign == '+':
                    stack.append(num)
                elif sign == 'x':
                    stack.append(stack.pop() * num)
                sign = expr[i]
                num = 0
            i += 1
        
        return sum(stack)
    
    # Step 1: Evaluate factorials
    data = evaluate_factorials(data)
    
    # Step 2: Evaluate multiplications and additions
    result = evaluate_expression(data)
    
    return result

print(arithmetic('4+3x3!'))
