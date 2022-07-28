from flask import Flask, render_template
from models.models import db, Playlist, PlaylistItem

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
db.create_all(app=app)

@app.route("/")
def test():
    playlists = Playlist.query.all()
    tracks = PlaylistItem.query.all()

    playlistViewModelArray = []
    
    # Eventualy can join on query w/ sql but this works for now
    for playlist in playlists:
        tracksInCurrentPlaylist = []
        for track in tracks:
            if(track.playlist_id == playlist.id):
                tracksInCurrentPlaylist.append(track)             

        playlistViewModelArray.append({"playlist": playlist, "tracks": tracksInCurrentPlaylist})
        
    return render_template('home.html',playlistViewModelArray=playlistViewModelArray)

app.run()

