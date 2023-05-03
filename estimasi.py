import pickle
import streamlit as sl

model = pickle.load(open('estimasi_fuel.sav', 'rb'))

sl.title('Estimasi Peringkat Konsumsi Bahan Bakar Tahun 2022')
sl.write('---')

EngineSize = sl.number_input('Input Total EngineSize')
Cylinders = sl.number_input('Input Total Cylinders')
FuelConsumptionCity = sl.number_input('Input Total FuelConsumptionCity')
FuelConsumptionHwy = sl.number_input('Input Total FuelConsumptionHwy')
FuelConsumptionCombMPG = sl.number_input('Input Total FuelConsumptionCombMPG')
CO2Emissions = sl.number_input('Input Total CO2Emissions')
CO2Rating = sl.number_input('Input Total CO2Rating')
SmogRating = sl.number_input('Input Total SmogRating')


predict = ''

if sl.button('Cek Rating'):
    predict = model.predict(
        [[EngineSize,Cylinders,FuelConsumptionCity,FuelConsumptionHwy,FuelConsumptionCombMPG,CO2Emissions,CO2Rating,SmogRating]]
    )
    sl.write ('Estimasi Peringkat Konsumsi Bahan Bakar : ', predict)