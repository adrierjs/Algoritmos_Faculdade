package provaII;

import java.util.ArrayList;
import javax.swing.JOptionPane;

/**
 *
 * @author LL
 */
public class Lista {

    private ArrayList<Conta> usuarios = new ArrayList<Conta>();

    public Lista() {
    }

    public Lista(ArrayList<Conta> usuarios) {
        this.usuarios = usuarios;
    }

    public ArrayList<Conta> getUsuarios() {
        return usuarios;
    }

    public void setUsuarios(ArrayList<Conta> usuarios) {
        this.usuarios = usuarios;
    }

    public void addConta(Conta usuarios) {
        this.usuarios.add(usuarios);
        JOptionPane.showMessageDialog(null, "Cliente cadastrato com sucesso!");
    }

    public void imprimirClientes() {
        if (usuarios.size() == 0) {
            JOptionPane.showMessageDialog(null, "Nenhum cliente cadastrado!");
            return;
        }
        for (Conta c : usuarios) {
            System.out.println(c.toString());
        }
    }

    public void excluirCliente(int num) {
        for (Conta n : usuarios) {
            if (n.getNum() == num) {
                this.usuarios.remove(n);
                JOptionPane.showMessageDialog(null, "Cliente excluído com sucesso");
                return;
            }
        }
        JOptionPane.showMessageDialog(null, "A conta não existe, tente novamente!");
    }

    public void imprimir() {
        System.out.println(usuarios);

    }

}
