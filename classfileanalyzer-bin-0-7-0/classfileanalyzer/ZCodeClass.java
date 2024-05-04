import java.lang.StringBuilder;

public class ZCodeClass {
    public static void writeNumber(float number) {
        System.out.print(number);
    }

    public static void writeString(String text) {
        System.out.print(text);
    }

    public static void writeBool(boolean value) {
        System.out.print(value);
    }

    public static String concatString(String s, String b) {
        StringBuilder sb = new StringBuilder();
        sb.append(s).append(b);
        return sb.toString();
    }

    public static float[][] a = {{1.0f, 2.0f}, {3.0f, 4.0f}};

    public static float b = 1.0f;

    public static void main(String[] args) {
        writeNumber(b);
        writeNumber(a[0][0]);
    }
}