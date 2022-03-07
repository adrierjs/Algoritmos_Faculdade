package banco;

/**
 *
 * @author LL
 */
public class ContaPoupanca extends Conta {

    private float taxa;
    private int variacao;

    public ContaPoupanca() {
        this.taxa = taxa;
    }

    public ContaPoupanca(int agencia, int num, float saldo, Pessoa dono, float taxa, int variacao) {
        super(agencia, num, saldo, dono);
        this.variacao = variacao;
        this.taxa = taxa;
    }

    public float getTaxa() {
        return taxa;
    }

    public void setTaxa(float taxa) {
        this.taxa = taxa;
    }

    public String toString() {
        return """
               ----------------
               |Conta_Poupança|
               ----------------
               Usuário:\n """ + dono + "\nNumero= " + num + "\nSaldo= " + saldo + "\nAgencia= " + agencia + "\nTaxa= " + taxa + "\nVariação= " + variacao +"\n";
    }

    /*@Override
    public void imprimir() {
        System.out.println("CONTA POUPANÇA");
        super.imprimir();
        System.out.println("Variação: " + variacao + "\nTaxa: " + taxa + "%\n");

    }*/

}
