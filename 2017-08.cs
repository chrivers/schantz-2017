        for (
            int Y = 15, X = 0;
            Y++ < 70;
            X += (Y > 28 ? Y > 34 ? 556 : 524 : 247) << 5
        ) Console.Write($"20{Y}	{X += X/118}\n")
