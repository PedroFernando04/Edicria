from editora.defs.defs_basicas import *

def menu_visualizar_livros_nome(cursor, id_cliente, nome):
    query_nome = """
                    SELECT nome_livro, nome_autor, nome_editora, 
                        data_de_lancamento_livro, nome_genero, nome_status, 
                        ano_lido_livro, nota_livro, resenha_livro

                    FROM editora.livros l 
                    JOIN editora.autores a ON l.id_autor_livro = a.id_autor
                    JOIN editora.editoras e ON l.id_editora_livro = e.id_editora
                    JOIN editora.generos g ON l.id_genero_livro = g.id_genero
                    JOIN editora.status s ON l.id_status_livro = s.id_status
                    
                    WHERE id_cliente_livro = %s AND nome_livro ILIKE %s
                    ORDER BY id_livro
                """
    nome_param = f"%{nome}%"  # Adiciona os curingas
    cursor.execute(query_nome, (id_cliente, nome_param))
     