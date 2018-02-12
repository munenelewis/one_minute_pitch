from app import create_app,db
from app.models import User,Pitch,Comment,Votes,Category
from  flask_migrate import Migrate, MigrateCommand


from flask_script import Manager,Server
# from app.models import User, Role, Comment,Pitch

#creating an app instance  
app = create_app('production')  


manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)
@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Pitch= Pitch,Comment=Comment,Votes=Votes,Category=Category)

if __name__ == '__main__':
    manager.run()