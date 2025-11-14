import java.util.Scanner;
import java.util.AbstractMap.SimpleEntry;

public class HexOctStringRecognition
{
    private static String runtimeEntry = "";

    public static void main(String[] args)
    {
        // Read string from user
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String userInput = input.nextLine();
        input.close();

        // Verify entry validity
        boolean valid = isInputValidHexOrOct(userInput); 

        if (valid)
        {
            System.out.print("Your string is a valid Octinteger or Hexinteger!");
        }
        else
        {
            System.out.print("Your string is NOT a valid Octinteger or Hexinteger!");
        }
    }

    private static boolean isInputValidHexOrOct(String entry)
    {
        runtimeEntry = entry;
        return start();
    }

    // Nodes
    private static boolean start(int i)
    {
        return q0(i) || q1(i) || q2(i);
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
            return q7(i + 1);
        }
        
        if (isChar(c, "01234567"))
        {
            return q4(i + 1);
        }

        return false;
    }

    private static boolean q4(int i)
    {
        if (isLastChar(i)) { return q14(i); }

        char c = getChar(i);

        if (isChar(c, "_"))
        {
            return q7(i + 1) || q14(i);
        }

        if (isChar(c, "01234567"))
        {
            return q4(i + 1) || q14(i);
        }

        return false;
    }

    private static boolean q5(int i)
    {
        if (isLastChar(i)) { return false; }

        char c = getChar(i);

        if (isChar(c, "0123456789"))
        {
            return q6(i + 1);
        }

        return false;
    }

    private static boolean q6(int i)
    {
        if (isLastChar(i)) { return q14(i); }

        char c = getChar(i);

        if (isChar(c, "0123456789"))
        {
            return q6(i + 1) || q14(i);
        }

        if (isChar(c, "_"))
        {
            return q5(i + 1) || q14(i);
        }

        return false;
    }

    private static boolean q7(int i)
    {
        if (isLastChar(i)) { return false; }

        char c = getChar(i);

        if (isChar(c, "01234567"))
        {
            return q4(i + 1);
        }

        return false;
    }

    private static boolean q8(int i)
    {
        if (isLastChar(i)) { return false; }

        // State q8 logic goes here
        return false;
    }

    private static boolean q9(int i)
    {
        if (isLastChar(i)) { return false; }

        // State q9 logic goes here
        return false;
    }

    private static boolean q10(int i)
    {
        if (isLastChar(i)) { return false; }

        // State q10 logic goes here
        return false;
    }

    private static boolean q11(int i)
    {
        if (isLastChar(i)) { return false; }

        // State q11 logic goes here
        return false;
    }

    private static boolean q12(int i)
    {
        if (isLastChar(i)) { return false; }

        // State q12 logic goes here
        return false;
    }

    private static boolean q13(int i)
    {
        if (isLastChar(i)) { return false; }

        // State q13 logic goes here
        return false;
    }

    private static boolean Accept(int i)
    {
        return true;
    }

    // Helpers
    private static boolean isLastChar(int i)
    {
        return (runtimeEntry == null) || (i >= runtimeEntry.length());
    }

    private static char getChar(int i)
    {
        if (s.length() <= 0)
        {
            return null;
        }

        char c = runtimeEntry.charAt(0);

        return new SimpleEntry<>(true, c);
    }

    private static boolean isChar(char c, String compatible)
    {
        if (compatible == null) 
        {
            return false;
        }

        for (int i = 0; i < compatible.length(); i++) 
        {
            if (c == compatible.charAt(i)) 
            {
                return true;
            }
        }

        return false;
    }
}