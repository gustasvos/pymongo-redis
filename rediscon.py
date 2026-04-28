from dotenv import load_dotenv
import os

load_dotenv()

"""Basic connection example.
"""
import redis
r = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=18455,
    decode_responses=True,
    username="default",
    password=os.getenv("REDIS_PASS"),
)
success = r.set('foo', 'bar')
result = r.get('foo')
print(result)