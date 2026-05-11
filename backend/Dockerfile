# Utiliser une image Python legere
FROM python:3.10-slim

# Empecher Python de generer des fichiers .pyc et forcer l'affichage des logs
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Installer les dependances systäme necessaires pour psycopg2 (Postgres)
RUN apt-get update && apt-get install -y libpq-dev gcc

# Installer les dependances Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code
COPY . /app/

# Lancer le serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
