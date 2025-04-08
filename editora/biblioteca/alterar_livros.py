from editora.defs.defs_basicas import *
from editora.biblioteca.menus.menu_alterar_livros import menu_alterar_livro

def alterar_livro(conn, id_cliente):

    cursor = conn.cursor()

    print("Escolha o livro que deseja alterar:\n")

    #select de todos os livros
    query_todos =   """
                        SELECT id_livro, nome_livro FROM editora.livros
                        WHERE id_cliente_livro = %s
                        ORDER BY id_livro
                    """ 
    cursor.execute(query_todos, (id_cliente, ))
    livros = cursor.fetchall()

    for i in range (0, len(livros)):
        print(f"{livros[i][0]}  - {livros[i][1]}")


    #try int input - livro enumerado
    while True:
        try:
            opc_livros = int(input("\nSelecione o livro pelo número indicado: "))
            if (opc_livros in range(1, len(livros) + 1)):
                break
            else:
                raise Exception

        except Exception:
            clear()
            print("Valor inválido!")
            print("Informe o número relacionado ao livro\n")
            for i in range (0, len(livros)):
                print(f"{livros[i][0]}  - {livros[i][1]}")

    menu_alterar_livro(opc_livros, conn)
    

    
