from flask import Flask
import blueprint
    
def create_app():
    app = Flask(__name__, static_folder='ui/public', static_url_path='/ui/public')
    app.register_blueprint(blueprint.bp)
    
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def catch_all(path):
        return app.send_static_file("index.html")

    return app

if __name__ == '__main__' :
    create_app().run(host='0.0.0.0')