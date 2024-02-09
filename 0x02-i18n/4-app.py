from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

# Define supported locales
SUPPORTED_LOCALES = ['en', 'fr']

# Function to get the locale


@babel.localeselector
def get_locale():
    # Check if the 'locale' parameter is in the request args
    locale = request.args.get('locale')
    if locale in SUPPORTED_LOCALES:
        return locale

    return request.accept_languages.best_match(SUPPORTED_LOCALES)

# Route for the home page


@app.route('/')
def index():
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
