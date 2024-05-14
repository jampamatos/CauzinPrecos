def calculate_cost_price(unit_price, icms_rate, ipi_rate, cfop, freight):
  unit_price = float(unit_price)
  freight = float(freight)/100

  # Determine effective ICMS tax based on CFOP and ICMS and/ or IPI rate
  if cfop in ['5101', '5102', '6101', '6102']: # No ST
    if icms_rate == '4.00%':
      icms_effective_rate = 13.27 / 100
    elif icms_rate == '12.00%':
      icms_effective_rate = 7.32 / 100
    else:
      icms_effective_rate = 0 # Other cases
  elif cfop in ['5401', '5403', '5405', '6401', '6403', '6405']: # ST
    if ipi_rate == '0.00%':
      icms_effective_rate = 19.7 / 100
    elif ipi_rate == '1.30%':
      icms_effective_rate = 20.3 / 100
    elif ipi_rate == '3.25%':
      icms_effective_rate = 21.26 / 100
    elif ipi_rate == '6.50%':
      icms_effective_rate = 24 / 100
    else:
      icms_effective_rate = 0 # Other cases
  else:
    icms_effective_rate = 0 # Other CFOPs

  # Apply ICMS to price
  unit_price += unit_price * icms_effective_rate
  
  # Calculate IPI and apply to calculated ICMS
  ipi_effective_rate = float(ipi_rate.strip('%')) / 100
  unit_price += unit_price * ipi_effective_rate

  # Calculate freight and update price
  unit_price += unit_price * freight

  return round(unit_price, 2)

def calculate_selling_price(cost_price, markup, additional, include_tax):
  markup = float(markup) / 100
  additional = float(additional) / 100
  tax_rate = 7/100 if include_tax else 0 # Assuming federal tax rate is 7%

  # Apply markup and update price
  cost_price += cost_price * markup

  # Apply additional
  cost_price += cost_price * additional

  # Apply federal tax rate
  cost_price += cost_price * tax_rate

  return round(cost_price, 2)