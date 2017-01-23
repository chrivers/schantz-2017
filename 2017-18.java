X=Y=0;
for (c:"ἢ䉃䘩")
    for (;c % 16 * 6 >= Y; X += c + X / 118)
        print(2016 + Y++ + "	" + X);
