from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

@app.route('/via_postman', methods=['POST']) # for calling the API from Postman/SOAPUI
def math_operation_via_postman():
    if (request.method=='POST'):
        operation=request.json['operation']
        num1=int(request.json['num1'])
        num2 = int(request.json['num2'])
        if(operation=='add'):
            r=num1+num2
            result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return jsonify(result)          #convert it to json format and send it

##Another function --->different route


@app.route('/aymane', methods=['POST']) # for calling the API from Postman/SOAPUI
def math_aymane():
    if (request.method=='POST'):
        num0=request.json['num0']
        num1=int(request.json['num1'])
        num2 = int(request.json['num2'])
        result = num0*num2*num1
        return  jsonify(result)

@app.route('/aymane_function')
def url_test1():

    test1= request.args.get('val1')
    test2= request.args.get('val2')
    test3 = test1+test2
    return '''<h1>my result is: {}</h1>'''.format(test3)

@app.route('/aymane_1', methods=['POST']) # for calling the API from Postman/SOAPUI
def math_aymane2():
    if (request.method=='POST'):
        name=request.json['name']
        email=request.json['email']
        tel = int(request.json['tel'])
        return  jsonify(name+email+ "tel")


if __name__ == '__main__': ##calling the super class main as a constructed
    app.run()
