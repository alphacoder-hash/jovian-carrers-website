from flask import Flask, render_template, jsonify
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

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

@app.route("/login", methods=['POST'])
def login():
    # Add authentication logic here
    return redirect('/')

@app.route("/signup", methods=['POST'])
def signup():
    # Add registration logic here
    return redirect('/')

@app.route("/apply", methods=['POST'])
def apply():
    # Add application handling logic here
    return redirect('/')

@app.route("/contact", methods=['POST'])
def contact():
    # Add contact form handling logic here
    return redirect('/')

if __name__ == "__main__":
    app.secret_key = 'your-secret-key'  # Required for sessions
    app.run(host='0.0.0.0', debug=True)