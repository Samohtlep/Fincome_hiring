# Fincome_hiring

## Introduction

Ceci est un mini projet pour le recrutement de Fincome. 


## Objectif

L'objectif est de créer un serveur API REST en utilisant le framework Fast_API 
qui permet de gérer des datasets avec une interface client en command-line.
le sujet peut être retrouvé ici : https://github.com/datapane/be-hiring-challenge

## Installation

### packages requis

#### main.py

fastapi  
uvicorn  
pydantic  
pandas  
python-multipart  
openpyxl  
matplotlib  

#### cli_fastapi.py

requests  

## Utilisation

installer les packages requis  
lancer le fichier main.py avec un interpreteur fastapi pour lancer le serveur
ouvrir un terminal dans le répertoire CLI:
executex les commandes suivantes:

```bash
python cli_fastapi.py
```
ou 
```bash
python cli_fastapi.py --help
```
pour afficher l'aide

```bash
python cli_fastapi.py --list 
```
pour afficher la liste des datasets disponibles

```bash
python cli_fastapi.py --get [id du dataset]
```
pour afficher les informations du dataset correspondant à l'id

```bash
python cli_fastapi.py --delete [id du dataset]
```
pour supprimer le dataset correspondant à l'id de la liste

```bash
python cli_fastapi.py --excel [chemin du fichier]
```
pour ajouter générer un fichier excel à partir du dataset correspondant à l'id

```bash
python cli_fastapi.py --stats [id du dataset]
```
pour afficher les statistiques du dataset correspondant à l'id

```bash
python cli_fastapi.py --plot [id du dataset]
```
pour afficher un graphique à partir du dataset correspondant à l'id



