

public class ZCodeClass {

    public static float[][] a = {{1.0f, 2.0f}, {3.0f, 4.0f}};

    public static float b = 1.0f;

    public static void main(String[] args) {
        io.writeNumber(b);
        io.writeNumber(a[0][0]);
    }
}