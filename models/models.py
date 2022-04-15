from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
        return '<Playlist %r>' % self.name

class PlaylistItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    track_title = db.Column(db.String(120), unique=True, nullable=False)
    spotify_track_id = db.Column(db.String(120), unique=True, nullable=False)
    playlist_id = db.Column(db.String(120), unique=True, nullable=False)

    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'),
        nullable=False)
    playlist = db.relationship('Playlist',
        backref=db.backref('playlist_item', lazy=True))

    def __repr__(self):
        return '<PlaylistItem %r>' % self.id