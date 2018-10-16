from sqlalchemy import Column, String, Integer, Date, MetaData, Table, ForeignKey
from base import Base, engine

metadata = MetaData()

reserve = Table('reserves', metadata,
        Column('sid', Integer, primary_key=True),
        Column('bid', Integer, primary_key=True),
        Column('day', Date, primary_key=True),
        Column('cost',Integer,primary_key=True))

sailors = Table('sailors', metadata,
        Column('sid', Integer, primary_key=True),
        Column('sname', String(30)),
        Column('rating', Integer),
        Column('age', Integer))

boats = Table('boats', metadata,
        Column('bid', Integer, primary_key=True),
        Column('bname', String(20)),
        Column('color', String(10)),
        Column('length', Integer))

employees = Table('employees', metadata,
             Column('eid', Integer, primary_key=True),
             Column('ename', String(20)),
             Column('salary', Integer)) #Salary is intepreted as $XXX/hour

hours = Table('hours', metadata,
             Column('day', Date, primary_key=True),
             Column('employees_eid', Integer,ForeignKey('employees.eid'),primary_key=True),
             Column('hours', Integer))

cost_record = Table('cost_record', metadata,
             Column('cid', Integer, primary_key=True),
             Column('boat_id', Integer, ForeignKey('boats.bid')),
             Column('employees_eid', Integer, ForeignKey('employees.eid')),
             Column('cost', Integer),
             Column('day', Date))



if __name__ == '__main__':
    #clear and create the schema
    metadata.drop_all(engine)
    metadata.create_all(engine)
    #insert with raw SQL lines
    with engine.connect() as conn:
        with open('../input2.txt', 'r') as lines:
            for line in lines:
                line = line.strip('\n')
                conn.execute(line)

    """ Another way to import instead of using raw SQL lines """
    with engine.connect() as conn:
        conn.execute(employees.insert(), [
            {'eid': 1, 'ename': 'iris', 'salary': 15},
            {'eid': 2, 'ename': 'leo', 'salary': 14},
            {'eid': 3, 'ename': 'leoon', 'salary': 12},
            {'eid': 4, 'ename': 'justin', 'salary': 13}
        ])
        conn.execute(hours.insert(), [
            {'day': '1998/10/10', 'employees_eid': 1, 'hours': 5},
            {'day': '1998/10/10', 'employees_eid': 2, 'hours': 3},
            {'day': '1998/10/10', 'employees_eid': 3, 'hours': 8},
            {'day': '1998/10/10', 'employees_eid': 4, 'hours': 6}
        ])
        conn.execute(cost_record.insert(), [
            {'cid': 1, 'boat_id': 101, 'employees_eid': 1, 'cost': 50, 'day': '1998/10/10'},
            {'cid': 2, 'boat_id': 102, 'employees_eid': 2, 'cost': 50, 'day': '1998/10/10'},
            {'cid': 3, 'boat_id': 103, 'employees_eid': 3, 'cost': 80, 'day': '1998/10/10'},
            {'cid': 4, 'boat_id': 104, 'employees_eid': 4, 'cost': 100, 'day': '1998/10/10'},
            {'cid': 5, 'boat_id': 102, 'employees_eid': 4, 'cost': 100, 'day': '1998/10/10'}
        ])


