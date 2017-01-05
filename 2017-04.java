interface A {
    static void main(String[]a) {
        float X = 0;
        for (int Y = 0; Y < 70; Y++) {
            System.out.format("%d	%f\n", Y+2016, X *= 1.00847f);
            X += (1e4f * (Y > 12 ? 2 : 1) * 0.89f) - (X > 2e5 ? 0 : 1e3);
        }
    }
}
