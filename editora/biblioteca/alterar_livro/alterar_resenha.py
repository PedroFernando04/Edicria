from editora.defs.defs_basicas import *


def alterar_resenha(id_livro, conn):
    cursor = conn.cursor()

    query_select =  """
                        SELECT nome_livro, resenha_livro
                        FROM editora.livros l
                        WHERE id_livro = %s
                    """
    cursor.execute(query_select, (id_livro, ))
    livro = cursor.fetchall()

    print(f"{livro[0][0]}\n Resenha:\n{livro[0][1]}")
    print("\nInforme a nova resenha do livro:\n")

    nova_resenha = input()
    

    query_nova_resenha =   """
                            UPDATE editora.livros l
                            SET resenha_livro = %s
                            WHERE id_livro = %s
                        """
    cursor.execute(query_nova_resenha, (nova_resenha, id_livro))
    conn.commit() 

    clear()
    input("Alterção realizada com sucesso!")
    clear()