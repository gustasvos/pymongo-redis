from dotenv import load_dotenv
import os
import json
import redis
from bson import ObjectId

load_dotenv()

"""Basic connection example.
"""
r = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=18455,
    decode_responses=True,
    username="default",
    password=os.getenv("REDIS_PASS"),
)


def salvar_no_redis(doc, prefixo="doc"):
    # converte ObjectId e outros tipos
    doc_json = json.dumps(doc, default=str, ensure_ascii=False)

    # cria uma chave única usando _id do mongo
    key = f"{prefixo}:{doc.get('_id')}"

    r.set(key, doc_json)

    print(f"\nDocumento salvo no Redis com chave: {key}")
    return key

def editar_no_redis(key):
    valor = r.get(key)
    if not valor:
        print("Chave não encontrada no Redis")
        return

    doc = json.loads(valor)
    print("\nCampos disponíveis para editar:")
    campos = [c for c in doc.keys() if c != "_id"]
    for i, campo in enumerate(campos, start=1):
        print(f'{i}. {campo}: {doc[campo]}')

    try:
        idx = int(input("\nEscolha o número do campo para editar: ")) - 1
        if not 0 <= idx < len(campos):
            print("Índice inválido.")
            return
    except ValueError:
        print("Digite um número válido.")
        return

    campo = campos[idx]
    novo_valor = input(f"Novo valor para '{campo}': ")

    # conversao de tipo para os tipos originais do mongo
    valor_atual = doc[campo]
    try:
        if isinstance(valor_atual, int):
            novo_valor = int(novo_valor)
        elif isinstance(valor_atual, float):
            novo_valor = float(novo_valor)
    except ValueError:
        pass

    doc[campo] = novo_valor
    r.set(key, json.dumps(doc, default=str, ensure_ascii=False))
    print(f"Campo '{campo}' atualizado no Redis.")

def deletar_no_redis(key):
    r.delete(key)
    print(f"Chave '{key}' deletada do Redis.")

def devolver_para_mongo(key, col):
    valor = r.get(key)
    if not valor:
        print("Chave não encontrada no Redis.")
        return

    doc = json.loads(valor)
    _id = ObjectId(doc.pop("_id"))

    col.replace_one({"_id": _id}, doc, upsert=True)
    print(f"Documento devolvido ao MongoDB na collection '{col.name}'.")