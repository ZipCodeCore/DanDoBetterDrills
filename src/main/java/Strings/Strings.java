package Strings;

import com.sun.tools.doclets.formats.html.SourceToHTMLConverter;

/**
 * Created by dan on 6/14/17.
 */
public class Strings {

    //Concatenate two strings together that are passed in the parameters
    public String concatenation(String one, String two){
        return one + two;
    }

    //Concatenate a string and a integer together that are passed in the parameters
    public String concatenation(int one, String two){
        return one + two;
    }

    //Get the substring of the first three letters of a string
    public String subStringBegin(String input){
        String newInput = input.substring(0, 3);
        return newInput;
    }

    //Get the substring of a string "Hello" so it returns the last three letters only
    public String subStringEnd(String input) {
        String newInput = input.substring(input.length()-3, input.length());
        return newInput;
    }

    //Compare the two strings using compareTo() and if they are return true, else false
    public boolean compareTwoStrings(String one, String two){
        if (one.compareTo(two) == 0) {
            return true;
        }
        return false;
    }

    //Compare the two strings using equals() and if they are return true, else false
    public boolean compareTwoStringsEqual(String one, String two){
        if (one.equals(two)) {
            return true;
        }
        return false;
    }

    //Write a method that returns the middle character in the given string hint: use the .length and .charAt methods
    public char getTheMiddleChar(String string) {
    char newString = string.charAt(string.length()/2);
    return newString;
    }

    //Use the indexOf method to find the first space in a string and .substring() to return the first word
    public String getTheFirstWord(String string){
        String firstWord = string.substring(0, string.indexOf(" "));
        return firstWord;
    }

    //Use the same behavior to find the second word
    public String getTheSecondWord(String string) {
        String secondWord[] = string.split((" "));
       return secondWord[1];
    }

    //Create a method that uses the above methods to return a string consisting of the second and first word in reversed order
    public String reverseTheTwo(String string) {
        String reversedString = getTheSecondWord(string) + " " + getTheFirstWord(string);
        return reversedString;
    }

}
