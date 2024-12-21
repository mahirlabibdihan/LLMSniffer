private static void processOperator(Stack<Integer> operandStack, Stack<Character> operatorStack) {
    char op = operatorStack.pop();
    int op1 = operandStack.pop();
    int op2 = operandStack.pop();
    if (op == '+') {
        operandStack.push(op2 + op1);
    } else if (op == '-') {
        operandStack.push(op2 - op1);
    } else if (op == '*') {
        operandStack.push(op2 * op1);
    } else if (op == '/') {
        if (op1 == 0) {
            System.out.println("Error: division by zero");
            return;
        }
        operandStack.push(op2 / op1);
    }
}

    