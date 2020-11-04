from psycopg2 import OperationalError
from psycopg2.pool import SimpleConnectionPool
from os import getenv

# TODO(developer): specify SQL connection details
# TODO encrypt password
CONNECTION_NAME = getenv('INSTANCE_CONNECTION_NAME', 'fullcourt-1227c:us-east1:fullcourt')
DB_USER = getenv('POSTGRES_USER', 'postgres')
DB_PASSWORD = getenv('POSTGRES_PASSWORD', 'watchdog')
DB_NAME = getenv('POSTGRES_DATABASE', 'postgres')
PASSWORD_FILE = 'passwords.txt'

PG_CONFIG = {
    'user': DB_USER,
    'password': DB_PASSWORD,
    'dbname': DB_NAME
}

# Connection pools reuse connections between invocations,
# and handle dropped or expired connections automatically.
PG_POOL = None

def postgres_init():
    """
    Initialize connection to DB
    """

    def __connect(host):
        """
        Helper function to connect to Postgres
        """
        global PG_POOL
        PG_CONFIG['host'] = host
        PG_POOL = SimpleConnectionPool(1, 1, **PG_CONFIG)

    global PG_POOL

    # Initialize the pool lazily, in case SQL access isn't needed for this
    # GCF instance. Doing so minimizes the number of active SQL connections,
    # which helps keep your GCF instances under SQL connection limits.
    if not PG_POOL:
        try:
            __connect('/cloudsql/{CONNECTION_NAME}')
        except OperationalError:
            # If production settings fail, use local development ones
            __connect('127.0.0.1')

    # Remember to close SQL resources declared while running this function.
    # Keep any declared in global scope (e.g. pg_pool) for later reuse.


def current_time():
    """
    Get current time from postgres db
    """

    global PG_POOL
    conn = PG_POOL.getconn()

    with conn.cursor() as cursor:
        cursor.execute('SELECT NOW();')
        results = cursor.fetchone()
        PG_POOL.putconn(conn)
    return results[0]


"""
import sqlalchemy
conn = psycopg2.connect(
	host="104.196.196.66", 
	dbname="fullcourt", 
	user="postgres", 
	password="watchdog",
	sslmode="require",
	sslcert="cert/client-cert.pem",
	sslkey="cert/client-key.pem")
"""

# eng = sqlalchemy.create_engine('postgresql:///fullcourt')
# con = eng.connect()

postgres_init()
