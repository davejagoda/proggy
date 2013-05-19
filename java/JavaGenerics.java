import java.util.ArrayList;
import java.util.List;

public class JavaGenerics {
    public static void main(String[] args) {
	System.out.println("Generics, in main");
	WithoutGenerics();
	WithGenerics();
	System.out.println("Generics, about to finish");
    }
// from this page:
// http://en.wikipedia.org/wiki/Generics_in_Java

// without generics
    public static void WithoutGenerics() {
	System.out.println("Generics, in WithoutGenerics");
	List v = new ArrayList();
	v.add("test");
// uncomment the next line to get the runtime error
//	Integer i = (Integer)v.get(0);        // Run time error
    }

// with generics
    public static void WithGenerics() {
	System.out.println("Generics, in WithGenerics");
	List<String> v = new ArrayList<String>();
	v.add("test");
// uncomment the next line to get the compile time error
//	Integer i = v.get(0); // (type error)  Compile time error
    }
}
