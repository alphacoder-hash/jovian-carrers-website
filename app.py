from flask import Flask, render_template
app = Flask(__name__)

JOBS =[
    {
      'id':1,
      'title':'Data Analyst', 
        'location':'Bengaluru, India',
        'salary':'Rs. 10,00,000'
        
    },
    {
      'id':2,
      'title':'Data Scientist', 
        'location':'Delhi, India',
        'salary':'Rs. 15,00,000'

    },
    {
      'id':3,
      'title':'Frontend Engineer', 
        'location':'Vadodara, India',
        'salary':'Rs. 10,78,000'

    },
    {
      'id':4,
      'title':'Backend Engineer', 
        'location':'Mumbai, India',
        'salary':'Rs. 10,000'

    }
]
@app.route("/")
def hello_world():
    return render_template('home.html',
                          jobs=JOBS)

app.run(host='0.0.0.0', debug=True)