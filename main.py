from semantic import parser

while True:
    try:
        s = input("Ingresa una expresión: ")
    except EOFError:
        break
    if not s:
        continue
    try:
        result = parser.parse(s)
        print(result)
    except Exception as e:
        print(e)