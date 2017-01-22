I=0;X=0;Y=2016;
for (c:"\u4f0d\ua806\ub224") {
    for (I=0; I++ < (c&0xFF); Y++, X += (c >> 8) * 100) {
        print(Y + "	" + (X += X / 118));
    }
}
