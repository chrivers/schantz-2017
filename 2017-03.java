interface A {
    static void main(String[]a) {
        float L = 0f;
        for (int Y = 2015; L < 1e6; Y++) {
            float I, r, P;
            I = 1e4f * (Y > 2027 ? 2 : 1);
            float X = L + I - (I * 0.1100f) - (L > 2e5 ? 0 : 1000);
            System.out.format("%d	%f\n", Y, L);
            L = 1.00847f * X;
       }
    }
}
