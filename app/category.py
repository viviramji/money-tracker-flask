import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('category', __name__, url_prefix='/category')

@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']
        db = get_db()

        db.execute(
            'INSERT INTO category (name) VALUES (?)',
            (name)
        )
        db.commit()

    return 'Process ok'


@bp.route('/read', methods=('GET', 'POST'))
def read():
    if request.method == 'GET':

        return db.execute(
            'SELECT Id, name from category'
        )

@bp.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM category WHERE id = ?', (id,))
    db.commit()
    return 'Delete ok'

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
def update(id):

    if request.method == 'POST':
        name = request.form['name']
        error = None

        if not name:
            error = 'Name is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE category SET name = ?'
                ' WHERE id = ?',
                (name, id)
            )
            db.commit()
            return 'Updated'

    return 'Okay'
