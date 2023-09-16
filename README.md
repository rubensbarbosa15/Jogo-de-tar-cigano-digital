# Jogo-de-tar-cigano-digital
Aplicativo de Cadastro e Listagem de Usuários para Jogo de Tarô
Este é um aplicativo simples para cadastrar e listar usuários para um jogo de tarô. Ele usa Flask como framework web e PostgreSQL como banco de dados.

Configuração do Ambiente
Certifique-se de que você tenha Python e Docker instalados em seu sistema. Além disso, verifique se o Docker Compose está disponível.

Configuração do Banco de Dados
O banco de dados PostgreSQL é usado para armazenar os dados dos usuários. Para configurar o banco de dados, siga estas etapas:

Crie um arquivo chamado .env na raiz do projeto e defina as variáveis de ambiente para o banco de dados, conforme necessário:

makefile
Copy code
POSTGRES_USER=seu_usuario
POSTGRES_PASSWORD=sua_senha
POSTGRES_DB=tarot_db
Substitua seu_usuario e sua_senha pelas credenciais desejadas.

Crie um arquivo SQL chamado init.sql na pasta raiz do projeto. Este arquivo será usado para criar a estrutura inicial do banco de dados. Você pode usar o conteúdo do arquivo init.sql fornecido neste projeto como um exemplo.

Use o Docker Compose para iniciar o banco de dados PostgreSQL:

Copy code
docker-compose up -d postgres
Isso criará um contêiner Docker com o PostgreSQL usando as configurações definidas no arquivo docker-compose.yml.

Execute as migrações do banco de dados:

bash
Copy code
docker-compose exec web python manage.py db upgrade
Isso aplicará as migrações e criará as tabelas necessárias no banco de dados.

Executando o Aplicativo
Para executar o aplicativo, siga estas etapas:

Construa a imagem Docker do aplicativo:

Copy code
docker-compose build
Inicie o aplicativo com Docker Compose:

Copy code
docker-compose up
O aplicativo estará disponível em http://localhost:5000 no seu navegador.

Uso do Aplicativo
O aplicativo possui duas rotas principais:

/: Página inicial com um formulário de cadastro de usuário.
/listar: Página que lista todos os usuários cadastrados.
Para cadastrar um usuário, preencha o formulário na página inicial. Após o cadastro, você verá uma mensagem de boas-vindas e o usuário será adicionado ao banco de dados.

Na página de listagem, você pode visualizar todos os usuários cadastrados.

Contribuição
Sinta-se à vontade para contribuir com este projeto, reportar problemas ou sugerir melhorias.
