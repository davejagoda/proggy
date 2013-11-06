import java.util.Arrays;

public class ArgsSort {
    public static void main(String...args) {
        System.out.println("raw\n");
        for (int i = 0; i < args.length; i++) {
            System.out.println(args[i]);
        }
        Arrays.sort(args);
        System.out.println("\nsorted\n");
        for (int i = 0; i < args.length; i++) {
            System.out.println(args[i]);
        }
    }
}
