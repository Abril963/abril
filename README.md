# Calculadora Aritmética Interactiva

Calculadora con soporte para consola, GUI y web.

## Características

- ✨ **Operaciones básicas**: suma (`+`), resta (`-`), multiplicación (`*`), división (`/`)
- 📈 **Exponenciación**: `^` o `**`
- 📐 **Raíces**: `sqrt(x)` o `root(x,n)`
- 💯 **Porcentajes**: `50%`, `200 * 10%`
- 📌 **Constante**: `pi`
- 🔁 **Trigonométricas**: `sin(x)`, `cos(x)`, `tan(x)` (radianes)
- 🧮 **Combinatoria**: `comb(n,k)`
- 🔢 **Cambio de base numérica**: `bin(x)`, `hex(x)`, `oct(x)` 
- 🔢 **Números decimales y negativos**: Soporta `-5.5 * 2.3`
- ⚠️ **Validación**: Maneja división por cero y expresiones inválidas
- 🔄 **Loop interactivo**: Múltiples cálculos en una sesión / interfaz de botones / interfaz web

## Versiones

### 1. Calculadora de Consola (`calculadora.py`)

Interfaz de línea de comandos interactiva.

#### Ejecutar

```bash
python calculadora.py
```

### Ejemplos de operaciones

```
Calculadora (ej: 5 + 3) o 'exit': 5 + 3
Resultado: 5.0 + 3.0 = 8.0

Calculadora (ej: 5 + 3) o 'exit': 10 - 2
Resultado: 10.0 - 2.0 = 8.0

Calculadora (ej: 5 + 3) o 'exit': 4 * 2
Resultado: 4.0 * 2.0 = 8.0

Calculadora (ej: 5 + 3) o 'exit': 8 / 2
Resultado: 8.0 / 2.0 = 4.0
```

### Salir del programa

Escribe `exit` o `q` para terminar:

```
Calculadora (ej: 5 + 3) o 'exit': exit
¡Hasta luego!
```

### 2. Calculadora con GUI (`calculadora_gui.py`)

Interfaz gráfica con Tkinter. Incluye:
- Display de números
- Botones numéricos (0-9)
- Operadores (+, -, *, /)
- Exponenciación `**`
- Porcentaje `%`
- `pi`, `sin`, `cos`, `tan`, `sqrt`, `root`, `comb`, `bin`, `hex`, `oct`
- Botón "=" para calcular
- Botón "C" para limpiar
- Punto decimal

#### Ejecutar

```bash
python calculadora_gui.py
```

**Características:**
- ✨ Interfaz intuitiva con botones
- 🖱️ Click para ingresar números y funciones
- ⚠️ Manejo automático de errores (división por cero, expresiones inválidas)

### 3. Calculadora Web (`calculadora_web.py`)

Interfaz web estática con JavaScript. Abre en el navegador de GitHub Codespaces.

#### Ejecutar

```bash
python calculadora_web.py
```

Luego expón el puerto `8000` desde la pestaña Ports de Codespaces y abre la URL publicada.

**Características:**
- 🌐 Interfaz web moderna
- 📱 Responsive para pantallas pequeñas
- ✅ Soporta expresiones avanzadas
- 💯 Porcentajes, exponenciación y raíces
- 📌 `pi`, `sin`, `cos`, `tan`, `sqrt`, `root`, `comb`, `bin`, `hex`, `oct`
- ⚠️ Validación de expresión básica

## Manejo de errores

- **División por cero**: Muestra `Error: División por cero`
- **Entrada inválida**: Muestra `Formato inválido. Usa: número operador número`

## Requisitos

- Python 3.x

## Estructura del código

### Versión Consola
- **Evaluación segura**: `safe_eval()` con funciones permitidas
- **Soporte avanzado**: `%`, `^`, `pi`, `sin`, `cos`, `tan`, `sqrt`, `root`, `comb`, `bin`, `hex`, `oct`
- **Loop infinito**: Continúa hasta que el usuario salga

### Versión GUI
- **Clase Calculadora**: Hereda de Tkinter
- **Botones dinámicos**: Generados con grid layout
- **Display**: StringVar para actualizar en tiempo real
- **Métodos**: `agregar()`, `limpiar()`, `calcular()`
- **Funciones avanzadas**: `pi`, `sin`, `cos`, `tan`, `sqrt`, `root`, `comb`, `bin`, `hex`, `oct`

### Versión Web
- **HTML/CSS/JS**: Interfaz de navegador y botones interactivos
- **Expresiones**: Paréntesis, `pi`, `%`, `**`, trigonométricas y cambios de base
- **JavaScript**: Procesa la expresión en el cliente antes de `eval()`

---

*Creado para práctica de programación Python*
