#!/usr/bin/python

from os import system, name
#from tkinter import Tk
from tkinter.filedialog import askopenfilename
import time
import json
import re


def clear_screen():
    '''funzione per eliminare le scritte della console'''
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def draw_menu():
    """disegna il menu"""
    print("1) Cerca nella conversazione")
    print("2) Stampa la conversazione")


def convert_to_json(input_file):
    count = 0
    fout = open("output.json", "w")
    fin = open(file_da_leggere)
    for riga in fin:
        parola = riga.split()
        count += 1
        if parola == []:
            pass
        elif re.match(r"\d{0,9}\d{0,9}/\d{0,9}\d{0,9}/\d{0,9}\d{0,9}",
                      parola[0]):
            msg = ""
            for elem in parola[3:]:
                msg = msg + " " + elem
            dizionario = {
                "line": count,
                "data": f"{parola[0]} {parola[1]}",
                "messaggio": msg
            }
            json.dump(dizionario, fout, indent=4)
            fout.write("\n\n")

        else:
            msg = ""
            for elem in parola:
                msg = msg + " " + elem
            dizionario = {
                "line": count,
                "data": "vedi sopra",
                "messaggio": msg
            }
            json.dump(dizionario, fout, indent=4)
            fout.write("\n\n")

    return 1


def find_word(word):
    '''trova una parola chiave all'interno del file'''
    localcounter = 0
    value = 0
    fin = open(file_da_leggere)
    for riga in fin:
        localcounter += 1
        parola = riga.split()
        for lemma in parola:
            if re.search(word, lemma, re.IGNORECASE):
                print(f"[line {localcounter}] {riga}\n")
                value += 1
    return value


def open_file():
    # Tk.withdraw()
    filename = askopenfilename()
    return filename


def main():
    clear_screen()
    print(f"Hai aperto il file {file_da_leggere}\n")

    # conta le righe del file
    counter = 0
    fin = open(file_da_leggere)
    for riga in fin:
        counter += 1
    print(f"Il file in lettura è formato da {counter} righe.\n")

    key = input("inserisci il testo da cercare: ")
    clear_screen()
    result = find_word(key)
    print(f"risultati della ricerca '{key}' in '{file_da_leggere}':")
    print(f"{result} corrispondenze trovate\n")
    convert_to_json(file_da_leggere)


if __name__ == "__main__":
    clear_screen()
    # comment or uncomment the two following lines to select the input file
    # input("\nInserisci il percorso del file da leggere:\n")
    file_da_leggere = open_file()
    # file_da_leggere = "/home/benny/Scrivania/Pollini.txt"
    main()
