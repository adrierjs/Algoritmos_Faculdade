
package medicos;

/**
 *
 * @author adrie
 */
public class Endereco {

    private String rua, numero, uf, cidade;

    public Endereco() {
    }

    public Endereco(String rua, String numero) {
        this.rua = rua;
        this.numero = numero;
    }

    public void setEndereco(String rua, String numero, String uf, String cidade) {/*metodo set caso ele chame 
                                                            o construtor vazio*/
        this.rua = rua;
        this.numero = numero;
        this.uf = uf;
        this.cidade = cidade;
    }

    public void setRua(String rua) {
        this.rua = rua;
    }

    public void setNumero(String numero) {
        this.numero = numero;
    }

    public String getRua() {
        return this.rua;
    }

    public String getNumero() {
        return this.numero;
    }

    public void setUf(String uf) {
        this.uf = uf;
    }

    public String getUf() {
        return uf;
    }

    public String getCidade() {
        return cidade;
    }

    public void setCidade(String cidade) {
        this.cidade = cidade;
    }
    
    

}
