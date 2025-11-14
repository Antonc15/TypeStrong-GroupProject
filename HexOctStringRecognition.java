import java.util.Scanner;

public class HexOctStringRecognition
{
    private static String runtimeEntry = "";

    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String userInput = input.nextLine();

        boolean valid = isInputValidHexOrOct(userInput);

        if (valid)
        {
            System.out.print("Your string is a valid Integer, Octinteger, or Hexinteger!");
        }
        else
        {
            System.out.print("Your string is NOT a valid Integer, Octinteger, or Hexinteger!");
        }

        input.close();
    }

    private static boolean isInputValidHexOrOct(String entry)
    {
        runtimeEntry = entry;
        return start(0);
    }

    private static boolean start(int i)
    {
        return q1(i) || q6(i) || q8(i);
    }

    private static boolean q1(int i)
    {
        if (isLastChar(i)) { return false; }
        char c = getChar(i);
        if (isChar(c, "0"))
        {
            return q2(i + 1);
        }
        return false;
    }

    private static boolean q2(int i)
    {
        if (isLastChar(i)) { return false; }
        char c = getChar(i);
        if (isChar(c, "0"))
        {
            return q3(i + 1);
        }
        return false;
    }

    private static boolean q3(int i)
    {
        if (isLastChar(i)) { return false; }
        char c = getChar(i);
        if (isChar(c, "_"))
        {
            return q5(i + 1);
        }
        if (isChar(c, "01234567"))
        {
            return q4(i + 1);
        }
        return false;
    }

    private static boolean q4(int i)
    {
        if (isLastChar(i)) { return Accept(i); }
        char c = getChar(i);
        if (isChar(c, "_"))
        {
            return q5(i + 1) || Accept(i);
        }
        if (isChar(c, "01234567"))
        {
            return q4(i + 1) || Accept(i);
        }
        return false;
    }

    private static boolean q5(int i)
    {
        if (isLastChar(i)) { return false; }
        char c = getChar(i);
        if (isChar(c, "01234567"))
        {
            return q4(i + 1);
        }
        return false;
    }

    private static boolean q6(int i)
    {
        if (isLastChar(i)) { return false; }
        char c = getChar(i);
        if (isChar(c, "0123456789"))
        {
            return q7(i + 1);
        }
        return false;
    }

    private static boolean q7(int i)
    {
        if (isLastChar(i)) { return Accept(i); }
        char c = getChar(i);
        if (isChar(c, "0123456789"))
        {
            return q7(i + 1) || Accept(i);
        }
        if (isChar(c, "_"))
        {
            return q6(i + 1) || Accept(i);
        }
        return false;
    }

    private static boolean q8(int i)
    {
        if (isLastChar(i)) { return false; }
        char c = getChar(i);
        if (isChar(c, "0"))
        {
            return q9(i + 1);
        }
        return false;
    }

    private static boolean q9(int i)
    {
        if (isLastChar(i)) { return false; }
        char c = getChar(i);
        if (isChar(c, "x"))
        {
            return q10(i + 1);
        }
        return false;
    }

    private static boolean q10(int i)
    {
        if (isLastChar(i)) { return false; }
        char c = getChar(i);
        if (isChar(c, "_"))
        {
            return q11(i + 1);
        }
        if (isChar(c, "0123456789ABCDEFabcdef"))
        {
            return q12(i + 1);
        }
        return false;
    }

    private static boolean q11(int i)
    {
        if (isLastChar(i)) { return false; }
        char c = getChar(i);
        if (isChar(c, "0123456789ABCDEFabcdef"))
        {
            return q12(i + 1);
        }
        return false;
    }

    private static boolean q12(int i)
    {
        if (isLastChar(i)) { return Accept(i); }
        char c = getChar(i);
        if (isChar(c, "0123456789ABCDEFabcdef"))
        {
            return q12(i + 1) || Accept(i);
        }
        if (isChar(c, "_"))
        {
            return q11(i + 1) || Accept(i);
        }
        return false;
    }

    private static boolean Accept(int i)
    {
        return (runtimeEntry != null) && (i >= runtimeEntry.length());
    }

    private static boolean isLastChar(int i)
    {
        return (runtimeEntry == null) || (i >= runtimeEntry.length());
    }

    private static char getChar(int i)
    {
        return runtimeEntry.charAt(i);
    }

    private static boolean isChar(char c, String compatible)
    {
        if (compatible == null)
        {
            return false;
        }
        for (int k = 0; k < compatible.length(); k++)
        {
            if (c == compatible.charAt(k))
            {
                return true;
            }
        }
        return false;
    }
}