/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package classes;

/**
 *
 * @author adrie
 */
public class Classes {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Carro c1 = new Carro("amarelo", "bmw", "rn-324");
        Lista lista = new Lista();
        
        
        lista.armazenarCarros(c1);
        lista.imprimirCarros();
        
     
       
       
        
    }    
}
