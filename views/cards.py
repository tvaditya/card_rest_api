from flask import Blueprint, render_template, request, redirect, url_for
from models.card import Card

card_blueprint = Blueprint('cards', __name__)

@card_blueprint.route('/')
def index():
    cards = Card.all()
    return render_template('cards/cards_index.html', cards=cards)


@card_blueprint.route('/new', methods=['GET', 'POST'])
def create_card():
    if request.method == 'POST':
        cpf = request.form['cpf']
        income = request.form['income']

        Card(cpf, income).save_to_mongo()

        return render_template("cards/new_card.html")


@card_blueprint.route('/delete/<string:card_id>')
def delete_card(card_id):
    Card.get_by_id().remove_from_mongo()
    return redirect(url_for('index'))