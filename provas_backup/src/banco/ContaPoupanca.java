package banco;

/**
 *
 * @author LL
 */
public class ContaPoupanca extends Conta {

    private int variacao;

    public ContaPoupanca() {
    }

    public ContaPoupanca(int agencia, int num, float saldo, Pessoa dono, int variacao) {
        super(agencia, num, saldo, dono);

        this.variacao = variacao;
    }

    public int getVariacao() {
        return variacao;
    }

    public void setVariacao(int variacao) {
        this.variacao = variacao;
    }
    

    @Override
    public double taxa() {
        return TAXAP;
    }

    @Override
    public String toString() {
        return """
               ----------------
               |Conta_Poupança|
               ----------------
               Usuário:\n """ + getDono() + "\nNumero: " + getNum() + "\nSaldo: " + getSaldo() + "\nAgencia: " + getAgencia() + "\nTaxa: "+ (TAXAP * 100)+ "%" + "\nVariação: " + this.variacao + "\n";
    }

}
