from flask import Flask
def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config['SECRET_KEY'] = 'sredtrfygtuyhioijk'

    from .views import views
    from .auth import auth

    # Register blueprints
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    return app