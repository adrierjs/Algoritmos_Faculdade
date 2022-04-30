package banco;

/**
 *
 * @author LL
 */
public interface IConta {

    public static double TAXAP = 0.05;
    public static double TAXACC = 0.0;

    void sacar(double valor);

    void depositar(double valor);

    void transferir(double valor, Conta contaDestino);

    void imprimir();

}
