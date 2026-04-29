from mongodb import read_document, usuario_col, produto_col, vendedor_col

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
            read_document(usuario_col, "usuario")
        elif (option == 2):
            read_document(produto_col, "produto")
        elif (option == 3):
            read_document(vendedor_col, "vendedor")
        elif (option == 0):
            print("Saindo.")
            break
        else:
            print("Opção inválida")

menu_col()