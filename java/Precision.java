public class Precision {
    public static void main(String[] args) {
	System.out.println("Precision");
	double n = 1;
	int i = 1;
	while (n > 0) {
	    System.out.printf("i:%4d n:%333.330f%n", i , n);
	    i++;
	    n = n / 2;
	}
    }
}
