/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package maratona_devjogo.abc.javacore.Hinterfaces.classes;

/**
 *
 * @author adrie
 */
public class Carro implements Itributavel{
    private double valor, valorFinal;
    @Override
    public void calcularImposto() {
        this.valorFinal = valor+valor*IMPOSTO;
        
    }

    public Carro(double valor) {
        this.valor = valor;
        calcularImposto();
    }

    public void setValor(double valor) {
        this.valor = valor;
    }
    
    
    public double getValor() {
        return valor;
    }

    public double getValorFinal() {
        return valorFinal;
    }

    @Override
    public String toString() {
        return "Carro{" + "valor=" + valor + ", valorFinal=" + valorFinal + '}';
    }
    
    
    
    
}
