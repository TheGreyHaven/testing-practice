from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))

#can take database as optional parameter, if left blank, the default is that database
def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    #FIXME: write a function that creates a game and adds it to the database.
    # these are example data that we add to our games data base because we 
    #do not want to use our actual games data
    game_a = Game(game_id=1, name="set", description="pattern matching")
    game_b = Game(game_id=2, name="bingo", description="Random number game")
    game_c = Game(game_id=3, name="Poker", description="Gambling with chips")

    #add games to our games database
    db.session.add_all([game_a, game_b, game_c])
    db.session.commit()

if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    print "Connected to DB."
