# Jhon Conways game of life

Ohjelma on simulaatio Jhon Conways game of life:stä jonkä ympärille on rakennettu tarvittavat elementit tukemaan karttojen tallentamista ja uudelleen lataamista.

## Dokumentaatio

- [Käyttöohje](https://github.com/levitesuo/OhTe/blob/main/projekti/Documentation/k%C3%A4ytt%C3%B6ohje.md)
- [Vaatimusmäärittely](https://github.com/levitesuo/OhTe/blob/main/projekti/Documentation/m%C3%A4%C3%A4rittelydokumentti.md)
- [Arkkitehtuurikuvaus](https://github.com/levitesuo/OhTe/blob/main/projekti/Documentation/arkkitehtuuri.md)
- [Tuntikirjanpito](https://github.com/levitesuo/OhTe/blob/main/projekti/Documentation/ty%C3%B6aikakirjanpito.txt)
- [Changelog](https://github.com/levitesuo/OhTe/blob/main/projekti/Documentation/changelog.md)

## Asennus ja suorittaminen

Ohjelman saa toimimaan suorittamalla seuraavat komennto. Tarkemmat asennus ohjeet löytyy [käyttöohjeesta](https://github.com/levitesuo/OhTe/blob/main/projekti/Documentation/k%C3%A4ytt%C3%B6ohje.md).

```sh
git clone https://github.com/levitesuo/OhTe
cd OhTe/projekti
poetry install
poetry run invoke build
poetry run invoke start
```

## Komentorivi

Tässä nopea selitys kaikista komennoista jotka ohjelmaan on valmisteltu.

|  	|  	|
|---	|---	|
| ```sh poetry run invoke start ``` 	| Aloittaa sovelluksen ja avaa päävalikon. 	|
| ```sh poetry run invoke test ``` 	| Suorittaa kaikki testit. 	|
| ```sh poetry run invoke coverage ``` 	| Suorittaa kaikkii testis käyttäen coveragea 	|
| ```sh poetry run invoke coverage-report ``` 	| Suorittaa kaikki testit ja muodostaa coverage reportin html formaatissa 	|
| ```sh poetry run invoke covr ``` 	| Suorittaa kaikki testit ja muodostaa coverage reportin sekä printtaa sen terminaaliin. 	|
| ```sh poetry run invoke build ``` 	| Poistaa ensin kaiken tiedon tietokannasta ja sitten ajaa sinne uudet taulukot. Alustaa siis tietokannan. 	|
| ```sh poetry run invoke coverage-report ``` 	| Tarkiestaa koodin laadun joka on määritelty [.pylintrc](https://github.com/levitesuo/OhTe/blob/main/projekti/.pylintrc) tiedostossa 	|