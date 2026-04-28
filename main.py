from mongodb import read_document, usuario_col, produto_col, vendedor_col

# menu das collections do mongodb
def menu_col():
    while True:
        print("----------MENU----------\n")
        print("Selecione uma collection do MongoDB:")
        print(
            """
1. Usuario
2. Produto
3. Vendedor
0. Sair
            """
        )
        try:
            option = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite um número válido.")
            continue
        if (option == 1):
            read_document(usuario_col)
        elif (option == 2):
            read_document(produto_col)
        elif (option == 3):
            read_document(vendedor_col)
        elif (option == 0):
            print("Saindo.")
            break
        else:
            print("Opção inválida")

menu_col()