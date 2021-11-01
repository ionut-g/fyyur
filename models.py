
#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#


#city table one to many:
class City(db.Model):
  __tablename__='city'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), nullable=False)
  venues = db.relationship('Venue',
                backref='venue_city',
                lazy=True)
  artists = db.relationship('Artist',
                backref='artist_city',
                lazy=True)

#state table
class State(db.Model):
  __tablename__='state'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), nullable=True)
  venues = db.relationship('Venue', 
                backref='venue_state', lazy=True)  
  artists = db.relationship('Artist',
                backref='artist_state',
                lazy=True)
  #genre table many to many relationship
  class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(120),nullable=True)

#association_table for many to many relationship between Genre and Venue tables
association_table_venue_genre = db.Table('assoc_venue_genre', 
    db.Column('venue_id',db.Integer, db.ForeignKey('venue.id'), primary_key=True),
    db.Column('genre_id',db.Integer, db.ForeignKey('genre.id'), primary_key=True)
    )

association_table_artist_genre = db.Table('assoc_artist_genre', 
    db.Column('artist_id',db.Integer, db.ForeignKey('artist.id'), primary_key=True),
    db.Column('genre_id',db.Integer, db.ForeignKey('genre.id'), primary_key=True)
    )

class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True) #ok
    name = db.Column(db.String, nullable=False) #ok
    #city
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False) #ok
    #state
    state_id = db.Column(db.Integer, db.ForeignKey('state.id'), nullable=True) #ok
    address = db.Column(db.String(120), nullable=False) #ok
    phone = db.Column(db.String(120), nullable=True, default='no number')
    #genre
    genres = db.relationship('Genre',
                          secondary=association_table_venue_genre,
                          lazy='subquery',
                          backref=db.backref('venue', lazy=True)) #ok
    facebook_link = db.Column(db.String(120), nullable=True, default="")
    image_link = db.Column(
        db.String(500),
        nullable=True,
        default="https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60",
        )
    website_link = db.Column(db.String(120), nullable=True, default="")
    looking_for_talent = db.Column(db.Boolean, nullable=True, default=False)
    seeking_description = db.Column(db.String(120), nullable=True)
    shows = db.relationship('Show', backref='show', lazy=True)

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    #ok
class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True) #ok
    name = db.Column(db.String, nullable=False) #ok
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    state_id = db.Column(db.Integer, db.ForeignKey('state.id'), nullable=True)
    phone = db.Column(db.String(120), nullable=True, default='no number')
    genres = db.relationship('Genre',
                          secondary=association_table_artist_genre,
                          lazy='subquery',
                          backref=db.backref('artist', lazy=True)) #ok
    facebook_link = db.Column(db.String(500), nullable=True, default="")
    image_link = db.Column(
        db.String(500),
        nullable=True,
        default="https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60",
        )
    website_link = db.Column(db.String(120), nullable=True, default="")
    looking_for_talent = db.Column(db.Boolean, nullable=True, default=False)
    seeking_description = db.Column(db.String(120), nullable=True)
    shows = db.relationship('Show', backref='show', lazy=True)
    # TODO: implement any missing fields, as a database migration using Flask-Migrate

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.

class Show(db.Model):
    __tablename__ = "show"
    artist_id = db.Column(db.Integer, db.ForeignKey("artist.id"), primary_key=True)
    venue_id = db.Column(
        db.Integer, db.ForeignKey("venue.id", ondelete="CASCADE"), primary_key=True
    )
    start_time = db.Column(db.DateTime, nullable=False)


