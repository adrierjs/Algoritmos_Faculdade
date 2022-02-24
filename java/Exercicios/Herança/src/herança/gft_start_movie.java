/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package herança;

import java.io.IOException;
import java.util.Scanner;


	
    public class gft_start_movie  {
    public static void main(String[]args) throws IOException {
        Scanner leitor = new Scanner(System.in);
        double A = leitor.nextDouble();
        double B = leitor.nextDouble();
        System.out.printf("%.2f%%%n", (B/A - 1)* 100);
        leitor.close();   
    }
	
}