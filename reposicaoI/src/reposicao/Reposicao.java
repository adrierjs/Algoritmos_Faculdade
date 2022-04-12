/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package reposicao;

/**
 *
 * @author jennyfer
 */
public class Reposicao {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Condicionador c1 = new Condicionador("Consul");

        c1.alterarTemp(1.8);
       
       
        
        System.out.println(c1.toString());
        
        Condicionador c2 = new Condicionador("LG");
        
        System.out.println(c2.toString());
        c2.aumentaTemp();
        System.out.println(c2.toString());
        c2.desligar();
       System.out.println(c2.toString());
       

    }

}
