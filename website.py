from flask import Flask , render_template ,redirect,request,url_for
app = Flask(__name__)

@app.route('/')
def index2():
    return render_template('home.html')

@app.route('/home.html')
def home():
    return render_template('home.html')

@app.route('/blogs.html')
def blogs():
    return render_template('blogs.html')

@app.route('/backpacks.html')
def bag():
    return render_template('backpacks.html')

@app.route('/contactus.html')
def contact():
    return render_template('contactus.html')




def write_to_file(data):
    with open('database.txt',mode = 'a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file=database.write(f'\n{email},{subject},{message}')
        
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    error = None
    if request.method == 'POST':
        data =request.form.to_dict()
        write_to_file(data)
        return 'Success'
    else:
        return 'Something went wrong '





