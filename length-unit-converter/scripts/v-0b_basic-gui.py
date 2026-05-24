# Length Unit Converter

# Version: 0.2
# Author: github.com/kuranez


import ipywidgets as widgets
from IPython.display import display

# --- GUI - Elemente -----------------------------------------------------------
# Titel & Beschreibung
title = widgets.Label(value = "Einheitenumrechner für Längenmaße")
description = widgets.Label(value = "Tool zum Umrechnen von Längenmaßen in SI-Einheiten")

# Feld für Eingabe
value_in = widgets.FloatText(value=10**0, description='Eingabe:')
value_out = widgets.FloatText(value=10**0, description='Ausgabe:', disabled=True)

# Menüs für Einheiten
unit_in = widgets.Dropdown(options=[('m', 10**0), ('km', 10**3), ('mm', 10**-3)], value=10**0, description='von Einheit:')
unit_out = widgets.Dropdown(options=[('m', 10**0), ('km', 10**3), ('mm', 10**-3)], value=10**0, description='in Einheit:')

# Output
out = widgets.Output()

# Button
submit_button = widgets.Button(description='Konvertieren')

# --- Funktionen ---------------------------------------------------------------
# Berechnung
def calculate(value_in, unit_in, unit_out):
  return value_in.value * unit_in.value / unit_out.value

# Ausführung
def submit(button):
    value_out.value = calculate(value_in, unit_in, unit_out)
    out.clear_output()
    with out:
        display(value_out.value)

# --- Ausführung ---------------------------------------------------------------
# Trigger
submit_button.on_click(submit)


# --- Anzeige ------------------------------------------------------------------
display(title, description, value_in, unit_in, value_out, unit_out, submit_button)