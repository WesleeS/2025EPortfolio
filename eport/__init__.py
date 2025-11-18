from flask import Flask, url_for

def create_app():
    app = Flask(__name__)

    # Import blueprints
    from .home import home_bp
    from .about import about_bp
    from .artefacts import artefacts_bp
    from .experience import experience_bp

    # Register blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(artefacts_bp)
    app.register_blueprint(experience_bp)


    return app
