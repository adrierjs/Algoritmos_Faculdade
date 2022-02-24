/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package maratona_devjobo.br.com.abc.javacore.Fmodificadorestatico.classes;

/**
 *
 * @author adrie
 */
public class Carro {
    private String modelo;
    private double velocidadeMaxima;
    private static double velocidadeLimite;

    public Carro() {
    }

    public Carro(String modelo, double velocidadeMaxima) {
        this.modelo = modelo;
        this.velocidadeMaxima = velocidadeMaxima;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public double getVelocidadeMaxima() {
        return velocidadeMaxima;
    }

    public void setVelocidadeMaxima(double velocidadeMaxima) {
        this.velocidadeMaxima = velocidadeMaxima;
    }

    public static double getVelocidadeLimite() {
        return velocidadeLimite;
    }

    public static void setVelocidadeLimite(double velocidadeLimite) {
        Carro.velocidadeLimite = velocidadeLimite;
    }
    public static double getvelocidadeLimite(){
        return Carro.velocidadeLimite;
    }
    
    
    public void imprime(){
        System.out.println("Modelo: "+this.modelo);
        System.out.println("Velocidade Máxima: "+this.velocidadeMaxima);
        System.out.println("Velocidade Limite: "+Carro.velocidadeLimite);
        System.out.println("--------------------");
        
    }
    
    
    
}
