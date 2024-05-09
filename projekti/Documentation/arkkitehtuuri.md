# Arkkitehtuurikuvaus

## Rakenne

Ohjelma on toteutettu käyttäen kolmitasoista kerrosarkkitehtuuria. Tätä hieman sotkee UI:n ja game_enginen verrattavissa olevat roolit, sillä kummatkin ovat vastuussa käyttöliittymästä.

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

Tkinter pohjaisissa menu näkymissä jokainen sivu on jaettu omaan luokkaansa sekä tiedostoonsa. Nämä ovat hyvin eristettyhä sovelluslogiikasta.

Pygamepohjaisessa game_engine luokassa on ollut pakko sotkea hieman toiminnallisuutta ja käyttöliittymää. Toiminnallisuutta täältä löytyy pelin askeltamisen nopeuden hallinta sekä zoomauksen että liikkumisen hallinta, jotka olisivat kaikki hankala toteuttaa muualla.


## Sovelluslogiikka

```mermaid
 classDiagram
      Board "*" --> "1" User
      class User{
          id
          username
          password
      }
      class Board{
          id
          name
          size
          grid
      }
```

Toiminnallisista kokonaisuuksista vastaa luokka GOLService josta löytyy kaikille UI:n ja enginen pääfunktioille omat metodit. Tällä oliolla saavutetaan myös tiedonsiirto UI:n ja enginen välillä. Käytännössä kaikki käyttöliittymät ovat portaaleita joiden kautta käyttäjä manipuloi GOLServices olion atribuutteja.

## Tietojen pysyväistallennus

Pakkauksen repositories luokat GridRepository ja UserRepository huolehtivat tietojen tallettamisesta. Kummatkin luokat tallentavat tiedot SQLite-tietokantaan.

UserRepository:n tallentaa tiedot täsmälleen siinä muodossa kun ne ovat User luokassa, mutta GridRepository pakkaa Board objektin grid atribuutin tiedon tekstijonoksi str(grid) komennolla ennen tietokantaan pakkaamista. Kun GridRepositorystä pyydetään tietoa se purkaa kyseiset tekstijonot takaisin matriiseiksi. Board olion size atribuutti jätetään myös tallentamatta, sillä se voidaan helposti laskea Board olion grid atribuutin pituudesta.

## Päätoiminnallisuudet

Alla on kuvattu sovelluksen päätoiminnallisuutta sekvenssikaaviona.

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

### Kartan tallennus

```mermaid
sequenceDiagram
  actor Käyttäjä
  participant game_engine
  participant GOL_service
  participant grid_repository
  Käyttäjä->>game_engine: click "Save"
  game_engine->>GOL_service: save_board()
  GOL_service->>grid_repository: save_grid(self._board, self._user.user_id)
```

### Kartan lataaminen

```mermaid
sequenceDiagram
  actor Käyttäjä
  participant UI
  participant GOL_service
  participant grid_repository
  participant engine
  Käyttäjä->>UI: click "Load"
  UI->>GOL_service: load_board(board_id)
  GOL_service->>grid_repository: get_grid_by_id(board_id)
  grid_repository-->>GOL_service: board
  GOL_service->>GOL_service: self._board = board
  UI->>UI: root.destroy()
  UI->>engine: game_engine.start()
```

### Kartan manipulointi

```mermaid
sequenceDiagram
  actor Käyttäjä
  participant engine
  participant GOL_service
  participant Board
  Käyttäjä->>engine: click cell
  engine->>GOL_service: manipulate_board(x, y)
  GOL_service->>Board: self._board.manipulate(x, y)
```

### Muut toiminnallisuudet


## Ohjelman rakenteeseen jääneet heikkoudet

### Käyttöliittymä

Ohjelman käyttöliittymä on jaoteltu selkeästi kahteen eri osaan. Olisi kuitenkin suoraviivaisempaa tehdä se vain yhdellä moduulilla.

### Engine

Engine luokka on liian iso ja pitkä. Se pitäisi refactoroida useampaan pienempään luokkaan.

### Errorit

Ohjelma kykenee käsittelemään hyvin rajallisen määrän erroreita. Myönnettäköön että kyseiset errorit ovat juuri ne jotka käyttäjä voi saada aikaiseksi. Laajempi erroreitten käsittely kuitenkin olisi hyödyllistä.

**HUOM:** pylintrc muokattu rivilla 171. Lisäys generated-members=pygame.* tehty, koska muuten pylint valitti että

```sh
src/engine.py:208:29: E1101: Module 'pygame' has no 'QUIT' member (no-member)
src/engine.py:209:16: E1101: Module 'pygame' has no 'quit' member (no-member)
src/engine.py:210:29: E1101: Module 'pygame' has no 'MOUSEBUTTONDOWN' member (no-member)
src/engine.py:219:29: E1101: Module 'pygame' has no 'KEYDOWN' member (no-member)
src/engine.py:219:61: E1101: Module 'pygame' has no 'K_SPACE' member (no-member)
src/engine.py:231:12: E1101: Module 'pygame' has no 'quit' member (no-member)
src/engine.py:260:16: E1101: Module 'pygame' has no 'K_a' member (no-member)
src/engine.py:262:16: E1101: Module 'pygame' has no 'K_d' member (no-member)
src/engine.py:264:16: E1101: Module 'pygame' has no 'K_s' member (no-member)
src/engine.py:266:16: E1101: Module 'pygame' has no 'K_w' member (no-member)
```
