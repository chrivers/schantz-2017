X=0;Y=16;
for (c:"\u4f1d\ua823\ub247")
    for (;Y < (c&0xFF); X += (c >> 8) * 100)
        print(2e3 + Y++ + "	" + (X += X / 118));
