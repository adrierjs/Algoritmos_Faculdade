
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

    public float getLimite() {
        return limite;
    }

    public void setLimite(float limite) {
        this.limite = limite;
    }
    
    public String toString(){
        return """
               ----------------
               |Conta_Corrente|
               ----------------
               Usuário:\n """ + dono + "\nNumero= " + num + "\nSaldo= " + saldo + "\nAgencia= " + agencia + "\nLimite= " + limite +"\n";
    }

    /*@Override
    public void imprimir() {
        System.out.println("CONTA CORRENTE");
        super.imprimir();
        System.out.println("Limite: " + this.limite + "\n");
    }*/

}
