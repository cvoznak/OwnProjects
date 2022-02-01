package Ideas;

import java.util.Scanner;

/*
 * The idea is create a simple program to convert decimal numbers to binary and vice-versa, limited in 8 columns.
 */
public class DecimalBinary {

	public static int maxBinary(int column) {
		
		//Method to calculate maxim number possible to convert from decimal to binary when number of column was informed.
		
		int maxBinary = 0;
		
		for (int i = 0; i < column; i++ ) {
			maxBinary += Math.pow(2, i);
		}
		return maxBinary;
		
	}
	
	public static int[] binary(int decimal, int binaryColumns) {
		// Method to convert binary to decimal
		
		int [] bin = new int [binaryColumns];
		
		for (int i = (binaryColumns); i > 0; i--) {
			bin[((binaryColumns)-i)] = decimal / (int)Math.pow(2, (i - 1));
			
			decimal = decimal % (int)Math.pow(2, (i - 1));
		}
		return bin; 
	}
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int desire, binaryColumns, decimal;
		
		System.out.print("Do you desired convert binary to decimal (0) or decimal to binary (1): ");
		desire = sc.nextInt();
		
		if (desire == 0) {
			System.out.print("How many columns do you have to represent desired binary? ");
			binaryColumns = sc.nextInt();
			
			System.out.print("Which decimal do you wish convert to binary? ");
			decimal = sc.nextInt();
			
			if (decimal > DecimalBinary.maxBinary(binaryColumns)) {
				System.out.println("Sorry, maximal decimal possible to convert to binary with " + binaryColumns + " columns is " + DecimalBinary.maxBinary(binaryColumns));
			}
			
			else {		
				System.out.println();		
				for (int bin : DecimalBinary.binary(decimal, binaryColumns)) {
					System.out.print(bin + " ");
				}	
				
				int [] bin = new int [binaryColumns];
			
				bin = DecimalBinary.binary(decimal, binaryColumns);
			
				int decimalProof = 0;
			
				for (int i = 0; i < binaryColumns; i++) {
					decimalProof += bin[i] * Math.pow(2, ((binaryColumns - 1) - i));
				}
				System.out.println();
				System.out.println("\nBinary above is equivalent of " + decimalProof);
			}
			
			
			
		}
		
		else if (desire == 1) {
			
			int columns, decimalDesired = 0;
			
			System.out.print("How many columns you will type? ");
			columns = sc.nextInt();
			
			int [] binary = new int [columns];
			
			for (int i = 0; i < columns; i++) {
				System.out.print("Type 0 or 1: ");
				binary[i] = sc.nextInt();
				while (binary[i] != 1 && binary[i] != 0) {
					System.out.print("Invalid entry!\nPlease, type only 0 or 1: ");
					binary[i] = sc.nextInt();
				}
			}
			
			System.out.print("For binary ");		
			for (int bin : binary) {
				System.out.print(bin + " ");
			}	
			
			for (int i = 0; i < columns; i++) {
				decimalDesired += binary[i] * Math.pow(2, ((columns - 1) - i));
			}
			System.out.println("the equivalent decimal is " + decimalDesired);
			
		}
		else {
			System.out.println("Invalid entry!!!");
		}
		
		sc.close();
	}

}
