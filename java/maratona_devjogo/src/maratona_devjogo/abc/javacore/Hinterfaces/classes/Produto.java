/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package maratona_devjogo.abc.javacore.Hinterfaces.classes;

/**
 *
 * @author adrie
 */
public class Produto implements Itributavel, Transportavel{
   private String nome;
   private double peso, preco, precoFinal, valorFrete;

    @Override
    public void calcularImposto() {
        precoFinal = this.preco +(preco* IMPOSTO);
    }
    
   @Override
    public void calculaFrete(){
        this.valorFrete = this.preco/peso * 0.1;
        
    }

    public Produto(String nome, double peso, double preco) {
        this.nome = nome;
        this.peso = peso;
        this.preco = preco;
    }
    

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public double getPeso() {
        return peso;
    }

    public void setPeso(double peso) {
        this.peso = peso;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }

    public double getPrecoFinal() {
        return precoFinal;
    }

    public double getValorFrete() {
        return valorFrete;
    }

    @Override
    public String toString() {
        return "Produto" + "nome=" + nome + ", peso=" + peso + ", preco=" + preco + ", precoFinal=" + precoFinal + ", valorFrete=" + valorFrete + '}';
    }
    

   
    
    
    
    


    
}
