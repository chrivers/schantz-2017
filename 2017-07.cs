class P
{
    static void Main()
    {
        for (
            int Y = 15, X = 0;
            Y++ < 70;
            X += Y > 28 ? 524 + Y / 35 * 32 << 5 : 7904
        ) System.Console.Write($"20{Y}	{X += X/118}\n");
    }
}
