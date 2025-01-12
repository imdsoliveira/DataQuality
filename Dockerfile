FROM python:3.12

# Expõe a porta
EXPOSE 8501

# Atualiza o pip e instala Poetry
RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Atualiza pip e instala Poetry
RUN pip install --upgrade pip
RUN pip install poetry

# Copia os arquivos do projeto
WORKDIR /dataquality
COPY . /dataquality

# Instala as dependências (sem tentar instalar o “root package”)
RUN poetry install --no-root

# Expõe a porta e executa o Streamlit
EXPOSE 8501
ENTRYPOINT ["poetry","run","streamlit","run","app/main.py","--server.port=8501", "--server.address=0.0.0.0" ]