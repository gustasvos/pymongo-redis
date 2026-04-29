from dotenv import load_dotenv
import os
import json
import redis

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

    # cria uma chave única (usa _id do Mongo)
    key = f"{prefixo}:{doc.get('_id')}"

    r.set(key, doc_json)

    print(f"\nDocumento salvo no Redis com chave: {key}")