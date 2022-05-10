import psycopg2


def dbConnect():
    # Establish database connection
    try:
        dbConnection = psycopg2.connect(
            database="covidlivecasesdb",
            user="postgres",
            password="1234")

        print('DB connected...')
        return dbConnection
    except (Exception, psycopg2.DatabaseError) as error:
        print('Failed connecting to db...', error)
