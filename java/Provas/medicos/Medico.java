package medicos;

import java.util.ArrayList;

/**
 *
 * @author adrie
 */
public class Medico {

    private String nome;
    private Contato contato = new Contato();
    private Dados dados = new Dados();
    private Endereco endereco = new Endereco();

    public Medico() {
    }

    public Medico(String nome, Contato contato, Dados dados, Endereco endereco) {
        this.contato = contato;
        this.dados = dados;
        this.endereco = endereco;
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public Contato getContato() {
        return contato;
    }

    public void setContato(Contato contato) {
        this.contato = contato;
    }

    public Dados getDados() {
        return dados;
    }

    public void setDados(Dados dados) {
        this.dados = dados;
    }

    public Endereco getEndereco() {
        return endereco;
    }

    public void setEndereco(Endereco endereco) {
        this.endereco = endereco;
    }

    public void listar() {
        System.out.println("Médico: " + this.nome);
        System.out.println("Email: " + contato.getEmail());
        System.out.println("Telefone: " + contato.getTelefone());
        System.out.println("Estado:" + endereco.getUf());
        System.out.println("Cidade: " + endereco.getCidade());
        System.out.println("Rua: " + endereco.getRua());
        System.out.println("Número: " + endereco.getNumero());
        System.out.println("------------");

    }

}
