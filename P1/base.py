import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def connect(user, password, db, host='localhost', port=3306):
    try:
        url = 'mysql+pymysql://{}:{}@{}:{}/{}'
        url = url.format(user, password, host, port, db)
        print("connecting to url: " + url)
        engine = sqlalchemy.create_engine(url)
        try:
            engine.connect()
        # Handle the case if the database we are connecting to does not exist
        except:
            default_url = 'mysql+pymysql://{}:{}@{}:{}'
            default_url = default_url.format(user, password, host, port)
            con = sqlalchemy.create_engine(default_url)
            with con.connect() as conn:
                conn.execute("CREATE DATABASE " + db + ";")
        Session = sessionmaker(bind = engine)
        return engine, Session
    except Exception as e:
        print(e)
        raise e

engine, Session = connect('root', 'wozhenshigeshabi',"new_one")
Base = declarative_base()


