from wtforms import Form, StringField, SelectField

class TermSearchForm(Form):
    choices = [('By Verses', 'By Verses'), ('By Words', 'By Words')]
    select = SelectField('Search for Term Frequency', choices=choices)
    search = StringField('')