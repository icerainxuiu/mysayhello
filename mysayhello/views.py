from flask import render_template, flash, url_for, redirect

from mysayhello import app, db
from mysayhello.forms import HelloForm
from mysayhello.models import Message


@app.route('/sayhello', methods=['POST', 'GET'])
def sayhello():
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(name=name, body=body)
        db.session.add(message)
        db.session.commit()
        flash("your message have been sent to the world")
        return redirect(url_for("sayhello"))
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('sayhello.html', form=form, messages=messages)


@app.route('/', methods=["POST", "GET"])
def index():
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(name=name, body=body)
        db.session.add(message)
        db.session.commit()
        flash("your message have been sent to the world")
        return redirect(url_for("index"))
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('index.html', form=form, messages=messages)
