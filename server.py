from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'pineapple'

@app.route('/')
def landing():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    if 'visit' not in session:
        session['visit'] = 1
    else:
        session['visit'] += 1
    return render_template('index.html')

@app.route('/counter')
def counter():
    session['count'] += 1
    return redirect('/')

@app.route('/destroy')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/client', methods=['post'])
def client_choice():
    increment = int(request.form['increment'])
    increment -= 1
    session['count'] += increment
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)