from flask import Flask, render_template

app=Flask(__name__) #'__name__' is a special python variable set at execution time 
                    # it will be set to '__main__' when run directly, i.e. not imported

@app.route('/') # this is a decorator. Parameter determines where output is mapped to, i.e. local host (http://localhost:5000/)
def home():
    return render_template('home.html') # html file must be in a folder called 'templates'

@app.route('/about/') # this is another decorator. Parameter determines where output is mapped to, i.e. local host/about (http://localhost:5000/about)
def about():
    return render_template('about.html') # html file must be in a folder called 'templates'

if __name__=="__main__": #if we are executing the script directly and not importing, run the app
    app.run(debug=True)