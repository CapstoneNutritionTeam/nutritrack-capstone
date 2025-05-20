from flask import Flask

def create_app():
    app = Flask(__name__)

    #Register the Blueprints from the submodules
    from .searchbar import search_bp
    from .calculations import calc_bp

    app.register_blueprint(search_bp, url_prefix='/search')
    app.register_blueprint(calc_bp, url_prefix='/information')

    return app #Now we set :)