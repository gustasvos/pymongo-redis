from dotenv import load_dotenv
import os
import json
from rediscon import salvar_no_redis

load_dotenv()

from pymongo import MongoClient
from pymongo.server_api import ServerApi

# URI UNICA
uri = os.getenv("MONGO_URI")
 
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["mercadolivre"]
 
# collections
usuario_col = db.usuario
produto_col = db.produto
vendedor_col = db.vendedor


def print_doc_formatado(doc):
    print(json.dumps(doc, indent=4, ensure_ascii=False, default=str))

def read_collection(col):
    print(f"\nCollection {col.name}\n")
    docs = list(col.find())

    if not docs:
        print("Nenhum documento encontrado")
        return []
    
    for i, doc in enumerate(docs, start=1):
        print(f"{i}. {doc["nome"]}")
    return docs

def select_collection(col):
    docs = read_collection(col)
    if not docs:
        return None
    
    while True:
        option = int(input("\nSelecione o número do documento: "))
        if 1 <= option <= len(docs):
            return docs[option - 1]
        else:
            print(f"Índice inválido, escolha entre 1 e {len(docs)}.")

def read_document(col, doc_name):
    print(f"\nSelecione o documento que deseja visualizar: ")
    doc = select_collection(col)

    if doc is None:
        return
    else:
        print_doc_formatado(doc)

    salvar_no_redis(doc, doc_name.lower())