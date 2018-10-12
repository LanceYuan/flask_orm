from app import create_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import db

app = create_app()
manager = Manager(app)
Migrate(app, db)

# flask-migrate 依懒于flask-script
# 增加数据初始化相关操作 python manage.py db init|migrate|upgrade
manager.add_command("db", MigrateCommand)

# python manage.py cmd lance 给manager增加参数.
@manager.command
def cmd(args):
    print(args)


# 通过pipreqs生产插件库.  pipreqs ./ --encoding=utf8
if __name__ == "__main__":
    manager.run()