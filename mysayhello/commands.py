import click

from mysayhello import app, db
from mysayhello.models import Message


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        click.confirm('This operation will delete the database, do you want to continue?', abort=True)
        db.drop_all()
        click.echo('Drop tables.')
    db.create_all()
    click.echo('Initialized database.')


@app.cli.command()
@click.option('--count', default=20, help="quantity of message, default is 20")
def forge(count):
    from faker import Faker
    db.drop_all()
    db.create_all()
    fake = Faker("zh_CN")
    click.echo("working ...")
    for i in range(count):
        message = Message(
            name=fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year()

        )
        db.session.add(message)
    db.session.commit()
    click.echo("create %d fake message" % count)
