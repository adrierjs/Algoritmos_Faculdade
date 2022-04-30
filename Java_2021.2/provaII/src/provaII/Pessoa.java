package provaII;

/**
 *
 * @author adrie
 */
public class Pessoa {

    private String nome;
    private int identidade;

    public Pessoa() {
    }

    public Pessoa(String nome, int identidade) {
        this.nome = nome;
        this.identidade = identidade;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getIdentidade() {
        return identidade;
    }

    public void setIdentidade(int identidade) {
        this.identidade = identidade;
    }

    @Override
    public String toString() {
        return "Nome: " + nome + "\nIdentidade: " + identidade;
    }

}
