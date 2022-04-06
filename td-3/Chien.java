public class Chien extends Animal
{
	public boolean isCute;

	public Chien( String name )
	{
		super(Classification.MAMMIFERE,name);
		isCute = true;
	}

	public static void main(String[] args)
	{
		Chien chien = new Chien("Guimauve");
		System.out.println(chien.getName());
	}
}
