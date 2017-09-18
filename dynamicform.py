
from flask import Flask, request
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'

# This route is a good example
@app.route('/user/<name>')
def hello_user(name):
   return '<h1>Hello {0}</h1>'.format(name)

@app.route('/form',methods= ['POST','GET'])
def enter_data():
    s = """<!DOCTYPE html>
<html>
<body>

<form action="http://localhost:5000/result" method="GET">
  First name:<br>
  <input type="text" name="firstname" value="Mickey">
  <br>
  Last name:<br>
  <input type="text" name="lastname" value="Mouse">
  <br><br>
  <input type="submit" value="Submit">
</form> 

</body>
</html>""" # Note that this defaults to first name is Mickey, last name is Mouse -- you could change that!
    return s

@app.route('/result',methods = ['POST', 'GET'])
def res():
    if request.method == 'GET':
        result = request.args
        first = result.get('firstname')
        last = result.get('lastname')
        #return render_template("result.html",result = result)
        return "<b>" + first + "</b>, <i>" + last + "</i>" 

if __name__ == '__main__':
    app.run()
