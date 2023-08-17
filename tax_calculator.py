
def tax_calculator(subtotal, sales_tax = .06):
    tax = round(subtotal * sales_tax, 2)
    total = round(subtotal + tax, 2)
    return(subtotal, tax, total)
    
