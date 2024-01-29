import sys
import os
from cx_Freeze import setup, Executable

# Definir o que deve ser incluído na pasta final
arquivos = ['requirements.txt', 'instruções.txt']

# Saída dos arquivos
configuracao = Executable(
    script = 'main_final.py',
    icon = 'pen_edit_.ico'
)

# Configurar o CX-Freeze(detalhes do programa)
setup(
    name ='Bot EDP',
    version = '1.0',
    description = 'Esse programa renomeia os PDFs baixados da EDP',
    author = 'Adriano',
    options = {'build_exe': {'include_files': arquivos}},
    executables = [configuracao] 
)

# python setup.py build