# BibleGateway Scrapper

This is a simple scrapper made with Python and BeautifulSoup.

## Usage:

`python app.py [verse] [bible version | optional, it defaults to Reina Valera 1960)`

So, on the terminal:
```bash
python app.py Juan3:16
```
Will get
```bash
 Juan 3:16Reina-Valera 1960 (RVR1960)
De tal manera amó Dios al mundo
16 Porque de tal manera amó Dios al mundo, que ha dado a su Hijo unigénito, para que todo aquel que en él cree, no se pierda, mas tenga vida eterna.
```

If you want another bible version:
```bash
python app.py Juan3:16 TLA
```

Will get
```bash
 Juan 3:16Traducción en lenguaje actual (TLA)
16 »Dios amó tanto a la gente de este mundo, que me entregó a mí, que soy su único Hijo, para que todo el que crea en mí no muera, sino que tenga vida eterna.
```

Currently it only works in Spanish!
