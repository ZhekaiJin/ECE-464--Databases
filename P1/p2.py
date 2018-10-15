from sqlalchemy import Column, String, Integer, Date, MetaData, Table
from base import Base, engine

metadata = MetaData()

reserve = Table('reserves', metadata,
        Column('sid', Integer, primary_key=True),
        Column('bid', Integer, primary_key=True),
        Column('day', Date, primary_key=True),
)

sailors = Table('sailors', metadata,
        Column('sid', Integer, primary_key=True),
        Column('sname', String(30)),
        Column('rating', Integer),
        Column('age', Integer),
)

boats = Table('boats', metadata,
        Column('bid', Integer, primary_key=True),
        Column('bname', String(20)),
        Column('color', String(10)),
        Column('length', Integer),
)



if __name__ == '__main__':
    #clear and create the schema
    metadata.drop_all(engine)
    metadata.create_all(engine)
    #insert with raw SQL lines
    with engine.connect() as conn:
        with open('./input.txt', 'r') as lines:
            for line in lines:
                line = line.strip('\n')
                conn.execute(line)

    """ Another way to import instead of using raw SQL lines """
    # with engine.connect() as conn:
    #     conn.execute(sailors.insert(), [
    #         {'sid': 22, 'sname': 'dusting','rating': 7, 'age': 45.0},
    #         {'sid': 29, 'sname': 'brutus','rating': 1, 'age': 33.0},
    #         {'sid': 31, 'sname': 'lubber','rating': 8, 'age': 55.5},
    #         {'sid': 32, 'sname': 'andy','rating': 8, 'age': 25.5},
    #         {'sid': 58, 'sname': 'rusty','rating': 10, 'age': 35.0},
    #         {'sid': 64, 'sname': 'horatio','rating': 7, 'age': 16.0},
    #         {'sid': 71, 'sname': 'zorba','rating': 10, 'age': 35.0},
    #         {'sid': 74, 'sname': 'horatio','rating': 9, 'age': 25.5},
    #     ])

