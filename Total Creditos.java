Import javax.swing.JOpcionPane; //importando paquete 
public class TotalCreditos{
	public static void main (String [] orgs ) { 
		short fCre, cF; 
		byte tc1, tc2, tc3, tc4, tc5, tc6; 
		System.out.println("Recuerda que lo máximo de créditos por semestre son 34 y lo mínimo son 18"); 
		System.out.println ("Dime tus créditos de primer semestre"); 
		tc1; 
		tc1= Byte.parseByte (JOpcionPane.showInputDialog("Dime tus créditos de primer semestre"));
		JOpcionPane.showMessageDialog ("Dime tus créditos de segundo semestre"); 
		tc2; 
		tc2= Byte.parseByte (JOpcionPane.showInputDialog("Dime tus créditos de segundo semestre");
		JOpcionPane.showMessageDialog ("Dime tus créditos de tercer semestre");
		tc3;
		tc3= Byte.parseByte (JOpcionPane.showInputDialog("Dime tus créditos de tercer semestre"));
	|	JOpcionPane.showMessageDialog ("Dime tus créditos de cuarto semestre)"; 
		tc4 
		tc4= Byte.parseByte (JOpcionPane.showInputDialog("Dime tus créditos de cuarto semestre"));
		JOpcionPane.showMessageDialog ("Dime tus créditos de quinto semestre");
		tc5;
		tc5= Byte.parseByte (JOpcionPane.showInputDialog("Dime tus créditos de quinto semestre"); 
		JOpcionPane.showMessageDialog ("Dime tus créditos de sexto semestre"); 
		tc6;
		tc6= Byte.parseByte (JOpcionPane.showInputDialog("Dime tus créditos de sexto semestre")); 
		fCre= (tc1+tc2+tc3+tc4+tc5+tc6); 
		cF= (fCre*0.60);
		System.out.println ("Tu total de créditos es" + fCre); 
		System.out.println ("Tu porcentaje de créditos es" +cF);
		if (fCre<=) && (fCre>=122.4) {
			System.out.println ("Puedes realizar servico social");
		} else { 
			System.out.println ("No puedes realizar servicio social");
		} else if (fCre>204) && (fCre>122.4); 
			System.out.print ("Valores invalidos"); 
		} 
}
		