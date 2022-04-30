package medicos;

/**
 *
 * @author adrie
 */
public class Dados {

    private String crm, especialidade, nome, sexo;
    ;
    private double salario;
    private int idade;

    public Dados() {

    }

    public Dados(String nome, int idade, String sexo, String crm, String especilidade, double salario) {
        this.nome = nome;
        this.idade = idade;
        this.sexo = sexo;
        this.crm = crm;
        this.especialidade = especilidade;
        this.salario = salario;

    }

    public void setDados(String nome, int idade, String sexo, String crm, String especilidade, double salario) {
        this.nome = nome;
        this.idade = idade;
        this.sexo = sexo;
        this.crm = crm;
        this.especialidade = especilidade;
        this.salario = salario;

    }

    public String getCrm() {
        return crm;
    }

    public void setCrm(String crm) {
        this.crm = crm;
    }

    public String getEspecialidade() {
        return especialidade;
    }

    public void setEspecialidade(String especialidade) {
        this.especialidade = especialidade;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getSexo() {
        return sexo;
    }

    public void setSexo(String sexo) {
        this.sexo = sexo;
    }

    public double getSalario() {
        return salario;
    }

    public void setSalario(double salario) {
        this.salario = salario;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

}
