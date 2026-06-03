import java.util.*;
import java.util.Arrays;

class javaNotes {
        public static void main(String[] args) {
        //write your code here:
        	String str = "I am learning Java programming";
		int n = str.length();
		int spaceCount = 0;
		int l = 0;
		int max = 0;
		for(int i = 0; i <n; i++) {
			if (str.charAt(i) == ' ') {
				if (max < l) {
					max = l;
					
				}
			l = -1;
			}
			l++;
		}
		if (max < l) {
				max = l;
				l = -1;
		}
		System.out.println("The length of the longest word is: " + max);
	}
}
