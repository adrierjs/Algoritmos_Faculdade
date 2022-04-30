package maratona_devjogo.abc.javacore.Gabstradas.classes;

/**
 * Created by William Suane on 5/26/2016.
 */
public abstract class Pessoa {
    protected String nome;

    public abstract void imprime();

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
}
