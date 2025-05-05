package com.zipcodewilmington.danny_do_better_exercises;

import java.util.ArrayList;
import java.util.Scanner;

/**
 * Modified by kristofer 3/4/2024.
 */
public class StringUtilities {
    /**
     * @return `Hello World` as a string
     */
    public static String getHelloWorld() {

        return "Hello World";
    }

    /**
     * @param firstSegment a string to be added to
     * @param secondSegment a string to add
     * @return the concatenation of two strings, `firstSegment`, and `secondSegment`
     */
    public static String concatenation(String firstSegment, String secondSegment){
        return firstSegment.concat(secondSegment);
    }

    /**
     * @param firstSegment a string to be added to
     * @param secondSegment a string to add
     * @return the concatenation of an integer, `firstSegment`, and a String, `secondSegment`
     */
    public static String concatenation(int firstSegment, String secondSegment){

        return firstSegment + secondSegment;
    }

    /**
     * @param input a string to be manipulated
     * @return the first 3 characters of `input`
     */
    public static String getPrefix(String input){


        return input.substring(0, 3);
    }

    /**
     * @param input a string to be manipulated
     * @return the last 3 characters of `input`
     */
    public static String getSuffix(String input){
        int inputLength = input.length();
        return input.substring(inputLength - 3, inputLength);

    }

    /**
     * @param inputValue the value to be compared
     * @param comparableValue the value to be compared against
     * @return the equivalence of two strings, `inputValue` and `comparableValue`
     */
    public static Boolean compareTwoStrings(String inputValue, String comparableValue) {
        if (inputValue.equals(comparableValue)) {
            return true;
        } return false;
    }


    /**
     * @param inputValue the value input from user
     * @return the middle character of `inputValue`
     */
    public static Character getMiddleCharacter(String inputValue){
//        int length = inputValue.length();
//        int middle = length / 2;
//        if (middle.length % 2 != 0) {
//        char middleChar = length.length((1/2) -1);
//        return middleChar;

        return null;
    }

    /**
     * @param spaceDelimitedString a string, representative of a sentence, containing spaces
     * @return the first sequence of characters
     */
    public static String getFirstWord(String spaceDelimitedString){

        String[] str = spaceDelimitedString.split(" ");
        String firstWord = str[0];
        return firstWord;



//        return null;
//        return words[0];

//        while (scanWords.hasNext()) {
//            words.add(scanWords.next());
//        } return words
    }

    /**
     * @param spaceDelimitedString a string delimited by spaces
     * @return the second word of a string delimited by spaces.
     */
    public static String getSecondWord(String spaceDelimitedString){
        String[] str = spaceDelimitedString.split(" ");
        String secondWord = str[1];
        return secondWord;
    }

    /**
     * @param stringToReverse
     * @return an identical string with characters in reverse order.
     */
    public static String reverse(String stringToReverse){
        String newString = new StringBuffer(stringToReverse).reverse().toString();
        return newString; 
    }
}
