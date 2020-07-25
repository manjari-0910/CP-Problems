// # Write the function longestSubpalindrome(s), that takes a string s and returns
// the longest palindrome that occurs as consecutive characters (not just letters, but
// 	any characters) in s. So:
// #    	longestSubpalindrome("ab-4-be!!!")
// # returns "b-4-b". If there is a tie, return the lexicographically larger value --
// in java, a string s1 is lexicographically greater than a string s2 if (s1 > s2). So:
// #    	longestSubpalindrome("abcbce")
// # returns "cbc", since ("cbc" > "bcb"). Note that unlike the previous functions,
// this function is case-sensitive (so "A" is not treated the same as "a" here). Also,
// from the explanation above, we see that longestSubpalindrome("aba") is "aba",
// and longestSubpalindrome("a") is "a".
import java.util.*;

class longestsubpalindromes {

	public Object[] substring(String a){
		ArrayList<String>al=new ArrayList<String>();
		int i=0;
		int k=0;
		while(i<a.length()){
		    int j=0;
		    while (i+j<=a.length()){
    		    if (a.substring(i,i+j).length()>0){
    		      //  sarr[k++]=a.substring(i,i+j);
    		        al.add(a.substring(i,i+j));
		        }
		        j++;
		    }
		    i++;
		}
		Object [] sarr=al.toArray();
		return sarr;
	}

	public String fun_longestsubpalindromes(String s){
		Object[] sarr=substring(s);
		int l=0;
		String word="";
		for (int i=0;i<sarr.length;i++){
		    String part=(String)sarr[i];
			StringBuilder sb=new StringBuilder(part);
			StringBuilder rev=sb.reverse();
			if (part.equals(rev.toString())){
				if (part.length()>=l){
					l=part.length();
					word=(String)sarr[i];
				}
			}
		}
		return word;
	}

	public static void main(String[] args) {

	}
}
