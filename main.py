from tika import parser
import re
import os
import glob
# from lista_condominios import lista_condominios

print('Iniciando o pograma')

print()

# Solicitar entrada para a lista de condomínios em formato de lista de dicionários
entrada_usuario = input('Digite a lista de condomínios no formato [{\'nome\': [\'cnpj\', instalação]}, ...]: ')
lista_condominios = eval(entrada_usuario)

print()

caminho_download = input('Informe o caminho para seus arquivos: ')

print()

# Lista todos os arquivos PDF no caminho fornecido
arquivos_pdf = glob.glob(os.path.join(caminho_download, "*.pdf"))

for caminho_arquivo in arquivos_pdf:
    # Lendo o arquivo PDF
    raw = parser.from_file(caminho_arquivo)

    # Extraindo o conteúdo do PDF
    texto = raw['content']

    # Variáveis para armazenar os resultados
    nome = None
    instalacao = None

    # Iterando sobre a lista de condomínios
    for condominio in lista_condominios:
        for chave, valores in condominio.items():
            # Verificando se a chave e o valor estão no texto
            if re.search(chave, texto, re.IGNORECASE) and re.search(str(valores[1]), texto):
                # Se a chave e o valor forem encontrados, armazene a chave e o valor2 nas variáveis nome e instalacao
                nome = chave
                instalacao = valores[1]
                break

    # Imprimindo os resultados
    print(f'Nome: {nome}')
    print(f'Instalação: {instalacao}')

    # Renomeando o arquivo
    if nome and instalacao:
        # Criando o novo nome do arquivo
        novo_nome = f"{nome} - {instalacao}.pdf"

        # Obtendo o diretório do arquivo original
        diretorio = os.path.dirname(caminho_arquivo)

        # Criando o novo caminho do arquivo
        novo_caminho = os.path.join(diretorio, novo_nome)

        # Renomeando o arquivo
        os.rename(caminho_arquivo, novo_caminho)

print()
print('Programa encerrado confira se os arquivos foram renomeados')
