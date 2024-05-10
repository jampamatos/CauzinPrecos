from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Check if file sent
    if 'xmlFile' not in request.files:
        return redirect(url_for('index')) # Redirect to index if no file sent

    file = request.files['xmlFile']
    if file.filename == '':
        return redirect(url_for('index')) # Redirect to index if no file selected

    # Fetch other form data
    markup = request.form['markup']
    additional = request.form['additional']
    include_tax = 'federalTax' in request.form

    # Logic for XML processing and price calculation
    # Temporarily, we'll view received data
    return f"Received file {file.filename}; markup: {markup}; additional {additional}; tax: {include_tax}."

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
