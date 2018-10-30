import pytest
from sqlalchemy import Column, String, Integer, Date, MetaData, ForeignKey, desc, func
from base import Base, engine, Session



#################### ORM ########################
metadata = MetaData()

class Boats(Base):
    __tablename__ = 'boats'

    bid = Column(Integer, primary_key=True)
    bname = Column(String)
    color = Column(String)
    length = Column(Integer)

class Sailors(Base):
    __tablename__ = 'sailors'

    sid = Column(Integer, primary_key=True)
    sname = Column(String)
    rating = Column(Integer)
    age = Column(Integer)

class Reserves(Base):
    __tablename__ = 'reserves'

    sid = Column(Integer, ForeignKey('sailors.sid'), primary_key=True)
    bid = Column(Integer, ForeignKey('boats.bid'), primary_key=True)
    day = Column(Date, primary_key=True)

#################### TEST ########################
def custom_assert(raw_query, api_query):
    #convert ResultProxy result from excute() to list to compare with Query object
    raw_list = []
    api_list = []
    with engine.connect() as conn:
        result = conn.execute(raw_query)
        for x in result:
            raw_list.append(x)
    #print(raw_list)
    for x in api_query:
        api_list.append(x)
    #print(api_list)
    assert raw_list == api_list

session = Session()


def test_query5():
    api_q5 = session.query(Reserves.bid, func.count('*').label('c')).group_by(Reserves.bid).order_by(desc('c')).limit(1)
    raw_q5 = "select bid, res.c from (select bid, count(*) as c from reserves group by bid order by c desc limit 1) as res;"
    custom_assert(raw_q5, api_q5)


def test_query6():
    query1 = session.query(Boats.bid).filter(Boats.color == "red")
    query2 = session.query(Reserves.sid).filter(Reserves.bid.in_(query1))
    query3 = session.query(Sailors.sname).filter(Sailors.sid.notin_(query2))
    raw_q6 = "select s.sname from sailors s where s.sid not in (select r.sid from reserves r where r.bid in (select b.bid from boats b where b.color = 'red'));"
    custom_assert (raw_q6, query3)


def test_query7():
    query_7 = session.query(func.avg(Sailors.age)).filter(Sailors.rating == 10).all()
    raw_q7 = "SELECT avg(s.age) from sailors s where s.rating = 10;"
    custom_assert (raw_q7,query_7)


if  __name__ == "__main__":
    test_query5()
    test_query6()
    test_query7()
    session.commit()
    session.close()
