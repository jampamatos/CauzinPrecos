import xml.etree.ElementTree as ET


def extract_data_from_xml(xml_file, namespaces):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
    except Exception as e:
        print("Erro ao carregar o arquivo XML:", e)
        return []

    item_data = []

    for item in root.findall('.//nfe:det', namespaces=namespaces):
        icms_tag = item.find('.//nfe:imposto/nfe:ICMS/*', namespaces=namespaces)
        icms_value = icms_tag.find('nfe:pICMS', namespaces=namespaces).text if icms_tag is not None and icms_tag.find('nfe:pICMS', namespaces=namespaces) is not None else "0"

        # General search for 'pIPI' under 'IPI' tag
        ipi_value = "0"  # Default value if not found
        for ipi_subtag in item.findall('.//nfe:imposto/nfe:IPI/*', namespaces=namespaces):
            pipi_element = ipi_subtag.find('.//nfe:pIPI', namespaces=namespaces)
            if pipi_element is not None:
                ipi_value = pipi_element.text
                break  # Assumes only one 'pIPI' per 'det' element
        
        # Assure formatting with two decimals
        icms_value = f"{float(icms_value):.2f}%"
        ipi_value = f"{float(ipi_value):.2f}%"
        
        product_data = {
          "Nome do Produto": item.find('.//nfe:prod/nfe:xProd', namespaces=namespaces).text,
          "CFOP": item.find('.//nfe:prod/nfe:CFOP', namespaces=namespaces).text,
          "Valor Unitário": item.find('.//nfe:prod/nfe:vUnCom', namespaces=namespaces).text,
          "Alíq. ICMS": icms_value,
          "Alíq. IPI": ipi_value
        }
        item_data.append(product_data)

    return item_data

