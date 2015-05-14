#!/use/bin/env/python
import os
from app import db, create_app
from app.models import User, Role
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.login import current_user

app = create_app(os.getenv('FLASK_CONFIG')or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
	return dict(app = app, db = db, User = User, Role = Role)
manager.add_command("shell", Shell(make_context = make_shell_context))
manager.add_command('db', MigrateCommand)
#db = upgrade()
@manager.command
def test():
	"""Run the unit test."""
	import unittest
	tests = unittest.TestLoader().discover('tests')
	unittest.TextTestRunner(verbosity = 2).run(tests)

print test()

#u = User(email = '1065482660.com',username = 'lizhexxxxxxxxxxxxxx', password = '1065482100@qq.com', role_id = 0)
#db.session.add(u)
#db.session.commit()
if __name__ == '__main__':
	manager.run()
