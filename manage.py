from app import create_app
from app import db
from app.models import User

# from flask_migrate import Migrate #MigrateCommand

from flask.cli import FlaskGroup


# Creating app instance
app = create_app('development')
cli = FlaskGroup(app)


@cli.command('test')
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@cli.command('shell')
def make_shell_context():
    return dict(app = app,db = db,User = User )

if __name__ == '_main_':
    cli()
