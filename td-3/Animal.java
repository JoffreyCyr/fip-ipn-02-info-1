public class Animal
{
	private String name;
	private Classification classification;

	enum Classification
	{
		POISSON(0)   ,
		INSECTE(1)   ,
		OISEAU(2)    ,
		MAMMIFERE(3) ,
		AMPHIBIEN(4) ,
		REPTILE(5)   ,
		INVERTEBRE(6);

		private int value;

		private Classification(int value)
		{
			this.value = value;
		}
	}

	public Animal(Classification classification, String name)
	{
		this.name = name;
		this.classification = classification;
	}

	public String getName()
	{
		return name;
	}

	public Classification getClassification()
	{
		return classification;
	}
}