import java.io.*;public class PrimeNumberGenerator {  public static void main(String[] args) {    long MAX_NUMBER = 10000000000L;    int PRIME_CHUNK_SIZE = 10000;    boolean[] isPrime = new boolean[(int)MAX_NUMBER];    isPrime[0] = false;    isPrime[1] = false;    