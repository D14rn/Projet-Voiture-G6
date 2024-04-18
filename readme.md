# Projet voiture

## Équipe

Notre équipe :
- Fabio est le SCRUM Master
- Nico s'occupe de la config R-Pi
- On se réparti le dev et les tests

## Conventions de nommage

> Respecter au maximum [PEP 8](https://realpython.com/python-pep8/)

Les conventions de nommage utilisées dans ce projet sont les suivantes :

- Les noms de **variables**, **fonctions** et **fichiers** sont en minuscules avec des mots séparés par des underscores (**snake_case**).
- Les noms de **classes** commencent par une majuscule et utilisent la casse Pascal (**PascalCase**).
- Les **constantes** sont entièrement en majuscules avec des mots séparés par des underscores (**UPPER_CASE**).

Les noms doivent être assez explicites mais rester de longueur raisonnable !

## UML (début)

Une ébauche d'UML de début de projet (qui va certainement pas mal changer) :

![UML](projet-voiture.png)

## Tests

Les tests sont réalisé à l'aide de unittest mais ne sont pas entièrement automatisé étant donné que l'on travail avec des capteurs et moteurs physiques.

Ceux-ci sont placés dans un sous-dossier à part et il faut les glisser à la racine du projet afin de les exécuter.

## Dépendances

### A installer pour le dévellopement

```shell
pip3 install adafruit-circuitpython-tcs34725
pip3 install adafruit-circuitpython-ina219
```

### Sur le RPi :

```shell
apt update
apt install -y python-smbus i2c-tools

pip3 install RPi.GPIO
pip3 install i2cdevice
pip3 install busio
pip3 install adafruit-circuitpython-tcs34725
pip3 install adafruit-circuitpython-ina219
```

Vérifier le I2C
```shell
lsmod | grep i2c_
i2cdetect -y 1
```
--> Si i2c_bcmxxxx : OK !
