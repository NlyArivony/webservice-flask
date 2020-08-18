

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
<<<<<<< HEAD
    return "master voalohany!".format(name)
=======
    return "karak{}!".format(name)
>>>>>>> parent of e74976c... sparta

if __name__ == '__main__':
    app.run()