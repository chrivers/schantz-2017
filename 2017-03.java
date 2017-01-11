interface C {
    static void main(String[]a) {
        float L = 0f;
        float X = 0;
        float Q = 0;
        for (int Y = 2015; Q < 1e6; Y++) {
            L = 1.00847f * X;
            float I, r, P;
            I = 1e4f * (Y > 2027 ? 2 : 1);
            X = L + I - (I * 0.1100f) - (L > 2e5 ? 0 : 1000);
            System.out.format("%d	%f\n", Y, L);
            Q = L;
    }
    }
}
