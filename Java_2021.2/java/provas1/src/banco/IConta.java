
package avaliacao1_u2;

/**
 *
 * @author LL
 */
public interface IConta {

    void sacar(double valor);

    void depositar(double valor);

    void transferir(double valor, Conta contaDestino);

    void imprimir();

}
