package provaII;

/**
 *
 * @author LL
 */
public abstract class Conta implements IConta {

    private int agencia;
    private int num;
    private double saldo, desconto, valorTaxa;
    private static Pessoa dono;
    public static double TAXAP = 0.05;
    public static double TAXACC = 0.0;

    public Conta() {
        this.num = 0;
        this.saldo = 0;
        this.agencia = 0;
        this.dono = new Pessoa();

    }

    public Conta(int agencia, int num, double saldo, Pessoa dono) {
        this.agencia = agencia;
        this.num = num;
        this.saldo = saldo;
        this.dono = dono;
    }

    public Conta(double saldo) {
        this.saldo = saldo;
    }
    
    public abstract double taxa();

    public static double getTAXAP() {
        return TAXAP;
    }

    public static double getTAXACC() {
        return TAXACC;
    }

    @Override
    public void sacar(double valor) {
        this.valorTaxa = valor * taxa();
        desconto = valor + valorTaxa;
        this.saldo = saldo - desconto;

    }

    @Override
    public void depositar(double valor) {
        this.saldo = valor + saldo;
    }

    @Override
    public void transferir(double valor, Conta contaDestino) {
        this.sacar(valor);
        contaDestino.depositar(valor);
    }

    public int getAgencia() {
        return agencia;
    }

    public void setAgencia(int agencia) {
        this.agencia = agencia;
    }

    public Pessoa getDono() {
        return dono;
    }

    public void setDono(Pessoa dono) {
        this.dono = dono;
    }

    public int getNum() {
        return num;
    }

    public void setNum(int num) {
        this.num = num;
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

  
    

    @Override
    public String toString() {
        return "Conta" + 
                "agencia=" + 
                agencia + 
                ", num=" + 
                num + ", saldo="
                + saldo + ", dono="
                + dono;
    }

    @Override
    public void imprimir() {
        System.out.println(dono + "\nAgencia: " + agencia + "\nNúmero: " + num + "\nSaldo: " + saldo);

    }

}
