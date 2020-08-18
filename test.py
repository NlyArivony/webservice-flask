

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "master voalohany!".format(name)

if __name__ == '__main__':
    app.run()