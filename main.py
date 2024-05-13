from flask import Flask, redirect, render_template, request, url_for

from xml_processor import extract_data_from_xml

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

    # Adding namespace
    namespaces = { 'nfe': 'http://www.portalfiscal.inf.br/nfe' }

    # Extract data from XML file
    product_data = extract_data_from_xml(file, namespaces)

    # Return extracted data to page
    return render_template('index.html', product_data=product_data, markup=markup, additional=additional, include_tax=include_tax)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
