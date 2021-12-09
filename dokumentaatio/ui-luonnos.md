# UI-luonnoksia

## User story: Käyttäjä voi merkata lukuvinkin tyypin

Käyttäjän luodessa uutta vinkkiä:

```
Anna komento:
1: lisää lukuvinkki
2: selaa lukuvinkkejä
0: lopeta
Syötä toiminto: 1

Valitse uuden lukuvinkin tyyppi: (k)irja, (v)ideo, (p)odcast tai (b)logiposti. Tyhjä tyyppi-kenttä lopettaa lisäyksen.
Syötä tyyppi: k
Kirjoita otsikko: Harry Potter
```

Tyypin syötteessä oli virhe:
```
Valitse uuden lukuvinkin tyyppi: (k)irja, (v)ideo, (p)odcast tai (b)logiposti. Tyhjä tyyppi-kenttä lopettaa lisäyksen.
Syötä tyyppi: z
Virheellinen tyyppi, hyväksytyt lukuvinkin tyypit ovat: (k)irja, (v)ideo, (p)odcast tai (b)logiposti.
```

Otsikon syötteessä oli virhe, esim. tyhjä kenttä:
```
Valitse uuden lukuvinkin tyyppi: (k)irja, (v)ideo, (p)odcast tai (b)logiposti. Tyhjä tyyppi-kenttä lopettaa lisäyksen.
Syötä tyyppi: v
Kirjoita otsikko: 
Otsikko ei voi olla tyhjä.
Kirjoita otsikko: _
```

## User story: Käyttäjä voi lisätä eri tietoja lukuvinkin tyypistä riippuen

Luodessa uutta kirjan lukuvinkkiä:
```
Anna komento:
1: lisää lukuvinkki
2: selaa lukuvinkkejä
0: lopeta
Syötä toiminto: 1

Valitse uuden lukuvinkin tyyppi: (k)irja, (v)ideo, (p)odcast tai (b)logiposti. Tyhjä tyyppi-kenttä lopettaa lisäyksen.
Syötä tyyppi: k
Kirjoita otsikko: Foundation
Kirjoittajan nimi: Isaac Asimov
ISBN: 0-553-29335-4
Kirjan kuvaus (vapaaehtoinen): Scifi-kirja
Uuden lukuvinkin luonti onnistui.
```
