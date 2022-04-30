package aula6;

public class Principal {
	public static void main(String args []) {
		
		//Conta c=new Conta();
		
		ContaCorrente cc =new ContaCorrente();
		SeguroDeVida sv=new SeguroDeVida();
		ContaPoupanca cp=new ContaPoupanca();
		
		cc.depositar(100);
		cp.depositar(100);
		
		if(cc.saque(50)) {
			System.out.println(cc.obterSaldo());
		}
		
		if(cp.saque(50)) {
			System.out.println(cp.obterSaldo());
		}
		
		System.out.println(sv.calculaTributos());
		System.out.println(cc.calculaTributos());
		
	}
}
