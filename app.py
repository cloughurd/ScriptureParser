from flask import Flask, request, render_template, flash, redirect, session, url_for
from search import TermSearchForm
from makevisual import make_visualization
import os
import matplotlib
matplotlib.use('Agg')

VISUALS_FOLDER = os.path.join('static', 'visuals')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = VISUALS_FOLDER

@app.route('/', methods=['GET','POST'])
def home():
    search = TermSearchForm(request.form)
    if request.method == 'POST':
        search_term = search.data['search']
        select_choice = search.data['select']
        by_verse = select_choice == 'By Verses'
        res = make_visualization(search_term, by_verse)
        return redirect(url_for('result', res=res))
    return render_template('home.html', form=search)

@app.route('/atonement', methods=['GET','POST'])
def atonement():
    search = TermSearchForm(request.form)
    if request.method == 'POST':
        search_term = search.data['search']
        select_choice = search.data['select']
        by_verse = select_choice == 'By Verses'
        res = make_visualization(search_term, by_verse)
        return redirect(url_for('result', res=res))
    return render_template('atonement.html', form=search)

@app.route('/titles', methods=['GET','POST'])
def titles():
    search = TermSearchForm(request.form)
    if request.method == 'POST':
        search_term = search.data['search']
        select_choice = search.data['select']
        by_verse = select_choice == 'By Verses'
        res = make_visualization(search_term, by_verse)
        return redirect(url_for('result', res=res))
    return render_template('titles.html', form=search)

@app.route('/other', methods=['GET','POST'])
def other():
    search = TermSearchForm(request.form)
    if request.method == 'POST':
        search_term = search.data['search']
        select_choice = search.data['select']
        by_verse = select_choice == 'By Verses'
        res = make_visualization(search_term, by_verse)
        return redirect(url_for('result', res=res))
    return render_template('other.html', form=search)

@app.route('/result', methods=['GET','POST'])
def result():
    search = TermSearchForm(request.form)
    if request.method == 'POST':
        search_term = search.data['search']
        select_choice = search.data['select']
        by_verse = select_choice == 'By Verses'
        res = make_visualization(search_term, by_verse)
        return redirect(url_for('result', res=res))
    else:
        res = request.args.get('res')
        filename = os.path.join(app.config['UPLOAD_FOLDER'], res)
        return render_template('result.html', form=search, result_graph=filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)