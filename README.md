# Ohjelmistotekniikka, harjoitustyö
## Tehtävät
### Viikko 1
>[gitlog.txt](https://github.com/levitesuo/OhTe/blob/master/laskarit/viikko1/gitlog.txt)

>[komentorivi.txt](https://github.com/levitesuo/OhTe/blob/master/laskarit/viikko1/komentorivi.txt)

### Viikko 2
>[coverage raportti](https://github.com/levitesuo/OhTe/blob/master/laskarit/viikko2/coverage_rep.png)

### Viikko 3
>[UML simppeli monopoli](https://github.com/levitesuo/OhTe/blob/master/laskarit/viikko3/mermaid%20harjottelua/Tehtava_1.md)

Boardissa _load_grid metodi on ehkä turha. Tämä palvelkoon muistutuksena myöhemmälle ajalle. 
Poetryn asennus 

Tietokannassa owner id, mutta board datatyyppi ei tue sitä. Tämä tekee siitä atm turhan.

Tietokannassa Uuid:t tallennettu str:inä, mutta luokka ottaa Uuiditä (mielestäni). Saattaa luoda ongelmia.
```sh
curl -sSL https://install.python-poetry.org | POETRY_HOME=$HOME/.local python3 -
echo "export PATH=\"\$HOME/.local/bin:\$PATH\"" >> $HOME/.bashrc

```

Poetryn alustaminen
```sh
poetry init --python "^3.8"
poetry install --no-root
```

Poetryn dependecien lisääminen
```sh
poetry add cowsay
poetry add pytest --group dev
```

Poetry ohjelman suorittaminen
```sh
poetry run python3 src
poetry shell
```

Autopep8 formationti 
```sh
autopep8 --in-place --recursive src
```

```sh
coverage run --branch -m pytest src
coverage report -m
```