/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package medicos;

import java.util.ArrayList;

/**
 *
 * @author adrie
 */
public class Lista {

    ArrayList<Medico> listademed;

    public Lista() {
        this.listademed = new ArrayList<>();
    }

    public void insereMed(Medico novoMedico) {
        listademed.add(novoMedico);
    }

    public void listarMed() {
        System.out.println("Lista de médicos");

        for (Medico med : listademed) {
            med.listar();
        }
    }

}
