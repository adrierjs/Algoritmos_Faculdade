/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package maratona_devjobo.br.com.abc.javacore.Fmodificadorestatico.test;

import maratona_devjobo.br.com.abc.javacore.Fmodificadorestatico.classes.Carro;



/**
 *
 * @author adrie
 */
public class CarroTest {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Carro c1 = new Carro("BMW", 220);
        Carro c2 = new Carro("Audi", 280);
        Carro c3 = new Carro("Mercedes", 255);
        
        c1.imprime();
        c2.imprime();
        c3.imprime();
        
        System.out.println("############");
        
        Carro.setVelocidadeLimite(220.5);
        c1.imprime();
        c2.imprime();
        c3.imprime();
        
    }
    
}
