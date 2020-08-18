

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
<<<<<<< HEAD
    return "karak{}!".format(name)
=======
    return "Hello {}!".format(name)
>>>>>>> parent of d771661... qsdqd

if __name__ == '__main__':
    app.run()