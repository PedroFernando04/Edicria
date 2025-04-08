from editora.defs.defs_basicas import *


def alterar_nota(id_livro, conn):
    cursor = conn.cursor()

    query_select =  """
                        SELECT nome_livro, nota_livro
                        FROM editora.livros l
                        WHERE id_livro = %s
                    """
    cursor.execute(query_select, (id_livro, ))
    livro = cursor.fetchall()

    print(f"Seu livro {livro[0][0]} está com nota {livro[0][1]}")
    print("\nInforme a nova nota do livro:\n")

    while True:

        nova_nota = float(input())
        if nova_nota >= 0 and nova_nota <= 10:
            break
        else:
            clear()
            print("Valor inválido!")
            print("Informe um valor entre 0 e 10\n")
    

    query_nova_nota =   """
                            UPDATE editora.livros l
                            SET nota_livro = %s
                            WHERE id_livro = %s
                        """
    cursor.execute(query_nova_nota, (nova_nota, id_livro))
    conn.commit() 

    clear()
    input("Alterção realizada com sucesso!")
    clear()