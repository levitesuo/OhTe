# Käyttöohje

Lataa projektin viimeisin versio valitsemalla releasseista uusin versio. Ja pura se haluaamaasi kansioon.

Vaihtoehtoisesti käytä komentoa

```sh
git clone https://github.com/levitesuo/OhTe
```

## Konfiguraatio

Ohjelman generoimaa tietokanta tiedoston nimea voi vaihtaa. Tämä onnistuu luomalla projekti kansioon .env tiedosto jossa on määritelty oikeat muuttujat. Tässä esimerkki muuttujien muodosta.

```sh
DATABASE_FILENAME="projekti.sqlite"
TEST_DATABASE_FILENAME="projekti_test.sqlite"
```

## Alustaminen ja käynnistäminen

Kun projekti on ladattu siirry tiedostoon projekti ja suorita seuraava komento ladataksesesi riippuvuudet. Kaikki tulevat komennot tulee suorittaa projekti kansiossa.

```sh
poetry install
```

Tämän jälkeen pitää vielä alustaa tietokannat. Seuraavan komennon voi myös suorittaa jos haluaa pyyhkiä tietokannat tyhjäksi.

```sh
poetry run invoke build
```

Nyt ohjelma on käyttövalmis ja sen voi käynnistää komennolla

```sh
poetry run invoke start
```

## Sovelluksen käyttö
![Menu näkymä](https://github.com/levitesuo/OhTe/blob/main/projekti/Documentation/Kuvat/menu%20n%C3%A4kym%C3%A4.png)
### Käyttäjän luonti ja kirjautuminen

Sovellus on automaattisesti kirjannut sinut sisään Guest käyttäjällä. Tehdäksesi oman käyttäjän klikkaa valikosta Login ja sitten Register. 

Rekisteröinnin jälkeen ohjelman kirjaa sinut sisään rekisteröidyllä  käyttäjälle. 

Login nappi on korvattu Logout napilla joka kirjaa sinut ulos käyttäjältä ja takaisin käyttäjälle Guest. Tämän jälkeen voit kirjautua takaisin luomallesi käyttäjälle tai luoda uuden käyttäjän.

### Pelin aloitus

Klikkaamalla New Map pääset kartanluonti valikkoon josta voit valita kartan koon ja nimen. Klikkaamalla Generate ohjelma sulkee menu ikkunan ja avaa peli-ikkunan juuri luomallasi kartalla.

### Pelinäkymä
![Peli näkymä](https://github.com/levitesuo/OhTe/blob/main/projekti/Documentation/Kuvat/pelin%C3%A4kym%C3%A4.png)

Voit liikkua pelinäkymässä käyttämällä `AWSD` nappeja ja zoomata sisään tai ulos käyttämällä hiiren rullaa. Neliötä klikkaamalla muutat sen tilaa. Klikkaamalla `Step` siirrät simulaatiota yhden askeleen eteenpäin ja klikkaamalla `Start`/`Pause` pystyt hallita simulaation etenemistä. `Slider` jonka näät ruudun alareunassa hallitsee simulaation nopeutta Start tilassa. Starttia ja Stoppia pystyy hallitsemaan myös `välilyönnillä`.

Klikkaamalla `Save` kartan tilanne tallentuu. Jos kartan nimellä on jo tallennettu toinen kartta tallentuu kartta nimellä kartan_nimi COPY. ( Tässä on pieni suunnittelu virhe jos kartalla "testi", joka on tallennettu klikataan useita kertoja `Save` nappia tallentuu kaikki nämä kartat nimellä "testi COPY" )

Klikkaamalla `Menu` pääset takaisin valikko näkymään.

Jos kartta on ns. ladattuna ohjelmaan voi päävalikosta klikata `Continue` joka vie takaisin karttaan.

## Karttojen lataaminen

Klikkaamalla päävalikosta `Load` tulee näkyviin lista kaikista tallennetuista kartoista. Kartan nimellä varustettua nappia klikkaamalla kartta ladataan ja menu näkymä vaihtuu peli näkymään kyseisellä kartalla.