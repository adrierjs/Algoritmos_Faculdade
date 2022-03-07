package banco;

import java.util.ArrayList;
/**
 *
 * @author LL
 */
public class Lista extends ContaCorrente {

    private ArrayList<Conta> usuarios = new ArrayList<Conta>();
   

    public Lista() {
    }
    
    public Lista(ArrayList <Conta> usuarios){ 
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
    }

    @Override
    public String toString() {
        return "Lista{" + "usuarios=" + usuarios;
    }

    public void imprimir() {
       System.out.println(usuarios);
        
    }

   
   

}
