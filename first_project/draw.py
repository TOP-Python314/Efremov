# field_template = ' {} | {} | {} \n———————————\n {} | {} | {} \n———————————\n {} | {} | {} '
def field_template(cells):
    line = (cells-1) * ' {} |' + ' {} \n'
    a = line + (cells-1) * '————' + '———\n'   
    return a * (cells-1) + line