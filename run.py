
# from flaskblog import app
from flaskblog import create_app
from flask import current_app

current_app.app_context().push()
app = create_app() # här kan man stoppa in en anpassad

if __name__ == "__main__":
    # db.create_all()
    app.debug = True
    app.run()
    
