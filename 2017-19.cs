int X, Y;
foreach (var c in "ἢ䉃䘩")
    for (;c % 16 * 6 >= Y; X += c + X/118)
        print($"20{Y+++16}	{X}")
