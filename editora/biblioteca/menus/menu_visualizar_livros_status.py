from editora.defs.defs_basicas import *

def menu_visualizar_livros_status(cursor, id_cliente):

    print("Escolha o status que deseja visualizar:")

    query_tipos_status = """
                            SELECT id_status, nome_status
                            FROM editora.status
                         """
    cursor.execute(query_tipos_status)
    status_válidos = cursor.fetchall()

    ids_válidos = []
    while True:
        for i in range(0, len(status_válidos)):
            print(f"{status_válidos[i][0]} - {status_válidos[i][1]}")
            ids_válidos.append(str(status_válidos[i][0]))
            

        menu_status = input()

        if menu_status in ids_válidos:
            clear()
            break
        
        else:
            clear()
            print("Valor inválido!")
            print("Informe um valor presente na tabela\n")

    query = """
                SELECT nome_livro, nome_autor, nome_editora, 
                data_de_lancamento_livro, nome_genero, nome_status, 
                ano_lido_livro, nota_livro, resenha_livro
                
                FROM editora.livros l 
                JOIN editora.autores a ON l.id_autor_livro = a.id_autor
                JOIN editora.editoras e ON l.id_editora_livro = e.id_editora
                JOIN editora.generos g ON l.id_genero_livro = g.id_genero
                JOIN editora.status s ON l.id_status_livro = s.id_status

                WHERE id_cliente_livro = %s and id_status_livro = %s
                ORDER BY id_livro
            """
    cursor.execute(query, (id_cliente, menu_status))