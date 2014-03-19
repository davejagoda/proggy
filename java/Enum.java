public class Enum {
    public enum Dir { 北, 南, 東, 西 }
    public static void main(String[] args) {
	System.out.println(java.util.Arrays.asList(Dir.values()));
    }
}
