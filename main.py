from mongodb import read_document, usuario_col, produto_col, vendedor_col
from rediscon import editar_no_redis, deletar_no_redis, devolver_para_mongo

def menu_redis(key, col):
    while True:
        print(f"\n--- Documento no Redis: {key} ---")
        print("1. Editar campo")
        print("2. Deletar do Redis")
        print("3. Devolver para o MongoDB")
        print("0. Voltar")
        try:
            option = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite um número válido.")
            continue

        if option == 1:
            editar_no_redis(key)
        elif option == 2:
            deletar_no_redis(key)
            break 
        elif option == 3:
            devolver_para_mongo(key, col)
        elif option == 0:
            break
        else:
            print("Opção inválida")

# menu das collections do mongodb
def menu_col():
    while True:
        print("----------MENU----------\n")
        print("Selecione uma collection do MongoDB:\n")
        print("1. Usuario")
        print("2. Produto")
        print("3. Vendedor")
        print("0. Sair\n")

        try:
            option = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite um número válido.")
            continue

        if (option == 1):
            key = read_document(usuario_col, "usuario")
            if key: menu_redis(key, usuario_col)
        elif (option == 2):
            key = read_document(produto_col, "produto")
            if key: menu_redis(key, produto_col)
        elif (option == 3):
            key = read_document(vendedor_col, "vendedor")
            if key: menu_redis(key, vendedor_col)
        elif (option == 0):
            print("Saindo.")
            break
        else:
            print("Opção inválida")

menu_col()