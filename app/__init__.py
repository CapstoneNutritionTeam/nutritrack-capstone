from flask import Flask

def create_app():
    app = Flask(__name__)

    #Register the Blueprints from the submodules
    from .searchbar.app import search_bp
    app.register_blueprint(search_bp, url_prefix='/search')

    return app #Now we set :)
    