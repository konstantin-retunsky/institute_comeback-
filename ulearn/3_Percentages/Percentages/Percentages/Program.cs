using System;
using System.Text.RegularExpressions;

namespace Percentages
{
  class Program
  {
    static void Main(string[] args)
    {
      Console.WriteLine(Calculate("100.00 12 1"));
      Console.WriteLine(Calculate("100.00 12 12"));
    }

    public static double Calculate(string userInput)
    {
      string[] inputData = Regex.Split(userInput ?? String.Empty, @"\s");

      if (inputData.Length != 3)
      {
        return 0;
      }

      double amount = Convert.ToDouble(inputData[0]);
      double percentages = Convert.ToDouble(inputData[1]);
      int months = Convert.ToInt32(inputData[2]);

      return amount * Math.Pow(1 + (percentages / 100 / 12), months);
    }
  }
}