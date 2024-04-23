# Arkkitehtuurikuvaus

## Rakenne

´

## Käyttöliittymä

´

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

[Tapahtumakäsittelijä](https://github.com/ohjelmistotekniikka-hy/python-todo-app/blob/master/src/ui/todos_view.py#L106) kutsuu sovelluslogiikan metodia [create_todo](https://github.com/ohjelmistotekniikka-hy/python-todo-app/blob/master/src/services/todo_service.py#L49) antaen parametriksi luotavan työn tiedot. Sovelluslogiikka luo uuden `Todo`-olion ja tallettaa sen kutsumalla `TodoRepository`:n metodia `create`. Tästä seurauksena on se, että käyttöliittymä päivittää näytettävät todot kutsumalla omaa metodiaan `initialize_todo_list`.

### Muut toiminnallisuudet

Sama periaate toistoo sovelluksen kaikissa toiminnallisuuksissa, käyttöliittymän tapahtumakäsittelijä kutsuu sopivaa sovelluslogiikan metodia, sovelluslogiikka päivittää todojen tai kirjautuneen käyttäjän tilaa. Kontrollin palatessa käyttäliittymään, päivitetään tarvittaessa todojen lista sekä aktiivinen näkyvä.

## Ohjelman rakenteeseen jääneet heikkoudet

### Käyttöliittymä

Graafisen käyttöliittymän koodissa on jonkin verran toisteisuuttaa, josta voisi toteuttaa omia komponenttejaan. Esimerkiksi pylint ilmoittaa toisteisesta koodista luokissa [CreateUserview](https://github.com/ohjelmistotekniikka-hy/python-todo-app/blob/master/src/ui/create_user_view.py) ja [LoginView](https://github.com/ohjelmistotekniikka-hy/python-todo-app/blob/master/src/ui/login_view.py).