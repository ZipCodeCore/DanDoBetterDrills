package com.zipcodewilmington.danny_do_better_exercises;

/**
 * Created by dan on 6/14/17.
 */
public class StringUtilities {
    /**
     * @return `Hello World` as a string
     */
    public static String getHelloWorld() {
       String helloWorld = "Hello World";

        return helloWorld;
    }

    /**
     * @param firstSegment a string to be added to
     * @param secondSegment a string to add
     * @return the concatenation of two strings, `firstSegment`, and `secondSegment`
     */
    public static String concatenation(String firstSegment, String secondSegment){

        return (firstSegment + secondSegment);
    }

    /**
     * @param firstSegment a string to be added to
     * @param secondSegment a string to add
     * @return the concatenation of an integer, `firstSegment`, and a String, `secondSegment`
     */
    public static String concatenation(int firstSegment, String secondSegment){
        //you're combining an int w/ a string = however you'll be returning a string because the method is calling for a string return.
        //Therefore you have to convert an int into a string. In order to combine them together.
        String stringFirstSegment = Integer.toString(firstSegment); //converting an int into a string - Integer.toString (static method) <- class method, used directy on the class Math.pow(); System.out.println().

        return concatenation (stringFirstSegment,secondSegment);
    }

    /**
     * @param input a string to be manipulated
     * @return the first 3 characters of `input`
     */
    public static String getPrefix(String input){
        //get the first 3 letters of the String input; input = inp;
        //

        return (input.substring(0,3));
    }

    /**
     * @param input a string to be manipulated
     * @return the last 3 characters of `input`
     */
    public static String getSuffix(String input){

        return input.substring(2,5);
    }

    /**
     * @param inputValue the value to be compared
     * @param comparableValue the value to be compared against
     * @return the equivalence of two strings, `inputValue` and `comparableValue`
     */
    public static Boolean compareTwoStrings(String inputValue, String comparableValue){
        //comparing two inputs to see if they are equivelent
        //using Boolean (true/false) to compare if they are the same

        return inputValue.equals(comparableValue);
    }

    /**
     * @param inputValue the value input from user
     * @return the middle character of `inputValue`
     */
    public static Character getMiddleCharacter(String inputValue){ //<-- method signature

        //.length is a property of String; and String is a non-primitive type or a class (because of the uppercase); .length
        int middleIndex = (inputValue.length()-1)/2;
        //-1 because the starting index is 0; it would that the total index length of inputValue minus by 1 position, divided by 2
        char ch = inputValue.charAt(middleIndex);
        //type variable is taking the inputValue.charAt(string method) returning the value of the middleIndex position of the letter that was in the string.
        return ch;
    }


    /**
     * @param spaceDelimitedString a string, representative of a sentence, containing spaces
     * @return the first sequence of characters
     */
    public static String getFirstWord(String spaceDelimitedString){
        //represents a sentence = example - the brown fox (w/ spaces)
        //return the first sequence of characters - return "the"
        //take the String input and make it into an array w/ a delimiter (specified in parathesis)that will remove the spaces. Then take the index position 0 (which represents the first word.)
        String noSpace[] = spaceDelimitedString.split(" "); //.split is a string method that allows you to specify what in the string you want to removes it.

        return noSpace[0];
    }

    /**
     * @param spaceDelimitedString a string delimited by spaces
     * @return the second word of a string delimited by spaces.
     */
    public static String getSecondWord(String spaceDelimitedString){
        //we are going to take the input and change it into an array, we will remove the spaces, and get the position 1 of the array.
        String noSpace[] = spaceDelimitedString.split(" ");

        return noSpace[1];
    }

    /**
     * @param stringToReverse
     * @return an identical string with characters in reverse order.
     */
    public static String reverse(String stringToReverse){
        //to change the input, into a character array and then reverse the indices
        //.toCharArray - representation of the each individual characters of the string, including spaces, and punctuation marks.
        char inputCharArray[] = stringToReverse.toCharArray(); // turning a string input into a char array
        //when returning a string length = total number of string (i.e. ford = 4 length) vs. indexes you will be returning the total position based on zero (i.e. ford = indices (0(f), 1(o), 2(r), 3(d))
        String results = "";
        for(int i = inputCharArray.length-1; i >= 0; i--){
            results = results + inputCharArray[i]; //containing the results of the for(loop) into the declared variable above is the same as results = results(not literal) (track previous number of the index) plus the for(loop)
        }
        //the for(loop) sets the condition for the charArray input, into the lenght(totalstring not indices) to start the count at the last index and continue to count backwards until its equal to zero.
        //i.e. FORD = 0123 start count at 3, 2, 1 , 0
        return results;
    }
}
