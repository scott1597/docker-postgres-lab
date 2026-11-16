import os
import psycopg2
from fastapi import FastAPI, HTTPException

app = FastAPI(title="DevOps Lab API")

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        database=os.getenv("DB_NAME", "devops_db"),
        user=os.getenv("DB_USER", "devops_user"),
        password=os.getenv("DB_PASSWORD", "secret"),
        port=os.getenv("DB_PORT", "5432")
    )

@app.get("/")
def read_root():
    return {"status": "online", "service": "FastAPI + PostgreSQL DevOps Lab"}

@app.get("/health")
def health_check():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()[0]
        cur.close()
        conn.close()
        return {"status": "healthy", "database": db_version}
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Database connection failed: {str(e)}")
