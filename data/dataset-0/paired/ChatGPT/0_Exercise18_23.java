public static int bin2Dec(String binaryString) {
    // Base case: the binary string is empty
    if (binaryString.isEmpty()) {
        return 0;
    }
    // Recursive case: compute the decimal value of the rest of the string
    int restValue = bin2Dec(binaryString.substring(1));
    // Multiply by 2 and add the current digit
    int currentValue = binaryString.charAt(0) == '1' ? 1 : 0;
    return currentValue + 2 * restValue;
}
