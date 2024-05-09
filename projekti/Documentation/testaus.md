# Testausdokumentti

Ohjelmaa on testattu yksikkö- ja integraatiotestein. Sekä sen toimivuus on tarkistettu manuaalisesti.

## Yksikkö- ja integraatiotestaus

Luokille Board, User, GridRepository, UserRepository  sekä GOLService on kirjoitettu yksikkötestit, joilla varmistutaan luokkien halutusta toiminnasta.

Testatessa luokkia GridRepository, UserRepository  sekä GOLService on luokille annettu tietokanta yhteydeksi  test_database_connection joka yhdistää ne eri tietokantaa kun mitä sovellus käyttää. Tällä varmistetaan ettei testien suorittaminen vaikuta aktiiviseen tietokantaan.

## Testikattavuus

![Kuva](https://github.com/levitesuo/OhTe/blob/main/projekti/Documentation/coverage-report.png)

Testauksen ulkopuolelle jäi engine.py, build.py sekä initialize_database.py.

## Järjestelmätestaus

Sovelluksen järjestelmätestaus on suoritettu manuaalisesti. On varmistettu että kaikki toiminnallisuus listattu määrittelydokumentissa toimii halutulla tavalla. Tämä on tehty käyttöohjeen antamien ohjeiden mukaisesti.