package provaII;

/**
 *
 * @author LL
 */
public class ContaCorrente extends Conta {

    private double limite;

    public ContaCorrente() {
        this.limite = 0;
    }

    public ContaCorrente(int agencia, int num, float saldo, Pessoa dono, float limite) {
        super(agencia, num, saldo, dono);
        this.limite = limite;
    }

    @Override
    public double taxa() {
        return TAXACC;
    }

    public double getLimite() {
        return limite;
    }

    public void setLimite(double limite) {
        this.limite = limite;
    }

    @Override
    public String toString() {
        return """
               ----------------
               |Conta_Corrente|
               ----------------
               Usuário:\n """ + getDono() + "\nNumero: " + getNum() + "\nSaldo: " + getSaldo() + "\nTaxa: " + (getTAXACC() * 100) + "%" + "\nAgencia: " + getAgencia() + "\nLimite: " + getLimite() + "\n";
    }

}
