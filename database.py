import psycopg2

try:
    
    connection = psycopg2.connect(
        dbname="TrackIt",
        user="postgres",
        password="password",
        host="localhost",
        port="5432"
    )

    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"PostgreSQL verzió: {db_version}")

    cursor.close()
    connection.close()

except Exception as e:
    print(f"Hiba történt: {e}")
