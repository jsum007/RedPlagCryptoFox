import java.util.*;
 
public class Halk{
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		String s = "";
		for (int i =1; i < n; i++){
 
		if (i % 2 == 1){
			s += "I hate that ";
		}else if (i % 2 == 0){
		    s += "I love that ";
		}
	}
		if (n % 2 == 1){
			s += "I hate it";
		}else if (n % 2 == 0){
			s += "I love it";
		}
		if (n == 1){
			System.out.println("I hate it");
		}else{
		System.out.println(s);
		}
	}
 
}