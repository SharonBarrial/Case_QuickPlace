# Usa una imagen base ligera de Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia todos los archivos del directorio actual al contenedor
COPY . .

# Instala las dependencias necesarias
RUN pip install flask pandas psutil

# Expone los puertos usados por las aplicaciones Flask
EXPOSE 5000
EXPOSE 8000

# Por defecto, ejecutará `app.py` (puedes sobrescribir esto en docker-compose.yml)
CMD ["python", "app.py"]
