package aula6;

public class SeguroDeVida implements Tributavel{
	public final double TAXA=42;
	
	@Override
	public double calculaTributos() {
		return TAXA;
	}

}
