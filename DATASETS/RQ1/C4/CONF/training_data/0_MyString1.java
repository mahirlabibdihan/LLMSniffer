public class MyString1 {
    private final char[] chars;

    public MyString1(char[] chars) {
        this.chars = chars.clone();
    }

    public char charAt(int index) {
        if (index < 0 || index >= chars.length) {
            throw new IndexOutOfBoundsException();
        }
        return chars[index];
    }

    public int length() {
        return chars.length;
    }

    public MyString1 substring(int begin, int end) {
        if (begin < 0 || end > chars.length || begin > end) {
            throw new IndexOutOfBoundsException();
        }
        char[] subChars = new char[end - begin];
        for (int i = begin; i < end; i++) {
            subChars[i - begin] = chars[i];
        }
        return new MyString1(subChars);
    }

    public MyString1 toLowerCase() {
        char[] lowerChars = new char[chars.length];
        for (int i = 0; i < chars.length; i++) {
            lowerChars[i] = Character.toLowerCase(chars[i]);
        }
        return new MyString1(lowerChars);
    }

    public boolean equals(MyString1 s) {
        if (s == null || s.chars.length != chars.length) {
            return false;
        }
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] != s.chars[i]) {
                return false;
            }
        }
        return true;
    }

    public static MyString1 valueOf(int i) {
        if (i == 0) {
            return new MyString1(new char[] {'0'});
        }
        int numDigits = (int) Math.ceil(Math.log10(i + 1));
        char[] digits = new char[numDigits];
        for (int j = numDigits - 1; j >= 0; j--) {
            digits[j] = (char) ('0' + i % 10);
            i /= 10;
        }
        return new MyString1(digits);
    }
}
