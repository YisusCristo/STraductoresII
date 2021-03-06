import os
from Lexer import *
import tkinter as tk
from tkinter import filedialog


FILE_TYPE = (('text files', '*.txt'), ("all files", "*.*"))


def select_file():
    root = tk.Tk()
    root.withdraw()
    file = filedialog.askopenfilename(filetypes=FILE_TYPE)
    if file == '':
        return None
    return file


if __name__ == '__main__':

    while True:
        text = input('shell > ')
        lexer = Lexer('<stdin>', text)
        tokens, error = lexer.analyze()

        # Imprime el error en caso de que haya encontrado uno
        if error:
            print(error.as_string())
        else:
            print(tokens)

        os.system("pause")
        os.system('cls')
