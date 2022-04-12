package medicos;

/**
 *
 * @author adrie
 */
public class Contato {

    String email, telefone;

    public Contato() {

    }

    public Contato(String email, String telefone) {
        this.email = email;
        this.telefone = telefone;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public void setTelefone(String telefone) {
        this.telefone = telefone;
    }

    public String getTelefone() {
        return telefone;
    }

    public String getEmail() {
        return email;
    }

}
