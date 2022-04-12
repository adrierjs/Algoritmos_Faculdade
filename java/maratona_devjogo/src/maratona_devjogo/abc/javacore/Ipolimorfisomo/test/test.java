/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package maratona_devjogo.abc.javacore.Ipolimorfisomo.test;


import maratona_devjogo.abc.javacore.Ipolimorfisomo.classes.Gerente;
import maratona_devjogo.abc.javacore.Ipolimorfisomo.classes.RelatorioPagamento;
import maratona_devjogo.abc.javacore.Ipolimorfisomo.classes.Vendedor;

/**
 *
 * @author adrie
 */
public class test {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Gerente g = new Gerente("Adrier", 5000, 2000);
        Vendedor v = new Vendedor("José", 2000, 20000);
//        RelatorioPagamento relatorio = new RelatorioPagamento();
//        System.out.println("\n");
//        relatorio.reletorioPagamentoGerente(g);
//        relatorio.relatorioPagamentoVendedor(v);

     RelatorioPagamento relatorio = new RelatorioPagamento();
        System.out.println("\n");
        
        relatorio.relatorioPagamentoGenerico(v);
     
     

     
    }
}
