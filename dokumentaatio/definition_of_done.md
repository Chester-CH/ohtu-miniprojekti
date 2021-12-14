# Definition of Done

## Yleiset määritelmät
* Testikattavuus vähintään 70 % ja testit menevät läpi
* Koodi noudattaa Pylint-sääntöjä (arvosana vähintään 9,00)
* Testikattavuus ja pylint-säännöt eivät koske käyttöliittymää
* Koodissa asiat ovat nimetty selkeästi ja englanniksi
* CI-palvelun (Git Hub Actions) testit menevät läpi
* CI-palvelun tila (eli ovatko testit läpäisty) on näkyvissä repositorion etusivulla
* Ohjelman käyttäjälle näkyvä toiminnallisuus toimii manuaalisesti testattuna

## User story -kohtaiset määritelmät
Käyttäjä voi lisätä tekstimuotoisen lukuvinkin otsikkon

	Ohjelman käynnistyessä avautuu alkuvalikko

	Aloitusnäkymästä pääsee siirtymään vinkinlisäykseen  Syöte 1

	Vinkinlisäysnäkymässä saa lisättyä otsikko-kohtaan tekstisyötteen  lukuvinkki

	Vinkinlisäys tuottaa hyväksyvän palautusarvon


Käyttäjä voi selata lisäämiään vinkkejä

	Ohjelman käynnistyessä avautuu alkuvalikko
	
	Aloitusnäkymästä pääsee siirtymään vinkkien selailuun  Syöte 2
	
	Selailunäkymässä tulostuu lisätyt vinkit lisäämisjärjestyksessä


Käyttäjä voi poistaa vinkin
	
	Ohjelman käynnistyessä avautuu alkuvalikko
	
	Aloitusnäkymästä pääsee siirtymään vinkinlisäykseen  Syöte 1

	Vinkinlisäysnäkymässä saa lisättyä otsikko-kohtaan tekstisyötteen  lukuvinkki
	
	Aloitusnäkymästä pääsee siirtymään vinkkien selailuun  Syöte 2
	
	Selailunäkymästä pääsee siirtymään vinkkien poistamiseen  Syöte p
	
	Vinkin voi poistaa antamalla vinkin id-numeron  Syöte 1
	
	Vinkkiä ei tulostu selaamisnäkymässä

![Käyttäjä voi merkata lukuvinkin tyypin: kirja, video, blogpost, podcast](https://github.com/Chester-CH/ohtu-miniprojekti/blob/main/src/tests/add_tips_type.robot)

	
