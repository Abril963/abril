import math
import re
import tkinter as tk
from tkinter import messagebox

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


class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("380x700")
        self.root.resizable(False, False)

        self.display_var = tk.StringVar(value="0")

        display = tk.Entry(root, textvar=self.display_var, font=("Arial", 20), justify="right", bd=2)
        display.pack(fill=tk.BOTH, padx=10, pady=10)

        frame = tk.Frame(root)
        frame.pack(padx=10, pady=10)

        botones = [
            ("C", 0, 0), ("(", 0, 1), (")", 0, 2), ("%", 0, 3),
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("**", 4, 2), ("+", 4, 3),
            ("pi", 5, 0), ("sin(", 5, 1), ("cos(", 5, 2), ("tan(", 5, 3),
            ("sqrt(", 6, 0), ("root(", 6, 1), ("comb(", 6, 2), ("bin(", 6, 3),
            ("hex(", 7, 0), ("oct(", 7, 1), ("log(", 7, 2), ("=", 7, 3),
        ]

        for texto, fila, col in botones:
            btn = tk.Button(frame, text=texto, font=("Arial", 14), width=6, height=2)
            btn.grid(row=fila, column=col, padx=2, pady=2)
            if texto == "=":
                btn.config(command=self.calcular)
            elif texto == "C":
                btn.config(command=self.limpiar)
            else:
                btn.config(command=lambda t=texto: self.agregar(t))

    def agregar(self, char):
        actual = self.display_var.get()
        if actual == "0" and char not in [".", "pi", "sin(", "cos(", "tan(", "sqrt(", "root(", "comb(", "bin(", "hex(", "oct(", "log("]:
            self.display_var.set(char)
        else:
            self.display_var.set(actual + char)

    def limpiar(self):
        self.display_var.set("0")

    def calcular(self):
        expr = self.display_var.get()
        try:
            resultado = safe_eval(expr)
            if isinstance(resultado, float) and resultado.is_integer():
                resultado = int(resultado)
            self.display_var.set(str(resultado))
        except ZeroDivisionError:
            messagebox.showerror("Error", "División por cero")
            self.limpiar()
        except Exception:
            messagebox.showerror("Error", "Expresión inválida")
            self.limpiar()


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculadora(root)
    root.mainloop()
