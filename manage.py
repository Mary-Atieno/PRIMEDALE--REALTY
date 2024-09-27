from app import create_app, db
from app.models import User, House
from flask_migrate import Migrate, MigrateCommand 
from flask_script import Manager, Server

from flask.cli import FlaskGroup

# Creating app instance
app = create_app('production')
cli = FlaskGroup(app)

# migrate = Migrate(app,db)


@cli.command('test')
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@cli.command('shell')
def make_shell_context():
    return dict(app = app,db = db,User = User, House = House)

if __name__ == '_main_':
    cli()


