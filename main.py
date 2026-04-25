
import json, os, time, catalogo

def mostrar_menu():
    catalogo.limpar()
    print("——————————————————————————————————————————")
    print("              💠 CineLog                 ")
    print("——————————————————————————————————————————\n")
    print("1- Adicionar filmes")
    print("2- Ver lista de filmes")
    print("3- Pesquisar filme por nome")
    print("4- Pesquisar filmes por gênero")
    print("5- Pesquisar filmes por ano")
    print("6- Sair\n")
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
                catalogo.listar_filmes(meus_filmes)
                catalogo.back()

            case "3":
                catalogo.pesquisar_por_titulo(meus_filmes)
                catalogo.back()

            case "4":
                catalogo.pesquisar_por_genero(meus_filmes)
                catalogo.back()

            case "5":
                catalogo.pesquisar_por_ano(meus_filmes)
                catalogo.back()

            case "6":
                catalogo.limpar()
                print("Encerrando e salvando programa...")
                break

            case _:
                print("ERRO: Opção inválida, tente novamente...")
                catalogo.back()
                continue

if __name__ == "__main__":
    iniciar_app()