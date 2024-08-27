#!/user/bin/python3
""" the main app routes """

from flask import render_template

def create_app():
    from api.v1.app import app
    return app

app = create_app()


@app.route('/')
def homePage():
    """render the hoem page"""
    return render_template('index.html')
