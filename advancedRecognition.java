import java.util.Scanner;

public class advancedRecognition
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String userInput = input.nextLine();

        if (isInputValidHexOrOct(userInput))
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
        return start(entry);
    }

    private static boolean start(String remainder)
    {
        if (entry.length() <= 0)
        {
            return false;
        }

        // State q0 logic goes here
        return false;
    }

    private static boolean q1(String remainder)
    {
        if (entry.length() <= 0)
        {
            return false;
        }

        // State q1 logic goes here
        return false;
    }

    private static boolean q2(String remainder)
    {
        if(entry.length() <= 0)
        {
            return false;
        }

        // State q2 logic goes here
        return false;
    }

    private static boolean q3(String remainder)
    {
        if(entry.length() <= 0)
        {
            return false;
        }

        // State q3 logic goes here
        return false;
    }

    private static boolean q4(String remainder)
    {
        if(entry.length() <= 0)
        {
            return false;
        }

        // State q4 logic goes here
        return false;
    }

    private static boolean q5(String remainder)
    {
        if(entry.length() <= 0)
        {
            return false;
        }

        // State q5 logic goes here
        return false;
    }

    private static boolean q6(String remainder)
    {
        if(entry.length() <= 0)
        {
            return false;
        }

        // State q6 logic goes here
        return false;
    }

    private static boolean q7(String remainder)
    {
        if(entry.length() <= 0)
        {
            return false;
        }

        // State q7 logic goes here
        return false;
    }

    private static boolean q8(String remainder)
    {
        if(entry.length() <= 0)
        {
            return false;
        }

        // State q8 logic goes here
        return false;
    }

    private static boolean q9(String remainder)
    {
        if(entry.length() <= 0)
        {
            return false;
        }

        // State q9 logic goes here
        return false;
    }

    private static boolean q10(String remainder)
    {
        if(entry.length() <= 0)
        {
            return false;
        }

        // State q10 logic goes here
        return false;
    }

    private static boolean q11(String remainder)
    {
        if(entry.length() <= 0)
        {
            return false;
        }

        // State q11 logic goes here
        return false;
    }

    private static boolean q12(String remainder)
    {
        if(entry.length() <= 0)
        {
            return false;
        }

        // State q12 logic goes here
        return false;
    }

    private static boolean q13(String remainder)
    {
        if(entry.length() <= 0)
        {
            return false;
        }

        // State q13 logic goes here
        return false;
    }

    private static boolean Accept(String remainder)
    {
        if(entry.length() <= 0)
        {
            return true;
        }

        // State q14 logic goes here
        return false;
    }
}