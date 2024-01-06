from flask import Flask
from app import create_app, db
from flask.cli import FlaskGroup

application = create_app()
cli = FlaskGroup(application)

# define that to create the tables having access to the app context from the container shell
@cli.command('create_all')
def create_all():
    with application.app_context():
        db.create_all()

if __name__ == "__main__":
    cli()