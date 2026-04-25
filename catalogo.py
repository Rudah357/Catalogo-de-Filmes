
import os, time, json
from datetime import date

ARQUIVO_DADOS = "meus_filmes.json"

def back():
    back = input("0 --> Back\n")
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def carregar_dados():
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except:
        print("Arquivo não existe! Criando lista vazia...")
        return []

def salvar_dados(dados):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def obter_ano_valido():
    while True:
        try:
            ano = int(input("Ano de lançamento: "))

            if ano < 1888 or ano > date.today().year:
                print("Por favor, ensira um ano realista.")
                continue
            
            return ano
        except ValueError:
            print("ERRO: Digite apenas números inteiros para o ano!")

def obter_nota_valida():
    while True:
        try:
            nota = float(input("Nota (0.0 a 5.0): "))

            if nota < 0.0 or nota > 5.0:
                print("ERRO: insira uma nota que esteja entre 0.0 e 5.0!")
                continue
            
            return nota
        except ValueError:
            print("ERRO: Digite um valor numérico (use ponto para decimais)!")

def adicionar_filmes(catalogo):
    limpar()
    print("———— REGISTRAR NOVO FILME ————\n")
    titulo = input("Título: ").strip()

    for filme in catalogo:
        if filme["titulo"].lower() == titulo.lower():
            print(f"\nERRO: O filme '{filme['titulo']}' já está cadastrado no seu catálogo!")
            return
        
    genero = input("Gênero (ex: Ação, Comédia e Drama): ").strip()
    ano = obter_ano_valido()
    nota = obter_nota_valida()
    critica = input("Breve crítica: ").strip()

    filme = {
        "titulo": titulo,
        "genero": genero,
        "ano": ano,
        "nota": nota,
        "critica": critica
    }

    catalogo.append(filme)
    salvar_dados(catalogo)
    print(f"🟢 '{titulo}' adicionado com sucesso ao seu catálogo!")

def remover_filme(catalogo):
    limpar()
    print("———— REMOVER FILME ————\n")
    filme_para_remover = input("Escreva o título do filme para remove-lo do catálogo: ").strip()

    if filme_para_remover not in catalogo:
        print("Filme não encontrado, tente novamente...")

    else:
        for filme_para_remover in catalogo:
            if filme_para_remover["titulo"].lower() == filme_para_remover.lower():
                lista_filmes.remove(filme_para_remover)
                print("\nFilme removido do catálogo com sucesso!")
        
def listar_filmes(catalogo):
    limpar()
    print("—" * 40)
    print("          MINHA COLEÇÃO")
    print("—" * 40)

    if not catalogo:
        print(" O seu catálogo está vazio.")
        print("—" * 40)
        return
    
    for filme in catalogo:
        estrelas = "⭐" * int(filme['nota'])
        genero = filme.get('genero', "Desconhecido")

        print(f"[{filme['ano']}] {filme['titulo'].upper()} ({genero}) | Nota: {filme['nota']:.1f} {estrelas}")
        print("—" * 40)

def pesquisar_por_titulo(catalogo):
    limpar()
    termo = input("Digite parte do titulo para pesquisar: ").strip().lower()

    resultados = []
    for filme in catalogo:
        if termo in filme['titulo'].lower():
            resultados.append(filme)

    _exibir_resultados_pesquisa(resultados)

def pesquisar_por_genero(catalogo):
    limpar()
    termo = input("Digite o gênero para pesquisar (ex: Ação): ").strip().lower()

    resultados = []
    for filme in catalogo:
        if termo in filme.get("genero", "").lower():
            resultados.append(filme)

    _exibir_resultados_pesquisa(resultados)

def pesquisar_por_ano(catalogo):
    limpar
    try:
        ano_pesquisa = int(input("Digite o ano de lançamento exato para pesquisar: ")).strip()
    except ValueError:
        print("ERRO: Digite um ano válido (número inteiro).")
        return
    
    resultados = []
    for filme in catalogo:
        if filme["ano"] == ano_pesquisa:
            resultados.append(filme)

    _exibir_resultados_pesquisa(resultados)

def _exibir_resultados_pesquisa(resultados):
    if resultados:
        print(f"\nEncontrados {len(resultados)} resultado(s):")

        for filme in resultados:
            genero = filme.get('genero', 'Desconhecido')
            print(f"> {filme['titulo']} ({filme['ano']}) - {genero} - Nota: {filme['nota']}")
    else:
        print("\nNenhum filme encontrado.") 


if __name__ == "__main__":
    lista_filmes = carregar_dados()
    pesquisar_por_ano(lista_filmes)