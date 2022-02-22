/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package classes;

import java.util.ArrayList;

/**
 *
 * @author adrie
 */
public class Lista {
 private ArrayList<Carro> carro;
	
	public Lista() {
		carro=new ArrayList<Carro>();
	}
	
	public void armazenarCarros(Carro p) {
		this.carro.add(p);
	}
	
	public void imprimirCarros() {
		for(Carro p:this.carro) {
			System.out.println(p);
		}
	}
	
	

	
}
