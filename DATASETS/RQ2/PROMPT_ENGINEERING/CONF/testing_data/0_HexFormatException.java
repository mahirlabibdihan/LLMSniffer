public class HexConverter {

    public static void main(String[] args) {
        try {
            // Simulate hex string conversion
            String hexString = "1A3G"; // Invalid hex string
            int decimalValue = hex2Dec(hexString);
            System.out.println("Decimal value: " + decimalValue);
        } catch (HexFormatException e) {
            // Handle custom HexFormatException
            System.out.println("Error: " + e.getMessage());
        }
    }

    // Method to convert hex string to decimal
    private static int hex2Dec(String hexString) throws HexFormatException {
        int decimalValue = 0;

        // Validate hex string
        try {
            validateHexString(hexString);
        } catch (HexFormatException e) {
            throw e; // Re-throw the exception
        }

        // Convert hex string to decimal
        for (int i = hexString.length() - 1, power = 0; i >= 0; i--, power++) {
            char hexChar = hexString.charAt(i);
            int hexDigit = hexCharToDecimal(hexChar);
            decimalValue += hexDigit * Math.pow(16, power);
        }

        return decimalValue;
    }

    // Method to validate hex string
    private static void validateHexString(String hexString) throws HexFormatException {
        // Check for null or empty string
        if (hexString == null || hexString.isEmpty()) {
            throw new HexFormatException("Hex string cannot be null or empty");
        }

        // Check for valid hex characters
        for (char hexChar : hexString.toCharArray()) {
            if (!Character.isDigit(hexChar) && (hexChar < 'A' || hexChar > 'F') && (hexChar < 'a' || hexChar > 'f')) {
                throw new HexFormatException("Invalid hex character: " + hexChar);
            }
        }
    }

    // Method to convert hex character to decimal
    private static int hexCharToDecimal(char hexChar) {
        if (Character.isDigit(hexChar)) {
            return hexChar - '0';
        } else {
            return Character.toUpperCase(hexChar) - 'A' + 10;
        }
    }

    // Custom HexFormatException class
    static class HexFormatException extends Exception {
        public HexFormatException(String message) {
            super(message);
        }
    }
}
