int X=0, Y=0;
foreach (char c in "ἢ䉃䘩")
    for (;c % 16 * 6 >= Y; X += c + X / 118)
        print(2016 + Y++ + "	" + X)