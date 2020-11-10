# Routing 

from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def HomePage():
    return 'Home Page'
 

@app.route('/user')
def user():
    return 'User Page'


@app.route('/about')
def about():
    return 'About Page'


if __name__ == '__main__':
    app.run()