interface A {
    static void main(String[]a) {
        float Y = 16, X = 0;
        while (Y++ < 71) {
            System.out.format("20%f	%f\n", Y, X *= 1.00847);
            X -= X > 2e5 ? 0 : 1e3;
            X += Y > 29 ? 17800 : 8900;
        }
    }
}
