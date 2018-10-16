from base import Session, engine, Base
from sqlalchemy import Column, String, Integer, Date, MetaData, Table


class Boat(Base):
    __tablename__ = 'boats'

    bid = Column(Integer, primary_key=True)
    bname = Column(String(20))
    color = Column(String(10))
    length = Column(Integer)


class Sailor(Base):
    __tablename__ = 'sailors'

    sid = Column(Integer, primary_key=True)
    sname = Column(String(30))
    rating = Column(Integer)
    age = Column(Integer)

def query5():
    with engine.connect() as conn:
        result = conn.execute("select bid from (select bid, count(*) as c from reserves group by bid order by c desc limit 1) as res;")
        row = result.first()
        return row[0]


def test_query5():
    assert query5() == 104




def query6():
    with engine.connect() as conn:
        result = conn.execute("select s.sname from sailors s where s.sid not in (select r.sid from reserves r where r.bid in (select b.bid from boats b where b.color = 'red'));")

        rows = result.fetchall()
        result = []
        for r in rows:
            result.append(r[0])
        return result


def test_query6():
    expected = ["brutus", "andy", "rusty", "jit", "zorba", "horatio", "art", "vin", "bob"]
    result = query6();
    assert len(result) == len(expected) and sorted(expected) == sorted(result)


def query7():
    session = Session()
    result = session.query(Sailor).filter(Sailor.rating == 10).all()
    sum = 0
    count = 0
    for sailor in result:
        count = count + 1
        sum += sailor.age
    ave_age = (sum / count)
    session.commit()
    session.close()
    return ave_age


def test_query7():
    assert query7() == 35.0


if  __name__ == "__main__":
    test_query5();
    test_query6();
    test_query7();




