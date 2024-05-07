# Ohjelmistotekniikka, harjoitustyö

### [Työaikakirjanpito](https://github.com/levitesuo/OhTe/blob/main/projekti/Documentation/ty%C3%B6aikakirjanpito.txt)

### [Changelog](https://github.com/levitesuo/OhTe/blob/main/projekti/Documentation/changelog.md)

## Asennus ohjeet
```sh
git clone https://github.com/levitesuo/OhTe
cd OhTe/projekti
poetry install
poetry run invoke build
poetry run invoke start
```

## Coverage raportin tuottaminen

```sh
poetry run invoke coverage-raport
```

## Testien suorittaminen

```sh
poetry run invoke test
```