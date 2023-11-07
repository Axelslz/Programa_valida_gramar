import tkinter as tk
import re

class validador:
    def __init__(self, root):
        self.root = root
        self.root.title("Logixx")
        self.text_widget = tk.Text(root, wrap=tk.WORD, height=15, width=50)
        self.text_widget.pack(expand=tk.YES, fill=tk.BOTH)
        self.validation_button = tk.Button(root, text="Validar", command=self.validate_code)
        self.validation_button.pack()
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def validate_code(self):
        code = self.text_widget.get("1.0", tk.END)
        if self.is_valid_code(code):
            self.result_label.config(text="Código válido")
        else:
            self.result_label.config(text="Código inválido")

    def is_valid_code(self, code):
        # Expresiones regulares para validar la declaración de variables y estructuras de funciones/sentencias
        variable_pattern = r"(int|string|bool)\s+\$\w+\s*=\s*(\d+|\".*?\"|true|false);"
        function_pattern = r"func\s+\w+\s*\(\s*(int|string|bool)\s+\$\w+\s*,\s*(int|string|bool)\s+\$\w+\s*\)\s*:\s*(int|string|bool)\s*{\s*retornar\s+\$\w+\s*[\+\-\/*]\s+\$\w+\s*;\s*}"
        repeat_pattern = r"repeat\s+\(int\s+\$\w+\s*=\s*\d+;\s+\$\w+\s*(<|<=|>|>=|==|!=)\s*\d+;\s+\$\w+\s*\+\+|\$\w+\s*--\)\s*{\s*.*\s*}"
        if_pattern = r"if\s+\(\s*\$\w+\s*(>|<)\s*\d+\)\s*{\s*.*\s*}\s*(else\s*{\s*.*\s*})?"
        main_pattern = r"func\s+main\(\)\s*{\s*.*\s*}"

        # Validar la declaración de variables, estructura de la función y sentencias
        if re.match(variable_pattern, code) or re.match(function_pattern, code) or re.match(repeat_pattern, code) or re.match(if_pattern, code) or re.match(main_pattern, code):
            # Verificar si falta alguna expresión en las declaraciones de variables
            lines = code.strip().split('\n')
            for line in lines:
                if re.match(variable_pattern, line):
                    if "=" not in line:
                        return False
            return True

        return False

if __name__ == "__main__":
    root = tk.Tk()
    ide_simulator = validador(root)
    root.mainloop()
