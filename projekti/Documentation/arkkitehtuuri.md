# Arkkitehtuurikuvaus

## Rakenne
```mermaid
---
title: Sovelluksen rakenne
---
classDiagram
services <|-- ui
services <|-- engine
ui <|--|>  engine : For switching between windows
repositories <|-- services
entities <|-- services
entities <|-- repositories
    class ui{
        Sisältää tkinter elementit.
        Vastuussa menu:ista
    }
    class engine{
        Sisältää pygame elementit.
        Vastuussa pelin pyörimisestä.
    }
    class services{
        Sisältää ui / enginen tarvitsemat komennot.
        Antaa engine:lle ja ui:lle pääsyn sovelluslogiikkaan.
    }
    class repositories{
        Sisältää tietokantojen käyttöön tarvittavan koodin
    }
    class entities{
        Sisältää sovelluslogiikalle keskeiset oliot.
    }

```
## Käyttöliittymä

Käyttöliittymä(t) on jaettu kahteen
- tkinter pohjaiset menu näkymät 
- pygame pohjainen peli näkymä


## Sovelluslogiikka

## Tietojen pysyväistallennus



### Tiedostot



## Päätoiminnallisuudet


### Käyttäjän kirjaantuminen


```mermaid
sequenceDiagram
  actor Käyttäjä
  participant UI
  participant GOL_service
  participant UserRepository
  Käyttäjä->>UI: click "Login" button
  UI->>GOL_service: login("kalle", "kalle123")
  GOL_service->>UserRepository: find_by_username("kalle")
  UserRepository-->>GOL_service: user
  GOL_service-->>UI: user
  UI->UI: show_main_view()
```


### Uuden käyttäjän luominen


```mermaid
sequenceDiagram
  actor Käyttäjä
  participant UI
  participant GOL_service
  participant UserRepository
  participant matti
  Käyttäjä->>UI: click "Create user" button
  UI->>GOL_service: register_user("matti", "matti123")
  GOL_service->>UserRepository: find_by_username("matti")
  UserRepository-->>GOL_service: None
  GOL_service->>matti: User("matti", "matti123")
  GOL_service->>UserRepository: register_user(matti)
  UserRepository-->>GOL_service: user
  GOL_service->>GOL_service:self._user = matti
  GOL_service-->>UI: user
  UI->>UI: show_main_view()
```

### Kartan luominen

```mermaid
sequenceDiagram
  actor Käyttäjä
  participant UI
  participant GOL_service
  participant board
  participant engine
  Käyttäjä->>UI: click "Create"
  UI->>GOL_service: create_todo("5X5", "matin_kartta")
  GOL_service->>board: Board(size=5, name="matin_kartta")
  GOL_service->>GOL_service: self._board = board
  UI->>UI: root.destroy()
  UI->>engine: game_engine.start()
```


### Muut toiminnallisuudet


## Ohjelman rakenteeseen jääneet heikkoudet

### Käyttöliittymä

