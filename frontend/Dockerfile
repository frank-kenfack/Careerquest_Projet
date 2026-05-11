FROM node:18-alpine

WORKDIR /app

# Copier les fichiers de dependances
COPY package*.json ./

# Installer les d‚pendances
RUN npm install

# Copier le reste du code
COPY . .

# Exposer le port de Vite
EXPOSE 5173

# Lancer Vite en mode host pour permettre l'acces depuis l'exterieur du conteneur
CMD ["npm", "run", "dev", "--", "--host"]
