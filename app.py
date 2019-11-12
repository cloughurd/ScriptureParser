from flask import Flask, request, render_template
from search import TermSearchForm

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    search = TermSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    return render_template('index.html')

@app.route('/results', methods=['GET','POST'])
def search_results(search):
    pass

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)