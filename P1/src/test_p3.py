from base import engine

#query for bi weekly wage report
def get_wages():
    with engine.connect() as conn:
        result = conn.execute("SELECT employees.ename ,employees.salary * hours.hours AS Wages FROM hours JOIN employees ON employees.eid=hours.employees_eid WHERE day >= '1998/10/9' AND day <= '1998/10/23';")
        rows = result.fetchall()
        return rows

def test_getwages():
    wage_sum = 0
    result = get_wages();
    for row in result:
        wage_sum = wage_sum + row[1]
    assert wage_sum == 291


# SELECT r.bid, SUM(r.cost) - SUM(c.cost) AS profit from cost_record c JOIN reserves r ON c.boat_id=r.bid WHERE r.day='1998/10/10' GROUP BY r.bid;
def get_daily_inventory(): # daily profit = profit [revenue - fix cost] by boat
    with engine.connect() as conn:
        result = conn.execute("SELECT r.bid, SUM(r.cost) - SUM(c.cost) AS profit from cost_record c JOIN reserves r ON c.boat_id=r.bid WHERE r.day='1998/10/10' GROUP BY r.bid;")
        rows = result.fetchall()
        return rows

def test_get_daily_inventory():
    daily_profit = 0
    result = get_daily_inventory();
    for row in result:
        daily_profit = daily_profit + row[1]
    assert daily_profit == -176


if __name__ == "__main__":
    test_getwages()
    test_get_daily_inventory()