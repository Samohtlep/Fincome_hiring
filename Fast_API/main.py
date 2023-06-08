from fastapi import FastAPI , File , UploadFile
import uvicorn
from pydantic import BaseModel
from typing import Dict
import pandas as pd
from fastapi.responses import FileResponse
import  matplotlib.pyplot as plt

class Dataset(BaseModel):
    # objet dans lequel on va stocker les données, le contenu des datasets est socké dans un dictionnaire.
    id: str
    file_name: str
    size: int
    dataframe: Dict

app = FastAPI()
datasets = []

@app.get("/datasets/")
def list_datasets():
    # affiche les informations de tous les datasets uploadés
    # return : liste des datasets avec id, file_name et size
    return [{"id": dataset.id, "file_name": dataset.file_name, "size": dataset.size} for dataset in datasets]

@app.post("/datasets/")
def create_dataset(file: UploadFile = File(...)):
    # ajoute un dataset à la liste des datasets
    # arg : file : fichier csv
    # return : id, file_name et size du dataset ajouté
    df = pd.read_csv(file.file)
    if len(datasets) == 0:
        dataset_id = '0'
    else:
        dataset_id = str(int(datasets[-1].id)+1)
    dataset = Dataset(
        id=dataset_id,
        file_name=file.filename,
        size=len(df),
        dataframe=df.to_dict()
    )
    datasets.append(dataset)
    return {"id": dataset.id, "file_name": dataset.file_name, "size": dataset.size}

@app.get("/datasets/{id}/")
def get_dataset(id: str):
    # retourne le dataset dont l'id est passé en paramètre
    # arg : id : id du dataset
    # return : id, file_name et size du dataset
    for dataset in datasets:
        if dataset.id == id:
            return {"id": dataset.id, "file_name": dataset.file_name, "size": dataset.size}
    return {"erreur": "Dataset introuvable"}


@app.delete("/datasets/{id}/")
def delete_dataset(id: str):
    # supprime le dataset dont l'id est passé en paramètre
    # arg : id : id du dataset
    # return : message de confirmation de suppression
    for dataset in datasets:
        if dataset.id == id:
            datasets.remove(dataset)
            return {"message": "Dataset supprimé"}
    return {"erreur": "Dataset introuvable"}

@app.get("/datasets/{id}/excel/")
def get_dataset_excel(id: str):
    # retourne un fichier excel du dataset dont l'id est passé en paramètre
    # arg : id : id du dataset
    # return : dataset au format excel
    for dataset in datasets:
        if dataset.id == id:
            df = pd.DataFrame.from_dict(dataset.dataframe)
            df.to_excel(dataset.file_name.split('.')[0]+'.xlsx', index=False)
            return FileResponse(dataset.file_name.split('.')[0]+'.xlsx', media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', filename=dataset.file_name.split('.')[0]+'.xlsx')
    return {"erreur": "Dataset introuvable"}

@app.get("/datasets/{id}/stats/")
def get_dataset_stats(id: str):
    # retourne les statistiques du dataset dont l'id est passé en paramètre sous forme d'objet json
    # arg : id : id du dataset
    # return : statistiques du dataset
    for dataset in datasets:
        if dataset.id == id:
            df = pd.DataFrame.from_dict(dataset.dataframe)
            return df.describe().to_json()
    return {"erreur": "Dataset introuvable"}


@app.get("/datasets/{id}/plot/")
def get_dataset_plot(id: str):
    # retourne un fichier pdf contant une liste d'histogrammes de toutes les colonnes numériques du dataset dont l'id est passé en paramètre
    # arg : id : id du dataset
    # return : fichier pdf contenant les histogrammes
    for dataset in datasets:
        if dataset.id == id:
            df = pd.DataFrame.from_dict(dataset.dataframe)
            df.hist()
            plt.savefig(dataset.file_name.split('.')[0]+'_plot.pdf')
            return FileResponse(dataset.file_name.split('.')[0]+'_plot.pdf', media_type='application/pdf', filename=dataset.file_name.split('.')[0]+'_plot.pdf')

if __name__ == "main" :
    uvicorn.run(app, host="127.0.0.1", port=8000)
