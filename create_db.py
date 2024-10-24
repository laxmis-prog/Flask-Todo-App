from app import db
from app import app, Todo

with app.app_context():
   db.create_all()
   db.session.commit()
