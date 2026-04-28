# Como rodar

Crie o arquivo `.env` na raiz do projeto e insira sua URI do mongodb, e o host e senha do redis:

```yaml
MONGO_URI=mongodb+srv://USUARIO:SENHA@HOST/?retryWrites=true&w=majority
REDIS_HOST=redis-00000.xxxxx.xxxxxx.ec2.cloud.redislabs.com
REDIS_PASS=redispassword
```

Use o `.env.example` como referência.

Depois instalar as dependencias e rodar o `main.py`:

```bash
> pip install -r requirements.txt
> python3 main.py
```

