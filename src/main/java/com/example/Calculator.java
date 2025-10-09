package com.example;
import java.util.Scanner;

public class Calculator {

    public static double squareRoot(double x) {
        return Math.sqrt(x);
    }

    public static long factorial(int n) {
        if (n < 0) throw new IllegalArgumentException("Negative number");
        long result = 1;
        for (int i = 1; i <= n; i++) result *= i;
        return result;
    }

    public static double naturalLog(double x) {
        if (x <= 0) throw new IllegalArgumentException("Log undefined for non-positive numbers");
        return Math.log(x);
    }

    public static double power(double x, double b) {
        return Math.pow(x, b);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            System.out.println("\n==== Scientific Calculator ====");
            System.out.println("1. Square Root");
            System.out.println("2. Factorial");
            System.out.println("3. Natural Logarithm");
            System.out.println("4. Power");
            System.out.println("5. Exit");
            System.out.print("Enter choice: ");
            int choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter number: ");
                    double n1 = sc.nextDouble();
                    System.out.println("√" + n1 + " = " + squareRoot(n1));
                    break;
                case 2:
                    System.out.print("Enter integer: ");
                    int n2 = sc.nextInt();
                    System.out.println(n2 + "! = " + factorial(n2));
                    break;
                case 3:
                    System.out.print("Enter number: ");
                    double n3 = sc.nextDouble();
                    System.out.println("ln(" + n3 + ") = " + naturalLog(n3));
                    break;
                case 4:
                    System.out.print("Enter base: ");
                    double base = sc.nextDouble();
                    System.out.print("Enter exponent: ");
                    double exp = sc.nextDouble();
                    System.out.println(base + "^" + exp + " = " + power(base, exp));
                    break;
                case 5:
                    System.out.println("Exiting...");
                    sc.close();
                    System.exit(0);
                default:
                    System.out.println("Invalid choice");
            }
        }
    }
}
