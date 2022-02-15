# ohtu-miniprojekti
![GitHub Actions](https://github.com/Chester-CH/ohtu-miniprojekti/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/Chester-CH/ohtu-miniprojekti/branch/main/graph/badge.svg?token=HB429BPBU1)](https://codecov.io/gh/Chester-CH/ohtu-miniprojekti)

## Käyttöohjeet

Lataa ohjelman koodi projektin sivuilta. Aja komento projektin juuressa:

``` bash
poetry install
``` 

Luo sen jälkeen tietokanta komennolla:
``` bash
poetry run invoke build
```
jonka jälkeen voit käynnistää ohjelman komennolla:

``` bash
poetry run invoke start
```

Jos haluat, niin `poetry run` osan voi jättää kirjoittamatta kutsumalla `poetry shell` komentoa ensin.

## Arkkitehtuuri

Arkkitehtuurin mallina on Ohjemistotekniikasta tutun [TodoApp](https://github.com/ohjelmistotekniikka-hy/python-todo-app):n mukainen arkkitehtuuri. Tietokannan käsittely tapahtuu Repository-mallin mukaisesti. Käyttöliittymäkoodi on eriytetty omalle ui-tasolle, ja se käsittelee sovelluslogiikkaa services-tason luokkien
kautta. Tietokannan käsittelyä tehdään vain repositories-luokkien sisällä.

## Definition of Done

![Definition of Done](https://github.com/Chester-CH/ohtu-miniprojekti/blob/main/dokumentaatio/definition_of_done.md)

## Product Backlog ja Sprint Backlogit

Backlog: https://helsinkifi-my.sharepoint.com/:x:/g/personal/zhishang_ad_helsinki_fi/ESzC-Jm3OalOiB9j0D8Jk3gBnYgjiXha1GqmPX1QvpkNvQ?e=tM95Tj

## Loppuraportti

![loppuraportti](https://github.com/Chester-CH/ohtu-miniprojekti/blob/main/LOPPURAPORTTI.md)

## Julkaisut
- ![Sprint 3 release](https://github.com/Chester-CH/ohtu-miniprojekti/releases/tag/v.1.1.0)
- ![1st release (sprint 2)](https://github.com/Chester-CH/ohtu-miniprojekti/releases/tag/v1.0.0)




x
