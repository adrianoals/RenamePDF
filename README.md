# Projeto de Renomeação de PDFs

## Descrição
Este projeto consiste em um script Python desenvolvido para automatizar a tarefa de renomear arquivos PDF para uma administradora de condomínios. 
O objetivo é organizar os documentos de forma mais eficiente, facilitando o acesso e a gestão dos mesmos. O script extrai informações de uma 
planilha do Excel contendo uma lista de condomínios e utiliza essas informações para renomear os arquivos PDF correspondentes.

## Funcionalidades
- **Renomeação Automática de PDFs:** Extrai informações de uma planilha do Excel e renomeia arquivos PDF de acordo com esses dados.

## Instruções de Uso
1. Informe o caminho relativo da planilha que contém a lista de condomínios. Exemplo: `C:\\Users\\usuario\\Downloads`.
2. Informe em qual aba da planilha irá extrair as informações.
3. Informe o caminho onde estão os arquivos PDF que serão renomeados.

**Observações:**
- Ao digitar o caminho, não coloque as aspas `" "`.
- A planilha deve manter uma configuração padrão para que o programa possa ler e entender a lista de condomínios.
- O programa acusará erro caso haja arquivos repetidos no diretório onde os arquivos estão.

## Dependências
O projeto requer as seguintes bibliotecas Python, que estão listadas no arquivo `requirements.txt`:

