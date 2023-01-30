# desafio2_backend
A Aplicação consiste em parsear arquivos de texto(CNBA) e salvar suas informações  em uma base de dados. 

## Tecnologias Utilizadas

 - Python 
 - Django
 - DjangoRestFrameWork


## Configurando o Ambiente de Desenvolvimento

Para configurar o ambiente de desenvolvimento, você precisará criar um ambiente virtual (VENV) e instalar as dependências necessárias.

### Criando o Ambiente Virtual (VENV)

1. Abra o terminal e navegue até a pasta onde deseja criar o ambiente virtual.
2. Execute o comando "python -m venv nome_do_ambiente" para criar o ambiente virtual. Por exemplo, "python -m venv myenv".
3. Ative o ambiente virtual usando o comando "nome_do_ambiente\Scripts\activate" (Windows) ou "source nome_do_ambiente/bin/activate" (Mac/Linux).

### Instalando as Dependências

1. Dentro do ambiente virtual ativado, execute o comando "pip install -r requirements.txt" para instalar todas as dependências especificadas em seu arquivo requirements.txt.

## Rodando a Aplicação

1. Dentro do ambiente virtual ativado, execute o comando "python manage.py runserver" para iniciar o servidor.
2. Acesse "http://127.0.0.1:8000/" no seu navegador para verificar se a aplicação está funcionando corretamente.

## Observação:
Para listar as dependencias é necessario criar um arquivo chamado requirements.txt e adicionar as dependencias lá com o comando "pip freeze > requirements.txt" no terminal
