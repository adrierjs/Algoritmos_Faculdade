/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package banco;

import java.util.Scanner;

/**
 *
 * @author LL
 */
public class Principal {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Lista controle = new Lista();
        int op = 0;
        ContaCorrente cc = new ContaCorrente();
        ContaPoupanca cp = new ContaPoupanca();
        Pessoa p1 = new Pessoa();
        Pessoa p2 = new Pessoa();
        while (op != 5) {
            System.out.println("COMANDOS:\n1 - Add Cliente\n2 - Imprimir lista de clientes\n3 - Transferir valor\n4 - Excluir cliente\n5 - Para sair do programa");
            op = sc.nextInt();
            switch (op) {
                case 1:
                    int op2;
                    System.out.println("Digite:\n1 - Add Conta corrente\n2 - Add Conta poupança");
                    op2 = sc.nextInt();
                    if (op2 == 1) {

                        System.out.print("Digite a agencia: ");
                        int agencia = sc.nextInt();
                        System.out.print("Digite o numero da conta: ");
                        int numero = sc.nextInt();
                        System.out.print("Digite o saldo: ");
                        float saldo = sc.nextFloat();
                        System.out.print("Digite seu nome: ");
                        String nome = sc.next();
                        System.out.print("Digite a identidade: ");
                        int identidade = sc.nextInt();
                        System.out.print("Digite o limite que deseja: ");
                        float limite = sc.nextFloat();

                        p1.setNome(nome);
                        p1.setIdentidade(identidade);
                        cc.setAgencia(agencia);
                        cc.setNum(numero);
                        cc.setSaldo(saldo);
                        cc.setDono(p1);
                        cc.setLimite(limite);

                        //Pessoa p1 = new Pessoa(nome, identidade);                 
                        //ContaCorrente cc = new ContaCorrente(agencia,numero,saldo,p1,limite);
                        controle.addConta(cc);
                        //controle.addConta(new ContaCorrente(agencia,numero,saldo,p1,limite)); 

                    } else if (op2 == 2) {
                        System.out.print("Digite a agencia: ");
                        int agencia = sc.nextInt();
                        System.out.print("Digite o numero da conta: ");
                        int numero = sc.nextInt();
                        System.out.print("Digite o saldo: ");
                        float saldo = sc.nextFloat();
                        System.out.print("Digite seu nome: ");
                        String nome = sc.next();
                        System.out.print("Digite a identidade: ");
                        int identidade = sc.nextInt();
                        System.out.print("Digite a variação: ");
                        int variacao = sc.nextInt();

                        p2.setNome(nome);
                        p2.setIdentidade(identidade);
                        cp.setAgencia(agencia);
                        cp.setNum(numero);
                        cp.setSaldo(saldo);
                        cp.setDono(p2);
                        cp.setVariacao(variacao);
                        //Pessoa p2 = new Pessoa(nome, identidade);
                        //ContaCorrente cp = new ContaCorrente(agencia,numero,saldo,p1,variacao);
                        controle.addConta(cp);
                    } else {
                        System.out.println("Opção incorreta, tente novamente!");
                    }
                    break;
                case 2:
                    controle.imprimirClientes();
                    break;
                case 3:
                    int op3;
                    System.out.println("Digite:\n1 - Transferir da conta corrente para conta poupança\n2 - Transferir da conta poupança para conta corrente");
                    op3 = sc.nextInt();
                    if (op3 == 1) {
                        System.out.print("Digite o valor que deseja transferir: ");
                        cc.transferir(sc.nextInt(), cp);
                    } else if (op3 == 2) {
                        System.out.print("Digite o valor que deseja transferir: ");
                        cp.transferir(sc.nextInt(), cc);
                    } else {
                        System.out.print("ERRO, tente novamente!");
                    }
                    break;
                case 4:
                    int op4;
                    System.out.print("Digite o numero da conta que deseja excluir: ");
                    op4 = sc.nextInt();
                    controle.excluirCliente(op4);
                    break;

                case 5:
                    System.out.println("Programa encerrado!!!");
                    break;
                default:
                    break;
            }

        }
    }
}
