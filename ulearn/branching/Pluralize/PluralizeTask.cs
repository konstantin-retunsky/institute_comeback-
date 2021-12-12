using System;

namespace Pluralize
{
  public static class PluralizeTask
  {
    public static string PluralizeRubles(int count)
    {
      string countString = count.ToString();
      string lastTwoSymbol = count >= 10
        ? countString.Substring(countString.Length - 2, 2)
        : $"0{count}";

      if (count == 10)
      {
        Console.WriteLine(10);
      }

      if (
        lastTwoSymbol[1] == '0' ||
        lastTwoSymbol[1] == '5' ||
        lastTwoSymbol[1] == '6' ||
        lastTwoSymbol[1] == '7' ||
        lastTwoSymbol[1] == '8' ||
        lastTwoSymbol[1] == '9' ||
        lastTwoSymbol == "11" ||
        lastTwoSymbol == "12" ||
        lastTwoSymbol == "13" ||
        lastTwoSymbol == "14"
      )
        return "рублей";
      else if (
        lastTwoSymbol[1] == '1'
      )
        return "рубль";
      else
        return "рубля";
    }
  }
}