def obtener_fnc(formula):
    # Reemplazar los operadores lógicos por sus equivalentes en formato CNF
    formula = formula.replace('=', '|')
    formula = formula.replace('~', '-')

    # Dividir la fórmula en cláusulas
    clausulas = formula.split('&')

    # Eliminar espacios en blanco y paréntesis de las cláusulas
    clausulas = [clausula.replace('(', '').replace(')', '').strip() for clausula in clausulas]

    # Obtener la FNC
    fnc = ' '.join(clausulas)

    return fnc


def obtener_literales(fnc):
    literales = set()

    # Dividir la FNC en cláusulas
    clausulas = fnc.split()

    for clausula in clausulas:
        # Dividir la cláusula en literales
        literales_clausula = clausula.split('|')

        for literal in literales_clausula:
            # Eliminar el signo negativo del literal
            literal = literal.replace('-', '')

            # Agregar el literal a la lista de literales
            literales.add(literal)

    return literales


def obtener_fnc_y_literales(formula):
    fnc = obtener_fnc(formula)
    literales = obtener_literales(fnc)
    return fnc, literales


def guardar_solucion(fnc, literales, nombre_archivo):
    with open(nombre_archivo, 'w') as f:
        f.write('FNC:\n')
        f.write(fnc + '\n\n')
        f.write('Literales que hacen verdadera la FNC:\n')
        f.write(', '.join(sorted(list(literales))) + '\n')


# Aquí se cambia la fórmula
formula = '( p | ˜q )&(˜ p | q )&( q | ˜ r )&(˜ q | ˜ r )'
fnc, literales = obtener_fnc_y_literales(formula)
guardar_solucion(fnc, literales, 'solucion.txt')
