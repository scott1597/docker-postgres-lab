FROM python:3.11-slim

# Evita archivos .pyc y habilita logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Crea un usuario sin privilegios de root (buena práctica de seguridad)
RUN useradd --create-home appuser
WORKDIR /home/appuser/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=appuser:appuser main.py .

USER appuser
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
