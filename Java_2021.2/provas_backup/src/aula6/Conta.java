package aula6;

public abstract class Conta {
	private double saldo;

	public Conta(double saldo) {
		this.saldo = saldo;
	}
	
	public Conta() {
		this.saldo = 0;
	}
	
	
	public void setSaldo(double saldo) {
		this.saldo = saldo;
	}

	public void depositar(double v) {
		this.saldo+=v;
	}
	
	public double obterSaldo() {
		return this.saldo;
	}
	
	public abstract boolean saque(double v);
	
}
