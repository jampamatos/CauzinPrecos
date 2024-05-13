import unittest

from xml_processor import extract_data_from_xml


class TestXMLProcessor(unittest.TestCase):
  def test_extract_coral(self):
    """Tests data extraction from 'xml-coral.xml'."""
    namespaces = { 'nfe': 'http://www.portalfiscal.inf.br/nfe' }
    xml_file = 'xml-coral.xml'
    data = extract_data_from_xml(xml_file, namespaces)
    self.assertTrue(len(data) > 0, "No data extracted. Check XML file and extraction logic.")
    self.assertEqual(data[0]['CFOP'], '6401')
    self.assertEqual(data[0]['Alíq. ICMS'], '12.0000')
    self.assertEqual(data[0]['Alíq. IPI'], '0')
    self.assertEqual(data[3]['Alíq. IPI'], '3.2500')

  def test_extract_lazz(self):
    """Tests data extraction from 'xml-lazz.xml'."""
    namespaces = { 'nfe': 'http://www.portalfiscal.inf.br/nfe' }
    xml_file = 'xml-lazz.xml'
    data = extract_data_from_xml(xml_file, namespaces)
    self.assertTrue(len(data) > 0, "No data extracted. Check XML file and extraction logic.")
    self.assertEqual(data[0]['CFOP'], '6102')
    self.assertEqual(data[0]['Alíq. ICMS'], '12.00')
    self.assertEqual(data[0]['Alíq. IPI'], '6.50')
    self.assertEqual(data[1]['CFOP'], '6403')
    self.assertEqual(data[1]['Alíq. ICMS'], '12.00')
    self.assertEqual(data[1]['Alíq. IPI'], '3.25')

# Run the tests
if __name__ == '__main__':
  unittest.main()

