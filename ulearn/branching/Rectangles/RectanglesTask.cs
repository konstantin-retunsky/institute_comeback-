using System;

namespace Rectangles
{
  public static class RectanglesTask
  {
    public static bool AreIntersected(Rectangle r1, Rectangle r2)
    {
      return Math.Min(r1.Bottom, r2.Bottom) >= Math.Max(r1.Top, r2.Top) &&
             Math.Min(r1.Right, r2.Right) >= Math.Max(r1.Left, r2.Left);
    }

    public static int IntersectionSquare(Rectangle r1, Rectangle r2)
    {
      int left = Math.Max(r1.Left, r2.Left);
      int right = Math.Min(r1.Right, r2.Right);
      int top = Math.Max(r1.Top, r2.Top);
      int bottom = Math.Min(r1.Bottom, r2.Bottom);

      int width = right - left;
      int height = bottom - top;

      if (width <= 0 || height <= 0)
        return 0;

      return width * height;
    }

    private static bool IsInside(Rectangle r1, Rectangle r2)
    {
      return r1.Left >= r2.Left && r1.Top >= r2.Top && r1.Right <= r2.Right && r1.Bottom <= r2.Bottom;
    }

    public static int IndexOfInnerRectangle(Rectangle r1, Rectangle r2)
    {
      if (IsInside(r1, r2))
        return 0;
      else if (IsInside(r2, r1))
        return 1;
      else
        return -1;
    }
  }
}