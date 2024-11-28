import pandas as pd
from sklearn.model_selection import train_test_split
import json
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# Last inn datasettet fra JSON-filen
with open("temperature_data.json", "r") as f:
    data = json.load(f)

# Konverter data til en Pandas DataFrame
df = pd.DataFrame(data)

# Definer input (X) og output (y)
X = df["air_temperature"].values.reshape(-1, 1)
y = df["sea_temperature"].values

# Del data i trening- og testsett (80% trening, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Opprett et Sequential-objekt og legg til lag
model = Sequential([
    Dense(16, input_shape=(1,), activation="relu"),
    Dense(8, activation="relu"),
    Dense(1)  # Output lag
])

# Kompiler modellen med Adam-optimizer og Mean Squared Error som loss-funksjon
model.compile(optimizer=Adam(learning_rate=0.01), loss="mean_squared_error")

# Skriv ut en oppsummering av modellen
model.summary()

# Tren modellen på treningsdata med 100 epoker og batch-størrelse 8, og lagre treningshistorikken
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=100, batch_size=8, verbose=1)

# Evaluer modellen på testsettet
test_loss = model.evaluate(X_test, y_test, verbose=1)
print(f"Test Loss (Mean Squared Error): {test_loss}")

# Bruk matplotlib til å visualisere testdata prosessert av modellen
predictions = model.predict(X_test)

plt.scatter(X_test, y_test, label="Faktiske verdier", color="blue")
plt.scatter(X_test, predictions, label="Predikerte verdier", color="red")
plt.xlabel("Lufttemperatur (°C)")
plt.ylabel("Havtemperatur (°C)")
plt.legend()
plt.show()

# Lagre modellen til en fil
model.save("temperature_model.h5")
print("Modellen ble lagret.h5")

