from flask import Flask
from flask import request
from flask import render_template
from markdown import markdown
import shutil
import os
from os import listdir
from os.path import isfile, join

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route ('/')
def index():
    filenames = [f for f in listdir('./posts/') if isfile(join('./posts/', f))]
    for i in range(0, len(filenames)):
        filenames[i] = '<a href="posts/' + filenames[i] + '">' + filenames[i] + '</a>'
    return render_template('base.html', title='Home', content='<br/>'.join(filenames))

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        with open('posts/' + request.form['title'] + '.md', 'w') as writer:
            try:
                writer.write(request.form['content'])
            finally:
                writer.close
        return render_template('base.html', title=content, content=content)
    else:
        return render_template('admin.html', title='admin')

@app.route('/delete-posts')
def delete_posts():
    shutil.rmtree('posts')
    os.mkdir('posts')
    return  render_template('base.html', title='Posts deleted', content='Posts deleted')

@app.route('/posts/<title>')
def readPost(title):
    with open('posts/' + title) as reader:
        try:
            content = reader.read()
        finally:
            reader.close()
    return  render_template('base.html', title=title, content=markdown(content))
        

@app.after_request
def add_header(req):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    req.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    req.headers["Pragma"] = "no-cache"
    req.headers["Expires"] = "0"
    req.headers['Cache-Control'] = 'public, max-age=0'
    return req