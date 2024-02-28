# Usa a imagem oficial do python
FROM python:3.8

# Define o diretória de trabalho da imagem
WORKDIR /app

# Copia os arquivos da pasta atual para o diretório de trabalho
# No caso os arquivos app.py, requirements.txt, Dockerfile e a pasta templates
COPY . .

# Instala as pendências necessárias como Flask
RUN pip install -r requirements.txt

# Expõe a porta que a aplicação Flask está sendo executada
EXPOSE 5000

# Comando para executar a aplicação qunado o contêiner for executado
CMD ["python","app.py"]