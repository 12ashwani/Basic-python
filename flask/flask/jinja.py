from flask import Flask, render_template, request

# Create an instance of the Flask class
app = Flask(__name__)

@app.route('/')
def welcome():
    return '''
    <html>
        <head>
            <title>Flask Application</title>
            <script>
                function navigate() {
                    const selectedPage = document.getElementById('pageDropdown').value;
                    if (selectedPage) {
                        window.location.href = selectedPage;
                    }
                }
            </script>
        </head>
        <body>
            <h1>Welcome to this Flask Application</h1>
            <p>This application shows various information.</p>
            <label for="pageDropdown">Navigate to:</label>
            <select id="pageDropdown" onchange="navigate()">
                <option value="">-- Select a page --</option>
                <option value="/index">Index</option>
                <option value="/about">About</option>
                <option value="/form">Form</option>
            </select>
        </body>
    </html>
    '''

@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Handle form data here
        name = request.form.get('name')
        email = request.form.get('email')
        return f'<h1>Form submitted by {name} with email {email}</h1>'
    return render_template('form.html')
## varivable rule
@app.route('/success/<int:score>')
def success(score):
    
    return f'The marks you get {score}'


if __name__ == '__main__':
    app.run(debug=True)
