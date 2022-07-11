/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package herança;


/**
 *
 * @author adrie
 */
public class Campus extends Universidade{
    private String cursos;

    public Campus() {
    }
 
    public Campus(String nome, String endereco,int telefone, String cursos){
        super(nome, endereco, telefone);
        this.cursos= cursos;
        Universidade uni = new Universidade();
    }
    public String getCursos() {
        return cursos;
    }

    public void setCursos(String cursos) {
        this.cursos = cursos;
    }  

    @Override
    public String toString() {
        return "Campus{" + "cursos=" + cursos + '}';
    }
    
    public void imprime(){
        System.out.println("Cursos:"+this.cursos+"Dados:"+Universidade);
        
        
    }
   
    
}
