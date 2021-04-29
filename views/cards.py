from flask import Blueprint, render_template, request, redirect, url_for
from models.card import Card
from common.score_calc import score_calc

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
        score = score_calc(float(income))[0]
        credit = score_calc(float(income))[1]
        Card(cpf, income, score, credit).save_to_mongo()
        print("Saved to DB")

    return render_template("cards/new_card.html")


# @card_blueprint.route('/edit/<string:card_id>', methods=['GET', 'POST'])
# def edit_card(card_id):
#     if request.method == 'POST':
#         cpf = request.form['cpf']
#         income = request.form['income']
#
#         card = Card.get_by_id(card_id)
#
#         card.cpf = cpf
#         card.income = income
#
#         card.save_to_mongo()
#
#         return redirect(url_for('.index'))
#
#     # What happens if it's a GET request
#     return render_template("stores/edit_store.html", card=Card.get_by_id(card_id))


@card_blueprint.route('/delete/<string:card_id>')
def delete_card(card_id):
    Card.get_by_id(card_id).remove_from_mongo()
    return redirect(url_for('.index'))

