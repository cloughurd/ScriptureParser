from wtforms import Form, StringField

class TermSearchForm(Form):
    search = StringField('')