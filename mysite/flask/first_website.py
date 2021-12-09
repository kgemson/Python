from flask import Flask

app=Flask(__name__) #'__name__' is a special python variable set at execution time 
                    # it will be set to '__main__' when run directly, i.e. not imported

@app.route('/') # this is a decorator. Parameter determines where output is mapped to, i.e. local host (http://localhost:5000/)
def home():
    return "Home content goes here"

@app.route('/about/') # this is another decorator. Parameter determines where output is mapped to, i.e. local host/about (http://localhost:5000/about)
def about():
    return "About content goes here"

if __name__=="__main__": #if we are executing the script directly and not importing, run the app
    app.run(debug=True)