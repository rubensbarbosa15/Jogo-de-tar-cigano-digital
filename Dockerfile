# Use uma imagem de base como ponto de partida
FROM postgres

# Defina variáveis de ambiente e outras configurações
ENV POSTGRES_USER tarot_user
ENV POSTGRES_PASSWORD tarot_password
ENV POSTGRES_DB tarot_db
ENV <NOME_VAR> <VALOR>

# Copie arquivos para dentro do contêiner
COPY init.sql /docker-entrypoint-initdb.d/

# Execute comandos dentro do contêiner
RUN <comando>

# Especifique o comando a ser executado quando o contêiner for iniciado
CMD ["<comando>", "<argumento>"]
