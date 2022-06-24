from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
import os

app = Flask(__name__)

# Forcing a hard refresh of static assets to prevent caching while previewing builds
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def index():
	return render_template('home.html')

@app.route('/about-akhmad-suhariyono')
def about():
	return render_template('about-akhmad-suhariyono.html')

@app.route('/work')
def work():
	"""
	Template for dict:
	'TITLE': {'url': 'LINK', 'file_path':'/static/images/portfolio/IMG.JPG'}
	"""
	work_content = {
		'I am freelance'}
		}
	return render_template('work.html', work_content=work_content)

@app.route('/actualtest')
def actualtest():
	return render_template('index.html')

def get_static_file(path):
    site_root = os.path.realpath(os.path.dirname(__file__))
    return os.path.join(site_root, path)

if __name__ == "__main__":
	app.run(debug=True)
