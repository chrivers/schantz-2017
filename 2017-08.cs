        for (
            int Y = 15, X = 0;
            Y++ < 70;
            X += (Y > 28 ? 524 + Y / 35 * 32 : 247) << 5
        ) print($"20{Y}	{X += X/118}")
