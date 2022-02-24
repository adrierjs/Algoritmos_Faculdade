package br.com.abc.javacore.Aintroducaoclasses.classes;

/**
 * Created by William Suane on 3/10/2016.
 */
public class Carro {
    public String placa;
    public String modelo;
    public float velocidadeMaxima;

    public Carro(String placa, String modelo, float velocidadeMaxima) {
        this.placa = placa;
        this.modelo = modelo;
        this.velocidadeMaxima = velocidadeMaxima;
    }

    public Carro() {
    }

    public String getPlaca() {
        return placa;
    }

    public void setPlaca(String placa) {
        this.placa = placa;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public float getVelocidadeMaxima() {
        return velocidadeMaxima;
    }

    public void setVelocidadeMaxima(float velocidadeMaxima) {
        this.velocidadeMaxima = velocidadeMaxima;
    }

   

}
