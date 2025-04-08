from editora.defs.defs_basicas import *
from editora.biblioteca.alterar_livro.alterar_status import alterar_status
from editora.biblioteca.alterar_livro.alterar_nota import alterar_nota
from editora.biblioteca.alterar_livro.alterar_resenha import alterar_resenha
from editora.biblioteca.visualizar_livros import visualizar_livros
#tipo de alteração(status, nota, resenha)
def menu_alterar_livro(id_livro, conn):
    cursor = conn.cursor()

    while True:
        clear()
        query_select =  """
                            SELECT nome_livro, nome_autor, nome_editora, 
                                data_de_lancamento_livro, nome_genero, nome_status, 
                                ano_lido_livro, nota_livro, resenha_livro
                                
                                FROM editora.livros l 
                                JOIN editora.autores a ON l.id_autor_livro = a.id_autor
                                JOIN editora.editoras e ON l.id_editora_livro = e.id_editora
                                JOIN editora.generos g ON l.id_genero_livro = g.id_genero
                                JOIN editora.status s ON l.id_status_livro = s.id_status

                                WHERE id_livro = %s
                                ORDER BY id_livro
                        """
        cursor.execute(query_select, (id_livro, ))
        livro = cursor.fetchall()
        visualizar_livros(livro)

        print("Agora selecione o tipo de alteração que será feita: ")

        print("\n1 - Status\n2 - Nota\n3 - Resenha\n4 - Voltar\n5 - Sair\n")

        opc_alteracao = input()
        clear()

        if opc_alteracao == '1':
            alterar_status(id_livro, conn)
            break
        
        elif opc_alteracao == '2':
            alterar_nota(id_livro, conn)
            break
        
        elif opc_alteracao == '3':
            alterar_resenha(id_livro, conn)
            break

        elif opc_alteracao == '4':
            clear()
            break

        elif opc_alteracao == '5':
            print("Finalizando...")
            exit()
            
        else:
            print("Valor inválido!")