package aula6;

public class ContaCorrente extends Conta implements Tributavel{
	
	ContaCorrente(){
		super();
	}

	@Override
	public boolean saque(double v) {
		if(obterSaldo()>=v+(v/100)) {
			setSaldo(obterSaldo()-v-(v/100));
			return true;
		}
		return false;
	}

	@Override
	public double calculaTributos() {
		return obterSaldo()-(obterSaldo()/100);
	}
	
}
