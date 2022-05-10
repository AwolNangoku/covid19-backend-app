import psycopg2

from dbConn import dbConnect


def fetch_countries():
    pg_conn = None
    listOfCountries = list()
    try:
        pg_conn = dbConnect()
        pg_cursor = pg_conn.cursor()
        pg_cursor.execute(
            "SELECT * FROM countries_table"
        )

        dbCountries = pg_cursor.fetchall()

        for country in dbCountries:
            listOfCountries.append(dict(
                id=country[0],
                country=country[1],
                confirmed=country[2],
                deaths=country[3],
                recovered=country[4],
                population=country[5],
                continent=country[6]
            ))

        pg_cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if pg_conn is not None:
            pg_conn.close()

    return listOfCountries
