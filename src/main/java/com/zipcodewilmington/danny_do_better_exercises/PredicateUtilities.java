package com.zipcodewilmington.danny_do_better_exercises;

/**
 * Modified by kristofer 3/4/2024.
 */
public class PredicateUtilities {
    /**
     * @param x
     * @param y
     * @return true if `x` is greater than `y`
     */
    public Boolean isGreaterThan(int x, int y) {
        Boolean isGreater = false;
        if(x > y)
        {
            isGreater = true;
        }

        return isGreater;
    }

    /**
     * @param x
     * @param y
     * @return true if `x` is less than `y`
     */
    public Boolean isLessThan(int x, int y) {
        Boolean isLesser = false;
        if(x < y)
        {
            isLesser = true;
        }

        return isLesser;
    }

    /**
     * @param x
     * @param y
     * @return true if `x` is greater than or equal to `y`
     */
    public Boolean isGreaterThanOrEqualTo(int x, int y) {
        Boolean isGreaterThanOrEqual = false;
        if(x >= y)
        {
            isGreaterThanOrEqual = true;
        }

        return isGreaterThanOrEqual;
    }

    /**
     * @param x
     * @param y
     * @return true if `x` is less than or equal to `y`
     */
    public Boolean isLessThanOrEqualTo(int x, int y) {
        Boolean isLesserThanOrEqual = false;
        if(x <= y)
        {
            isLesserThanOrEqual = true;
        }

        return isLesserThanOrEqual;
    }


    /**
     * @return true
     */
    public Boolean returnTrue() {
        return true;
    }

    /**
     * @return false
     */
    public Boolean returnFalse() {
        return false;
    }

}