interface B {
    static void main(String[]a) {
        float Rn = 0.0f;
        float Rn_last = 0.0f;
        for (int year = 2016; Rn_last < 1e6; year++) {
            Rn_last = Rn;
            float I, Oabs, Opct, r, PAL;
            if (year >= 2029) {
                I = 20000;
            } else {
                I = 10000;
            }
            Opct = I * 0.1100f;
            if (Rn_last > 200000) {
                Oabs = 0;
            } else {
                Oabs = 1000;
            }
            r = 0.01f * (Rn_last + I - Opct - Oabs);
            PAL = 0.1530f * r;
            Rn = Rn_last + I - Opct - Oabs + r - PAL;
            System.out.format("%d	%f\n", year, Rn_last);
       }
    }
}
