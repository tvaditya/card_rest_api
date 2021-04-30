from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, validators
from models.card import Card
from common.score_calc import score_calc

class  CardForm(FlaskForm):
    cpf = StringField('CPF: ', [validators.Length(min=11, max=11), validators.DataRequired(),
                                validators.regexp('^\d+$', message='Must contain only numericals.')])
    income = FloatField('INCOME: ', [validators.DataRequired(message='This field must is required and must contain only numericals.')])

card_blueprint = Blueprint('cards', __name__)

@card_blueprint.route('/')
def index():
    cards = Card.all()
    return render_template('cards/cards_index.html', cards=cards)


@card_blueprint.route('/new', methods=['GET', 'POST'])
def create_card():
    form = CardForm()

    if request.method == 'POST' and form.validate_on_submit():
        cpf = form.cpf.data
        income = form.income.data
        score, credit, approval = score_calc(income)
        # score = score_calc(float(income))[0]
        # credit = score_calc(float(income))[1]
        flash(f'The CPF {cpf} with score {score} and Income {income} was approval status is {approval} ')

        Card(cpf, income, score, credit, approval).save_to_mongo()
        print("Saved to DB")

    return render_template("cards/create_card.html", form=form, pageTitle="Create Credit Card Form")


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

