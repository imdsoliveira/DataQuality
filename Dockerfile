FROM python:3.12

# Instala Poetry
RUN pip install poetry

COPY . /src
WORKDIR /src

# Muda o shell para Bash
SHELL ["/bin/bash", "-c"]

# Cria + ativa a venv e instala dependências em uma só camada
RUN python -m venv venv \
    && source venv/bin/activate \
    && pip install --upgrade pip \
    && poetry install --no-root

EXPOSE 8501

ENTRYPOINT ["poetry","run","streamlit","run","main.py","--server.port=8501","--server.address=0.0.0.0"]