public class JavaGenerics {
    public static void main(String[] args) {
	System.out.println("Generics");
// from this page:
// http://en.wikipedia.org/wiki/Generics_in_Java

// without generics
	List v = new ArrayList();
	v.add("test");
	Integer i = (Integer)v.get(0);        // Run time error

// with generics
	List<String> v = new ArrayList<String>();
	v.add("test");
	Integer i = v.get(0); // (type error)  Compile time error
    }
}
