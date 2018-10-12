from app import create_app
from flask_script import Manager

app = create_app()
manager = Manager(app)

# python manage.py cmd lance 给manager增加参数.
@manager.command
def cmd(args):
    print(args)

if __name__ == "__main__":
    manager.run()