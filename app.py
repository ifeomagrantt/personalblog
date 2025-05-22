from flask import Flask, render_template

app = Flask('__name__')

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/article')
def get_article():
  return render_template('article.html')

@app.route('/article/edit')
def edit_article():
  return render_template('edit.html')

@app.route('/article/new')
def new_article():
  return render_template('new-article.html')

@app.route('/admin')
def get_admin():
  return render_template('admin.html')



if __name__ == '__main__':
    app.run(debug=True,port=5050)