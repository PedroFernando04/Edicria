from editora.cadastro.data.visualizar_data import visualizar_data
import textwrap

def visualizar_livros(livros):

    if livros:
        for livro in livros:
            info_livro = (
                livro[0],
                livro[1],
                livro[2],
                livro[3],
                livro[4],
                livro[5],
                livro[6],
                livro[7],
                livro[8]
            )

            (nome, autor, editora, data_lancamento, genero, status, ano_lido, nota, resenha) = info_livro

            if status == 'Lido':
                print("-"*120)
                print(f"Nome: {nome}")
                print(f"Autor(a): {autor}")
                print(f"Editora: {editora}")
                print(f"Data de Lançamento: {visualizar_data(data_lancamento)}")
                print(f"Gênero: {genero}")
                print(f"Status: {status}")
                print(f"Ano lido: {ano_lido}")
                print(f"Nota: {nota}")
                print(f"Resenha:")
                if resenha is None:
                    print(" ")
                else:
                    resenha_formatada = textwrap.fill(resenha, width=120)
                    print(f"\n{resenha_formatada}\n")

                print("-"*120)

            else:

                print("-"*120)
                print(f"Nome: {nome}")
                print(f"Autor(a): {autor}")
                print(f"Editora: {editora}")
                print(f"Data de Lançamento: {visualizar_data(data_lancamento)}")
                print(f"Gênero: {genero}")
                print(f"Status: {status}")
                print("-"*120)

    else:
        print("Nenhum livro cadastrado!")