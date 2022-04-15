from flask import Flask
from models.models import db, Playlist, PlaylistItem

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
db.create_all(app=app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/days")
def getDays():
    items = Playlist.query.all()
    days = []
    
    for i in items:
        days.append(i.title)
    
    return str(days)



app.run()