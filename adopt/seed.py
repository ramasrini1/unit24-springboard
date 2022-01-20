from app import db
from models import Pet

db.drop_all()
db.create_all()

p1 = Pet(name="Toby", species="dog", photo_url=None, age=2, notes="Good Dog")
p2 = Pet(name="Luna", species="dog", photo_url=None, age=2, notes="Good Smart Dog")
p3 = Pet(name="Toby", species="dog", photo_url=None, age=2, notes="Good Dog")
p4 = Pet(name="Daisy", species="cat", photo_url=None, age=2, notes="Fat Cat")
#db.session.add(p1)
db.session.add_all([p1, p2, p3, p4])
db.session.commit()
