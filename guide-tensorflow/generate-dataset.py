# importer nødvendige biblioteker
# random for å generere tilfeldige tall og json for å formatere data som JSON
import json
import random

# Funksjon for å generere data for luft- og havtemperatur
# num_samples er antall datapunkter som skal genereres
def generate_temperature_data(num_samples=1000):
    # Tom liste for å lagre data
    data = []

    # Start en loop for å generere data
    for _ in range(num_samples):

        # Generer en tilfeldig lufttemperatur mellom 0 og 35 grader
        air_temp = random.uniform(0, 35)

        # Generer havtemperatur basert på lufttemperatur med noe variasjon
        # Havtemperaturen er satt til 70% av lufttemperaturen pluss/minus 2 grader
        sea_temp = air_temp * 0.7 + random.uniform(-2, 2)

        # Legg til data i listen
        data.append({
            "air_temperature": round(air_temp, 2),
            "sea_temperature": round(sea_temp, 2)
        })

    return data

# Funksjon for å lagre data til en JSON-fil
# data er dataene som skal lagres, filename er filnavnet som skal brukes
def save_data_to_json(data, filename="temperature_data.json"):
    
    # Åpne filen i skrivemodus og lagre data som JSON
    with open(filename, "w") as json_file:

        # Bruk json.dump for å lagre data til filen
        json.dump(data, json_file, indent=4)

# Generer datasettet og lagre det som en JSON fil
dataset = generate_temperature_data(1000)  # Generer 1000 datapunkter

save_data_to_json(dataset)