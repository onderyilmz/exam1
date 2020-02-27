from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/onder/Desktop/Projects/pro1/comments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def index():
	oldComments= Comments.query.order_by(Comments.id.desc()).all()
	return render_template('index.html', oldComments=oldComments)


@app.route('/sign')
def sign():
	return render_template('sign.html')

@app.route('/signPost', methods=['POST'])
def signPost():
	name= request.form.get('name')
	comment= request.form.get('comment')

	newComments= Comments(username=name, comment=comment)

	db.session.add(newComments)
	db.session.commit()

	return redirect(url_for('index'))

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    comment = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.comment

if __name__== "__main__":
	app.run(debug=True)