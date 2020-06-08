from flask import Flask,request
app=Flask(__name__)#current module
#obj=classname()
@app.route('/')#binding
def hello():
    return 'Hello '
@app.route('/r2')
def hello2():
    # id= request.args.get('id')

    return  "running in r2"
if __name__=='__main__':
    app.run(debug=True)#live server