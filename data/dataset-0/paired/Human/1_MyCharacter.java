package ch_10.exercise10_24;


public class MyCharacter implements java.io.Serializable, Comparable<MyCharacter> {
    public static final char MIN_VALUE = '\u0000';
    public static final char MAX_VALUE = '\uFFFF';
    private final char value;

    static final MyCharacter[] cache = new MyCharacter[128];

    static {
        for (int i = 0; i < cache.length; i++)
            MyCharacter.cache[i] = new MyCharacter((char) i);
    }


    public MyCharacter() {
        value = MIN_VALUE;
    }

    public MyCharacter(char value) {
        this.value = value;
    }

    public static MyCharacter valueOf(char c) {
        if (c <= 127) {
            return MyCharacter.cache[(int) c];
        }
        return new MyCharacter(c);
    }

    public static MyCharacter valueOf(int i) {
        return new MyCharacter((char) i);
    }

    public char charValue() {
        return value;
    }

    public static boolean isLowerCase(char ch) {
        return ((int) ch) > 96 && ((int) ch) < 123;
    }

    public static boolean isDigit(char ch) {
        return ((int) ch) >= 48 && ((int) ch) <= 57;
    }

    public static boolean isUpperCase(char ch) {
        return ((int) ch) >= 65 && ((int) ch) <= 90;
    }

    public static boolean isLetter(char ch) {
        return ((int) ch) >= 65 && ((int) ch) <= 122;
    }

    public static boolean isLetterOrDigit(char ch) {
        return isLetter(ch) || isDigit(ch);
    }

    public static char toLowerCase(char ch) {
        return Character.toLowerCase(ch);
    }

    public static char toUpperCase(char ch) {
        return Character.toUpperCase(ch);
    }

    public static int compare(char x, char y) {
        return x - y;
    }

    @Override
    public int compareTo(MyCharacter anotherMyCharacter) {
        return compare(this.value, anotherMyCharacter.value);
    }

    @Override
    public int hashCode() {
        return MyCharacter.hashCode(value);
    }


    public static int hashCode(char value) {
        return (int) value;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof MyCharacter) {
            return value == ((MyCharacter) obj).charValue();
        }
        return false;
    }

    @Override
    public String toString() {
        char buf[] = {value};
        return String.valueOf(buf);
    }
}
