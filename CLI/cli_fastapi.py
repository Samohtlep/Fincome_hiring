import argparse
import requests

parser = argparse.ArgumentParser(description='Datasets API CLI')
url = 'http://127.0.0.1:8000/datasets/'

# ajout de tous les arguments correspondant aux différentes fonctions de l'API
parser.add_argument('--list', help='affiche les informations de tous les datasets uploadés', action='store_true')
parser.add_argument('--upload', type=str, help='ajoute un dataset à la liste des datasets')
parser.add_argument('--get', type=str, help='retourne le dataset dont l\'id est passé en paramètre')
parser.add_argument('--delete', type=str, help='supprime le dataset dont l\'id est passé en paramètre')
parser.add_argument('--excel', type=str, help='retourne un fichier excel du dataset dont l\'id est passé en paramètre')
parser.add_argument('--stats', type=str, help='retourne les statistiques du dataset dont l\'id est passé en paramètre')
parser.add_argument('--plot', type=str, help='retourne un fichier pdf contant une liste d\'histogrammes de toutes les colonnes numériques du dataset dont l\'id est passé en paramètre')


args = parser.parse_args()

# on exécute les requetes correspontdant aux arguments passés

if args.list:
    print(requests.get(url).json())

elif args.upload:
    with open(args.upload, 'rb') as file:
        rep = requests.post(url, files={'file': file})
    print(rep.json())

elif args.get:
    print(requests.get(url+args.get+'/').json())

elif args.delete:
    print(requests.delete(url+args.delete+'/').json())

elif args.excel:
    rep = requests.get(url+args.excel+'/excel/')
    with open(args.excel+'.xlsx', 'wb') as file:
        file.write(rep.content)
        print('Fichier excel créé')

elif args.stats:
    print(requests.get(url+args.stats+'/stats/').json())

elif args.plot:
    rep = requests.get(url+args.plot+'/plot/')
    with open(args.plot+'_plot.pdf', 'wb') as file:
        file.write(rep.content)
        print('Fichier pdf créé')

else:
    parser.print_help()

