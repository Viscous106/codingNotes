public class lc {
	public static void main(String[] args) {
		int n=6;
		int[] arr = new int[n+1];
		for(int k=0;k<=n;k++){
			arr[k]=0;
			for(int i = 1;i*i<=k;i++){
				if(k%i==0){
					if(i==k/i)
						arr[k] += 1;
					else
						arr[k] += 2;
				}
		}
			System.out.print(arr[k]);
		}
	}
}

