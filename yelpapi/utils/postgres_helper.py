"""
@author: Harsh Desai
@date: 09/12/19
@description: Simple wrapper functions for PostgreSQL pyscopg2 python api
"""
import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv, find_dotenv


def create_connection(env_file_path=None, verbose=False):
    """ Create a database connection to a Postgres database local or remote
    Parameter
    --------------------------------------------------------
    env_file_path: str
                environment file path
    verbose: bool
                prints detail output of connection
     """

    # Validates loading of .env file
    if env_file_path is None:
        if load_dotenv():
            if verbose:
                print('Environment file loaded successfully...')
    else:
        if not os.path.isfile(env_file_path):
            raise IOError('Invalid File Path')
        if load_dotenv(dotenv_path=env_file_path):
            if verbose:
                print(
                    f'Environment file {env_file_path} loaded successfully...')
        else:
            if not load_dotenv(find_dotenv()):
                raise EnvironmentError(f'!!! Error loading {env_file_path}')

    # Connects to PostgreSQL database local or remote
    pg_conn = None
    dbname = os.environ.get('db_name')
    user = os.environ.get('username')
    password = os.environ.get('password')
    host = os.environ.get('host')

    if verbose:
        print(f'Using psycopg2 version: {psycopg2.__version__}')
        print(f'Creating Connection to {dbname}, {user}@{host}...')

    try:
        pg_conn = psycopg2.connect(dbname=dbname, user=user,
                                   password=password, host=host)
        if verbose:
            pg_curs = pg_conn.cursor()
            pg_curs.execute('SELECT version()')
            db_version = pg_curs.fetchone()
            print('PostgreSQL database version: {}'.format(
                db_version))
        return pg_conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def select_query(pg_conn, query):
    """
    Query all rows in the database table
    Parameter
    -------------------------------------------------------
    pg_conn : connection
                postgres database connection object
    Returns
    --------------------------------------------------------
    df : Pandas DataFrame
            returns results as pandas dataframe
    """
    if not query.startswith('SELECT'):
        raise ValueError('Query should begin with `SELECT`')

    pg_curs = pg_conn.cursor()
    pg_curs.execute(query)

    df = pd.read_sql(query, pg_conn)
    return df


def get_sql_tables(pg_conn):
    """
    Get SQL tables from the PostgreSQL database
    Parameter
    -------------------------------------------------------
    pg_conn : connection
            postgres database connection object
    Returns
    --------------------------------------------------------
    tables : Pandas DataFrame
            returns results as pandas dataframe
    """
    show_tables = """
    SELECT
    *
    FROM
    pg_catalog.pg_tables
    WHERE
    schemaname != 'pg_catalog'
    AND schemaname != 'information_schema';
    """
    tables = pd.read_sql(show_tables, pg_conn)
    return tables


def get_table_info(pg_conn, table_name):
    """
    Get table info, like data types from PostgreSQL database
    Parameter
    -------------------------------------------------------
    pg_conn :connection
            postgres database connection object
    Returns
    --------------------------------------------------------
    result : Pandas DataFrame
            returns results as pandas dataframe
    """
    table_info = f"PRAGMA table_info({table_name});"
    result = pd.read_sql(pg_conn, table_info)
    return result