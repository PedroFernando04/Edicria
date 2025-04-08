from editora.defs.defs_basicas import *

def menu_visualizar_livros_ano_lido(cursor, id_cliente):
    print("Como deseja filtrar:")
    print("\n1 - Crescente\n2 - Decrescente\n3 - Escolher ano\n")

    menu_ano = input()
    clear()

    #CRESCENTE
    if menu_ano == '1':
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
                    ORDER BY ano_lido_livro
                """
        cursor.execute(query, (id_cliente, ))
        
    #DECRESCENTE
    elif menu_ano == '2':
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
                    ORDER BY ano_lido_livro DESC
                """ 
        cursor.execute(query, (id_cliente, ))
        
    elif menu_ano == '3':

        query_ano = """
                        SELECT DISTINCT ano_lido_livro
                        
                        FROM editora.livros l
                            
                        WHERE id_cliente_livro = %s
                    """
        cursor.execute(query_ano, (id_cliente, ))

        anos = cursor.fetchall()

        while True:
            print("Selecione o ano:\n")

            for i in range(0, len(anos)):
                print(f"{i + 1} - {anos[i][0]}")
            
            try:
                ano = int(input("\n"))

                if ano not in range(1, len(anos) + 1):
                    raise Exception

                clear()
                
            except:
                clear()
                print("Valor inválido!")
                print("Digite um número presente na tabela\n")

            else:
                break
            
            if ano > 0 and ano <= len(anos):
                break
            else:
                continue

        
        query = """
                    SELECT nome_livro, nome_autor, nome_editora, 
                    data_de_lancamento_livro, nome_genero, nome_status, 
                    ano_lido_livro, nota_livro, resenha_livro
                    
                    FROM editora.livros l 
                    JOIN editora.autores a ON l.id_autor_livro = a.id_autor
                    JOIN editora.editoras e ON l.id_editora_livro = e.id_editora
                    JOIN editora.generos g ON l.id_genero_livro = g.id_genero
                    JOIN editora.status s ON l.id_status_livro = s.id_status

                    WHERE id_cliente_livro = %s AND ano_lido_livro = %s
                """ 
        cursor.execute(query, (id_cliente, anos[ano - 1][0]))
    