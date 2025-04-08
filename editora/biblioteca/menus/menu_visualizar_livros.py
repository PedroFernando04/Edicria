from editora.biblioteca.visualizar_livros import visualizar_livros
from editora.defs.defs_basicas import *
from editora.biblioteca.menus.menu_visualizar_livros_ano_lido import menu_visualizar_livros_ano_lido
from editora.biblioteca.menus.menu_visualizar_livros_nota import menu_visualizar_livros_nota
from editora.biblioteca.menus.menu_visualizar_livros_nome import menu_visualizar_livros_nome
from editora.biblioteca.menus.menu_visualizar_livros_status import menu_visualizar_livros_status

def menu_visualizar_livros(conn, id_cliente):
    while True:
        print("Informe como deseja visualizar os seus livros: ")
        print("\n1 - Todos\n2 - Pesquisar nome\n3 - Filtrar pelo Status\n4 - Filtrar pelo ano lido\n5 - Filtrar pela nota\n6 - Voltar\n7 - Sair\n")
        valores_menu = {'1', '2', '3', '4', '5'}

        menu = input()
        clear()

        cursor = conn.cursor()

        if menu == '1':
                query = """
                            SELECT nome_livro, nome_autor, nome_editora, 
                            data_de_lancamento_livro, nome_genero, nome_status, 
                            ano_lido_livro, nota_livro, resenha_livro
                            
                            FROM editora.livros l 
                            JOIN editora.autores a ON l.id_autor_livro = a.id_autor
                            JOIN editora.editoras e ON l.id_editora_livro = e.id_editora
                            JOIN editora.generos g ON l.id_genero_livro = g.id_genero
                            JOIN editora.status s ON l.id_status_livro = s.id_status

                            WHERE id_cliente_livro = %s
                            ORDER BY id_livro
                        """
                
                cursor.execute(query, (id_cliente, ))
        
        elif menu == '2':
                nome = input("Pesquise o nome do livro que deseja encontrar: ")
                menu_visualizar_livros_nome(cursor, id_cliente, nome)

        elif menu == '3':
                    menu_visualizar_livros_status(cursor, id_cliente)
                    
        elif menu == '4':
                    menu_visualizar_livros_ano_lido(cursor, id_cliente)

        elif menu == '5':
                    menu_visualizar_livros_nota(cursor, id_cliente)
                    
        elif menu == '6':
                    break
        elif menu == '7':
                    print("\nFinalizando...")
                    exit()
        else:
                print("Valor inválido!\n")
                delay()


        if menu in valores_menu:
                livros = cursor.fetchall()

                visualizar_livros(livros)
                delay()
        else: 
            continue            
            