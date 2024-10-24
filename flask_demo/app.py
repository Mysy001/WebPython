from flask_script import Command, Manager
from flask import Flask

app = Flask(__name__)
#配置app
app.debug = True
manager = Manager(app)

class Hello(Command):
    "prints hello word"

    def run(self):
        print("Hello World!")

manager.add_command("hello",Hello())

if __name__ == "__main__":
    manager.run({'hello':Hello()})