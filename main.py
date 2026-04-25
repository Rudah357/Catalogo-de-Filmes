
import json, os, time, catalogo

def mostrar_menu():
    catalogo.limpar()
    print("——————————————————————————————————————————")
    print("              💠 CineLog                 ")
    print("——————————————————————————————————————————\n")
    print("1- Adicionar filmes")
    print("2- Remover filme do catálogo")
    print("3- Ver lista de filmes")
    print("4- Pesquisar filme por nome")
    print("5- Pesquisar filmes por gênero")
    print("6- Pesquisar filmes por ano")
    print("7- Sair\n")
    print("——————————————————————————————————————————")
    
def iniciar_app():
    meus_filmes = catalogo.carregar_dados()

    while True:
        mostrar_menu()
        opcao = input ("Escolha uma opção: ")

        match opcao:
            case "1":
                catalogo.adicionar_filmes(meus_filmes)
                catalogo.back()

            case "2":
                catalogo.remover_filme(meus_filmes)
                catalogo.back()

            case "3":
                catalogo.listar_filmes(meus_filmes)
                catalogo.back()

            case "4":
                catalogo.pesquisar_por_titulo(meus_filmes)
                catalogo.back()

            case "5":
                catalogo.pesquisar_por_genero(meus_filmes)
                catalogo.back()

            case "6":
                catalogo.pesquisar_por_ano(meus_filmes)
                catalogo.back()

            case "7":
                catalogo.limpar()
                print("Encerrando e salvando programa...")
                break

            case _:
                print("ERRO: Opção inválida, tente novamente...")
                catalogo.back()
                continue

if __name__ == "__main__":
    iniciar_app()