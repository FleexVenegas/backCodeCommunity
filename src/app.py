from flask import Flask
from config import config

# Routes
from routes import QuestionRoute
from routes import RegisterRoute
from routes import AuthRoutes

app = Flask(__name__)


def page_not_found(error):
    return "<h1>Page not found</h1>", 404



if __name__ == "__main__":
    app.config.from_object(config['development'])

    # Blueprint's
    app.register_blueprint(RegisterRoute.main, url_prefix="/api/user/")
    app.register_blueprint(QuestionRoute.main, url_prefix="/api/community")
    app.register_blueprint(AuthRoutes.main, url_prefix="/api/auth")

    # Error handlers
    app.register_error_handler(404, page_not_found)

    app.run()