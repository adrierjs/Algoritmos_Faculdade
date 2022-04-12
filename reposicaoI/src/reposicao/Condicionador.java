/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package reposicao;


/**
 *
 * @author jennyfer
 */
public class Condicionador {

    private String nome;
    private float temperatura;

    public Condicionador() {
        this.nome = "---";
        this.temperatura = 0;
    }

    public Condicionador(String nome) {
        this.nome = nome;
        this.temperatura = 0;
    }

    public void alterarTemp(double temperatura) {

        for (int i = 1; i <= 10; i++) {
            if (temperatura == 1.8 * i || temperatura == 0) {
                this.temperatura = (float) temperatura;
            }

        }
    }

    public void aumentaTemp() {
        this.temperatura = (float) (this.temperatura + 1.8);
        alerta();
    }

    public void diminueTemp() {
        this.temperatura = (float) (this.temperatura - 1.8);
        alerta();
    }

    public void alerta() {
        if (this.temperatura > 18) {
            this.temperatura = 18;
        } else if (this.temperatura < 0) {
            this.temperatura = 0;
        }
    }

    public void desligar() {
        this.temperatura = 0;
        alerta();
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    @Override
    public String toString() {
        if (this.temperatura == 0) {
            return "\nNome do ar-condionado: " + nome + "\nTemperatura: " + temperatura +"°C"+ ". Ar-condionado desligado!";
        }

        return "\nNome do ar-condionado: " + nome + "\nTemperatura: " + temperatura+ "°C";
    }

}
