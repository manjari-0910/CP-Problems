// # Write the function fun_nth_additive_prime(n) that takes a non-negative int n
// # and returns the nth Additive Prime, which is a prime number such that
// # the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5
// # is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2


public class nthtenlyprime {

	public boolean isPrime(int n)
    {
        // Corner cases
        if (n <= 1)
            return false;
        if (n <= 3)
            return true;

        // This is checked so that we can skip
        // middle five numbers in below loop
        if (n % 2 == 0 || n % 3 == 0)
            return false;

        for (int i = 5; i * i <= n; i = i + 6)
            if (n % i == 0 || n % (i + 2) == 0)
                return false;

        return true;
    }

	public boolean istenlyprime(int n){
		int sum=0;
		while(n!=0){
			int rem=n%10;
			n=n/10;
			sum+=rem;
		}
		if (sum==10){
			return true;
		}
		return false;
	}

	public int fun_nthtenlyprime(int n){
		int i=2;
		int c=0;
		while (c<=n){
			if (isPrime(i) && istenlyprime(i)){
				c++;
			}
			i++;
		}
		return (i-1);
	}

	public static void main(String[] args) {

	}
}