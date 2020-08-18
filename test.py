

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello ssdfsdf {}!".format(name)

if __name__ == '__main__':
    app.run()