public class lc {
	static void P(int n){
		System.out.print(n);
		if (n==1)
			return;	
		P(n-1);
	}
	public static void main(String[] args) {
		P(3);
	}
}

