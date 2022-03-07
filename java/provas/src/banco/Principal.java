/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package banco;

/**
 *
 * @author LL
 */
public class Principal {

    public static void main(String[] args) {
        Pessoa p = new Pessoa("Adrier", 2222);
        Pessoa p2 = new Pessoa("Gabriel", 113221);
        Lista contas = new Lista();

        Conta cp = new ContaPoupanca(2210, 19038 - 1, 10000, p, 1, 51);

        ContaCorrente cc = new ContaCorrente(1999, 194324, 2000, p2, 10000);

        cp.transferir(10000, cc);
        //cc.imprimir();
        //cp.imprimir();
        contas.addConta(cc);
        //System.out.println(cc);
        contas.addConta(cp);
        //System.out.println(cp);
        
        //imprimir.contas;
        contas.imprimir();

    }

}
