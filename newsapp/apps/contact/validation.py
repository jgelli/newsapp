def cellphone_has_letter(instance, cellphone):
    """ Check if has letter in the cellphone """
    if any(char.isalpha() for char in cellphone):
        instance.add_error('cellphone', 'Não inclua letras neste campo!')

def cellphone_length(instance, cellphone):
    """ Check if cellphone has 11 digits """
    if (len(cellphone) < 11):
        instance.add_error('cellphone', 'O número deve conter 11 dígitos. (DDD + CELULAR)')
