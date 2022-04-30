package banco;

/**
 *
 * @author LL
 */
public class ContaCorrente extends Conta {

    private float limite;

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

    public float getLimite() {
        return limite;
    }

    public void setLimite(float limite) {
        this.limite = limite;
    }

    @Override
    public String toString() {
        return """
               ----------------
               |Conta_Corrente|
               ----------------
               Usuário:\n """ + getDono() + "\nNumero: " + getNum() + "\nSaldo: " + getSaldo() + "\nTaxa: " + (TAXACC * 100) + "%"+ "\nAgencia: " + getAgencia() + "\nLimite: " + getLimite() + "\n";
    }

    /*@Override
    public void imprimir() {
        System.out.println("CONTA CORRENTE");
        super.imprimir();
        System.out.println("Limite: " + this.limite + "\n");
    }*/
}
