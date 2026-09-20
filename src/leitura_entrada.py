# Lê o arquivo da matriz e devolve os pontos
def ler_entrada(caminho_arquivo):
        try:
            # Abre o arquivo para leitura e o fecha automaticamante
            with open(caminho_arquivo, "r", encoding="utf-8") as f:

                # Leitura da linha do arquivo, remoção de espaços e converção para inteiro
                primeira_linha = f.readline()
                limpeza_espacos = primeira_linha.strip() 
                lista_linha_coluna = limpeza_espacos.split()
                qtd_linhas = int(lista_linha_coluna[0])
                qtd_colunas = int(lista_linha_coluna[1]) 

                # Criação do dicionário 
                locais = {}

                # Percorre as linhas restantes do arquivo e obtém o índice 
                for indice1, linha in enumerate(f):
                    limpeza_espacos2 = linha.strip()
                    lista_linhas_restantes = limpeza_espacos2.split()

                    # Obtém o índice das colunas
                    for indice2, i in enumerate(lista_linhas_restantes):
                        if i == "0":
                            pass
                        else:
                            locais[i] = (indice1, indice2)

                # Criação da lista sem o ponto de origem "R"
                lista_chaves = [chave for chave in locais if chave != "R"] 

                # Retorna todas as coordenadas e a lista dos pontos de entrega
                return locais, lista_chaves

        except FileNotFoundError:
            print("O arquivo solicitado não foi encontrado.")
            locais = lista_chaves = None
            return locais, lista_chaves 
            
todos_os_pontos, chaves = ler_entrada("entradas/exemplo1.txt") 