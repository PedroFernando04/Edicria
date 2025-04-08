from editora.defs.defs_basicas import *
from editora.biblioteca.cadastrar_livros import cadastro_livro

def alterar_status(id_livro, conn):
    cursor = conn.cursor()

    query_select =  """
                        SELECT nome_livro, id_status_livro, nome_status
                        FROM editora.livros l
                        JOIN editora.status s ON l.id_status_livro = s.id_status
                        WHERE id_livro = %s
                    """
    cursor.execute(query_select, (id_livro, ))
    livro = cursor.fetchall()

    print(f"Seu livro \"{livro[0][0]}\" possui o status \"{livro[0][2]}\"")
    print("\nInforme o novo status do livro:\n")
    query_status =  """
                        SELECT id_status, nome_status
                        FROM editora.status
                    """
    cursor.execute(query_status)
    status_válidos = cursor.fetchall()

    while True:
        for i in range(0, len(status_válidos)):
            print(f"{i + 1} - {status_válidos[i][1]}")

        novo_status = int(input("\n"))
        if novo_status in range(1, len(status_válidos) + 1):
            break
        else:
            clear()
            print("Valor inválido!")
            print("Informe um dos valores da tabela\n")
    
    if novo_status != 1:
        query_novo_status = """
                                UPDATE editora.livros
                                SET id_status_livro = %s
                                WHERE id_livro = %s
                            """
        cursor.execute(query_novo_status, (novo_status, id_livro))
        conn.commit()   
    else:
        clear()
        print("Que bom que finalzou este livro!")
        print("Agora vamos registrar suas opiniões sobre ele!\n")
        ano = cadastro_livro.ano_lido_livro(2025)
        nota = cadastro_livro.nota_livro()
        resenha = cadastro_livro.resenha_livro()

        query_lido =   """
                            UPDATE editora.livros
                            SET nota_livro = %s,
                                resenha_livro = %s, 
                                ano_lido_livro = %s,
                                id_status_livro = %s
                            WHERE id_livro = %s
                        """
        cursor.execute(query_lido, (nota, resenha, ano, novo_status, id_livro))
        conn.commit() 
    

    clear()
    input("Alterção realizada com sucesso!")
    clear()