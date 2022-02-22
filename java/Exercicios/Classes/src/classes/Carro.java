/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package classes;

import java.util.ArrayList;

/**
 *
 * @author adrie
 */
public class Carro {
    private String cor;
    private String modelo;
    private String placa;
    
    
    public Carro(){
        
    }
    
    public Carro(String cor, String modelo, String placa){
        this.cor = cor;
        this.modelo = modelo;
        this.placa = placa;
    }

    public String getCor() {
        return cor;
    }

    public void setCor(String cor) {
        this.cor = cor;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public String getPlaca() {
        return placa;
    }

    public void setPlaca(String placa) {
        this.placa = placa;
    }
    
    public String toString(){
        return this.cor+"\n"+
                this.modelo+"\n"+
                this.placa;
    }
    

 
    
}
