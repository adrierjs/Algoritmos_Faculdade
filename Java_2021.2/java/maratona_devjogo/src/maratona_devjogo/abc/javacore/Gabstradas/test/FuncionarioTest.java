package maratona_devjogo.abc.javacore.Gabstradas.test;

import maratona_devjogo.abc.javacore.Gabstradas.classes.Gerente;
import maratona_devjogo.abc.javacore.Gabstradas.classes.Vendedor;





/**
 * Created by William Suane on 5/25/2016.
 */
public class FuncionarioTest {
    public static void main(String[] args) {
        Gerente g = new Gerente("Anna", "11122-2", 2000);
        Vendedor v = new Vendedor("Camila", "22211-4",1500,5000);
        v.calculaSalario();
        g.calculaSalario();
        System.out.println(g);
        System.out.println("--------------");
        System.out.println(v);
    }
}
