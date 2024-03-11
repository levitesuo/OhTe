# Mermaid testing

Yritellääs
 
 ```mermaid
    classDiagram
        class Noppa{
            +heita () int
        }

        class Pelaaja {
            -Nimi str
            -Pelinappula Pelinappula

        }

        class Pelinappula {
            -Sijainti: Ruutu
        }
        class Pelilauta {
            -Ruudut: Arrya
        }
        class Ruutu {
            -Seuraava_ruutu: Ruutu
        }


        Pelinappula"2...8" --"1" Ruutu
        Pelaaja"1" -- "1"Pelinappula
        Pelaaja "2...8"-- "2"Noppa
        Pelilauta "1"--*"40" Ruutu
        
```