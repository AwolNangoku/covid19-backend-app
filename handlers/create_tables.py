import psycopg2
from dbConn import dbConnect


def create_tables():
    tables = ("""
        CREATE TABLE IF NOT EXISTS countries_table(
        country_id SERIAL PRIMARY KEY,
        country VARCHAR (100) UNIQUE,
        confirmed INT,
        deaths INT,
        recovered INT,
        population INT,
        continent VARCHAR (100)
    )
    """, """
        CREATE TABLE IF NOT EXISTS provinces_table(
        province_id SERIAL PRIMARY KEY,
        province VARCHAR (100) UNIQUE,
        country_id INT,
        confirmed INT,
        deaths INT,
        recovered INT,
        updated VARCHAR (100),
        CONSTRAINT fk_country
            FOREIGN KEY(country_id)
	        REFERENCES countries_table(country_id)
    )
    """)

    pg_conn = None
    try:
        pg_conn = dbConnect()
        pg_cursor = pg_conn.cursor()

        # create tables
        for table in tables:
            pg_cursor.execute(table)

        pg_cursor.close()
        pg_conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if pg_conn is not None:
            pg_conn.close()
