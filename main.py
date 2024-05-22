from flask import Flask, request, jsonify, render_template, redirect, url_for
from price_calculator import calculate_cost_price, calculate_selling_price
from xml_processor import extract_data_from_xml

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    # Passe valores padrão para as variáveis
    return render_template('index.html', product_data=[], markup=50, additional=5, freight=0, include_tax=False)

@app.route('/calculate', methods=['POST'])
def calculate():
    if 'xmlFile' not in request.files:
        return redirect(url_for('index'))

    file = request.files['xmlFile']
    if file.filename == '':
        return redirect(url_for('index'))

    markup = float(request.form['markup'])  # Convertendo para float
    additional = float(request.form['additional'])  # Convertendo para float
    freight = float(request.form['freight'])  # Convertendo para float
    include_tax = 'federalTax' in request.form

    namespaces = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}
    product_data = extract_data_from_xml(file, namespaces)

    for product in product_data:
        cost_price = calculate_cost_price(product['Valor Unitário'], product['Alíq. ICMS'], product['Alíq. IPI'], product['CFOP'], freight)
        selling_price = calculate_selling_price(cost_price, markup, additional, include_tax)
        product['Preço de Custo Final'] = cost_price
        product['Preço de Venda'] = selling_price

    return render_template('index.html', product_data=product_data, markup=markup, additional=additional, freight=freight, include_tax=include_tax)

@app.route('/update_prices', methods=['POST'])
def update_prices():
    data = request.get_json()
    index = data['index']
    markup = float(data['markup'])
    additional = data['additional']
    freight = data['freight']
    include_tax = data['include_tax']
    product_data = data['product_data']

    product = product_data[index]
    cost_price = calculate_cost_price(product['Valor Unitário'], product['Alíq. ICMS'], product['Alíq. IPI'], product['CFOP'], freight)
    new_selling_price = calculate_selling_price(cost_price, markup, additional, include_tax)

    return jsonify({'new_selling_price': new_selling_price})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
