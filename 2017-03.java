interface A {
    static void main(String[]a) {
        float Rn = 0f;
        float L = 0f;
        for (int Y = 2016; L < 1e6; Y++) {
            L = Rn;
            float I, A, Opct, r, P;
            if (Y >= 2029) {
                I = 2e4f;
            } else {
                I = 1e4f;
            }
            Opct = I * 0.1100f;
            if (L > 2e5) {
                A = 0;
            } else {
                A = 1000;
            }
            float X = L + I - Opct - A;
            float Z = 0.01f * X;
            Rn = X + 0.847f * Z;
            System.out.format("%d	%f\n", Y, L);
       }
    }
}
