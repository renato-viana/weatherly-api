# Weather Data Analysis

Este projeto é uma aplicação web que utiliza Flask para exibir e manipular dados meteorológicos.

## Funcionalidades

- Exibe uma página inicial com uma tabela de dados meteorológicos.
- Faz requisições GET para obter dados meteorológicos de um cluster OpenSearch.
- Faz requisições POST para inserir novos dados meteorológicos no cluster OpenSearch.

## Como executar o projeto

Siga as etapas abaixo para configurar e executar o projeto:

1. **Clone o repositório**: Faça o clone do repositório usando o comando `git clone <url-do-repositório>` no terminal.

2. **Instale as dependências**: Navegue até a pasta do projeto e instale as dependências necessárias usando o comando `pip install -r requirements.txt`.

3. **Inicie os serviços com Docker**: Execute o comando `docker-compose up` para iniciar os serviços necessários usando Docker. Isso irá iniciar o OpenSearch e o OpenSearch Dashboard.

4. **Execute a aplicação**: Finalmente, inicie a aplicação Flask com o comando `flask run`. Certifique-se de que o ambiente virtual esteja ativado e que todas as variáveis de ambiente necessárias estejam configuradas.

Agora, você deve ser capaz de acessar a aplicação em `http://localhost:5000`.

## Rotas

- `GET /`: Retorna a página inicial com a tabela de dados meteorológicos.
- `GET /weather`: Retorna os dados meteorológicos do documento com ID 1 do índice `weather-data` do OpenSearch.
- `POST /weather`: Insere novos dados meteorológicos no índice `weather-data` do OpenSearch.

## Tecnologias utilizadas

- Flask: Um microframework para Python baseado em Werkzeug, Jinja 2 e boas intenções.
- OpenSearch: Um projeto de código aberto derivado do Elasticsearch 7.10.2, incluindo os recursos de pesquisa e análise de código aberto de Elasticsearch 7.10.2 e os painéis de visualização de dados de código aberto do Kibana 7.10.2.
- OpenSearch Dashboard: Uma plataforma de análise e visualização de dados de código aberto que permite visualizar, explorar e interagir com os dados do OpenSearch.
- Docker: Uma plataforma de código aberto que automatiza a implantação, o dimensionamento e a execução de aplicativos em contêineres.
- jQuery: Uma biblioteca JavaScript rápida, pequena e rica em recursos.
- DataTables: Um plug-in jQuery que adiciona controles de interação avançados a qualquer tabela HTML.

## Licença

Este projeto está licenciado sob a licença MIT.
