# Usa a imagem oficial do PostgreSQL
FROM postgres:latest

# Instalação do psycopg2 para permitir conexões PostgreSQL
RUN apt-get update && apt-get install -y python3-psycopg2

# Variáveis de ambiente para configurar o PostgreSQL
ENV POSTGRES_DB=db_ada
ENV POSTGRES_USER=user_ada
ENV POSTGRES_PASSWORD=password_ada


# Volume nomeado
VOLUME /var/lib/postgresql/data
