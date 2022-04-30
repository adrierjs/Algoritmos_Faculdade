package medicos;

import javax.swing.JOptionPane;

/**
 *
 * @author adrie
 */
public class ClassePrincipal {

    public static void main(String[] args) {
        Lista listaMed = new Lista();
        while (true) {
            listaMed.insereMed(setMedico());
            int c = JOptionPane.showConfirmDialog(null, "Deseja continuar cadastrando médicos?");
            if (c == 1) {
                break;
            }
        }
        int c = JOptionPane.showConfirmDialog(null, "Deseja consultar os médicos cadastratos?");
        if (c == 0) {
            listaMed.listarMed();
        }
    }

    private static Contato getContato(String descricao) {
        Contato contato = new Contato();
        contato.setTelefone(JOptionPane.showInputDialog(descricao + "\n" + "Digite o Telefone do(a) "));
        contato.setEmail(JOptionPane.showInputDialog(descricao + "\n" + "O seu e-mail"));
        return contato;
    }

    private static Endereco getEndereco(String descricao) {
        Endereco endereco = new Endereco();
        endereco.setUf(JOptionPane.showInputDialog(descricao + "\n" + "Digite o estado em que você mora "));
        endereco.setCidade(JOptionPane.showInputDialog(descricao + "\n" + "Digite a sua cidade "));
        endereco.setRua(JOptionPane.showInputDialog(descricao + "\n" + "Digite a rua em que mora "));
        endereco.setNumero(JOptionPane.showInputDialog(descricao + "\n" + "Digite o número da sua residência "));
        return endereco;
    }

    private static Dados getDados(String descricao) {
        Dados medicos = new Dados();
        medicos.setSexo(JOptionPane.showInputDialog(descricao + "\n" + "Digite o seu sexo:\n"));
        medicos.setIdade(Integer.parseInt(JOptionPane.showInputDialog(descricao + "\n" + "Qual a sua idade?\n")));
        medicos.setEspecialidade(JOptionPane.showInputDialog(descricao + "\n" + "Digite a sua especilidade:\n"));
        medicos.setCrm(JOptionPane.showInputDialog(descricao + "\n" + "Digite o crm:\n" + descricao + ": "));
        medicos.setSalario(Double.parseDouble(JOptionPane.showInputDialog(descricao + "\n" + "Digite o seu salário?\n")));
        return medicos;
    }

    private static Medico setMedico() {
        String descricao = JOptionPane.showInputDialog("Qual o nome do médico?");
        Medico medico = new Medico();
        medico.setNome(descricao);
        medico.setContato(getContato(descricao));
        medico.setEndereco(getEndereco(descricao));
        medico.setDados(getDados(descricao));
        return medico;
    }

}
