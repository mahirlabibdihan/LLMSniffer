public class MyStringBuilder2 {
    private char[] value;
    private int count;

    public MyStringBuilder2() {
        value = new char[16];
        count = 0;
    }

    public MyStringBuilder2(char[] chars) {
        value = new char[chars.length + 16];
        System.arraycopy(chars, 0, value, 0, chars.length);
        count = chars.length;
    }

    public MyStringBuilder2(String s) {
        value = new char[s.length() + 16];
        s.getChars(0, s.length(), value, 0);
        count = s.length();
    }

    public MyStringBuilder2 insert(int offset, MyStringBuilder2 s) {
        if (offset < 0 || offset > count) {
            throw new StringIndexOutOfBoundsException(offset);
        }
        int newCount = count + s.length();
        if (newCount > value.length) {
            expandCapacity(newCount);
        }
        System.arraycopy(value, offset, value, offset + s.length(), count - offset);
        System.arraycopy(s.value, 0, value, offset, s.length());
        count = newCount;
        return this;
    }

    public MyStringBuilder2 reverse() {
        int len = length();
        for (int i = 0; i < len / 2; i++) {
            char temp = value[i];
            value[i] = value[len - i - 1];
            value[len - i - 1] = temp;
        }
        return this;
    }

    public MyStringBuilder2 substring(int begin) {
        if (begin < 0 || begin >= count) {
            throw new StringIndexOutOfBoundsException(begin);
        }
        return new MyStringBuilder2(value, begin, count - begin);
    }

    public MyStringBuilder2 toUpperCase() {
        for (int i = 0; i < count; i++) {
            if (Character.isLowerCase(value[i])) {
                value[i] = Character.toUpperCase(value[i]);
            }
        }
        return this;
    }

    public int length() {
        return count;
    }

    public char charAt(int index) {
        if (index < 0 || index >= count) {
            throw new StringIndexOutOfBoundsException(index);
        }
        return value[index];
    }

    public String toString() {
        return new String(value, 0, count);
    }

    private void expandCapacity(int minimumCapacity) {
        int newCapacity = value.length * 2 + 2;
        if (newCapacity < 0) {
            newCapacity = Integer.MAX_VALUE;
        } else if (minimumCapacity > newCapacity) {
            newCapacity = minimumCapacity;
        }
        char[] newValue = new char[newCapacity];
        System.arraycopy(value, 0, newValue, 0, count);
        value = newValue;
    }

    private MyStringBuilder2(char[] value, int offset, int count) {
        this.value = value;
        this.count = count;
    }
}
