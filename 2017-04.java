interface A {
    static void main(String[]a) {
        float X = 0;
        for (int Y = 0; Y < 70; Y++) {
            System.out.format("%d	%f\n", Y+2016, X *= 1.00847f);
            X += 8900 * (Y > 12 ? 2 : 1) - (X > 2e5 ? 0 : 1e3);
        }
    }
}
