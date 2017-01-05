interface A {
    static void main(String[]a) {
        float Rn = 0f;
        float L = 0f;
        for (int Y = 2016; L < 1e6; Y++) {
            L = Rn;
            float I, Opct, r, P;
            I = 1e4f * (Y >= 2029 ? 2 : 1);
            Opct = I * 0.1100f;
            float X = L + I - Opct - (L > 2e5 ? 0 : 1000);
            Rn = 1.00847f * X;
            System.out.format("%d	%f\n", Y, L);
       }
    }
}
