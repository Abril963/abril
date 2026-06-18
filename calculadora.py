import math
import re

SAFE_NAMES = {
    'pi': math.pi,
    'e': math.e,
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'sqrt': math.sqrt,
    'log': math.log,
    'log10': math.log10,
    'factorial': math.factorial,
    'comb': math.comb,
    'pow': pow,
    'abs': abs,
    'round': round,
    'bin': bin,
    'hex': hex,
    'oct': oct,
    'root': lambda x, n: x ** (1 / n),
}

PERCENT_RE = re.compile(r'(?P<num>\d+(?:\.\d+)?)%')


def parse_percent(expr):
    return PERCENT_RE.sub(r'(\g<num}/100)', expr)


def safe_eval(expr):
    expr = expr.replace('^', '**')
    expr = parse_percent(expr)
    return eval(expr, {'__builtins__': None}, SAFE_NAMES)


while True:
    try:
        entrada = input("\nCalculadora (ej: 5 + 3) o 'exit': ").strip()
        if entrada.lower() in ['exit', 'q']:
            print("¡Hasta luego!")
            break
        if not entrada:
            continue

        try:
            resultado = safe_eval(entrada)
        except ZeroDivisionError:
            print("Error: División por cero")
            continue
        except Exception:
            print("Formato inválido o función no reconocida")
            continue

        print(f"Resultado: {resultado}")
    except KeyboardInterrupt:
        print("\n¡Hasta luego!")
        break
