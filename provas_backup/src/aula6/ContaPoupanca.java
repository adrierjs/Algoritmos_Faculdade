package aula6;

public class ContaPoupanca extends Conta{

	@Override
	public boolean saque(double v) {
		if(obterSaldo()>=v) {
			setSaldo(obterSaldo()-v);
			return true;
		}
		return false;
	}


}
