import sqlalchemy as db

engine=db.create_engine("postgresql://postgres:macmhn1@localhost:5432/college") #--Here first is db software://username:password@address of db:port number/nameofdb
print(engine)

with engine.connect() as conn:
    result=conn.execute(db.text("SELECT * from students"))
    print(type(result))
    print(result)
    print(result.fetchall())
    for r in result.fetchall():
        print(r)