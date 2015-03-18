import java.math.BigDecimal;

public class NewtonsMethodSquareRoot {
    public static void main(String...args) {
	if (1 != args.length) {
	    System.out.println("Please provide exactly one argument");
	    System.exit(1);
        }
	int scale = 1024;
	int roundingMode = BigDecimal.ROUND_FLOOR;
	BigDecimal TWO = new BigDecimal(2);
	BigDecimal CLOSE_ENOUGH = new BigDecimal("1.0E-100");
	BigDecimal argument = new BigDecimal(args[0]);
	BigDecimal guess = new BigDecimal(1);
	BigDecimal numerator, denominator, quotient;
	int i = 1;
	while (true) {
	    denominator = guess.multiply(TWO);
	    numerator = guess.multiply(guess).subtract(argument);
	    quotient = numerator.divide(denominator, scale, roundingMode);
	    guess = guess.subtract(quotient);
	    //	    System.out.println(guess);
	    //	    System.out.println(i);
	    if (guess.multiply(guess).subtract(argument).abs().compareTo(CLOSE_ENOUGH) <= 0) break;
	    i++;
	}
	System.out.println("converged after " + i + " iterations");
	System.out.println(guess);
    }
}
