import pandas as pd
from statsmodels.tsa.stattools import adfuller, acf
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

def parseIntoSeries(list, metricName):
    df = pd.DataFrame.from_records(list, columns=["timestamp", "value"])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')

    # Imposta l'indice del dataframe come il campo temporale
    df.set_index("timestamp", inplace=True)

    # Adesso ho un dataframe con una colonna (i valori) e come indici ho tutti i timestamp
    
    # Estrae la colonna "value" come una serie temporale
    # series = df["value"].squeeze()

    print(df.index)

    #In questo momento la frequenza di campionamento è null, posso farmi un resampling forzando la frequenza ad 1 secondo.

    tsr = df.resample(rule='T').mean()
    print(tsr.index)

    plt.title(metricName)
    plt.xlabel('Time', fontsize=14)
    plt.ylabel('Values', fontsize=14)
    plt.plot(tsr, '-', label=metricName)

    filename='tmp/'+metricName
    plt.savefig(filename)
    return df

def stationarityTest(ts):
    testResult = "No test"

    # Esegue il test di Dickey-Fuller sulla serie temporale x
    result = adfuller(ts)

    # Ottiene il valore p del test
    p_value = result[1]

    # Verifica se la serie temporale è stazionaria
    if p_value < 0.05:
        print("La serie temporale è stazionaria")
        testResult = "La serie temporale è stazionaria"
    else:
        testResult = "La serie temporale non è stazionaria"
    return testResult


def seasonabilityTest(ts):

    try:
        # Esegue la decomposizione stagionale della serie
        result = seasonal_decompose(ts, period=12)

        # Stampa i componenti della decomposizione
        print("Trend:", result.trend)
        print("Stagionale:", result.seasonal)
        print("Residui:", result.resid)

        # Crea il grafico
        plt.plot(result.seasonal)

        # Aggiungi un titolo al grafico
        plt.title('Stagionalità della serie temporale')

        filename='tmp/seasonability.png'
        plt.savefig(filename)
    except Exception as e:
        print(e)

    return filename

def autocorrelationTest(ts):
    autocorr = acf(ts, nlags=4)

    # Stampa i valori di autocorrelazione
    print(autocorr)

    #I valori di autocorrelazione saranno compresi tra -1 e 1, dove valori prossimi a 1 indicano una forte autocorrelazione positiva 
    # (cioè i dati tendono a seguire una tendenza), mentre valori prossimi a -1 indicano una forte autocorrelazione negativa 
    # (cioè i dati tendono a muoversi in modo opposto alla tendenza). 
    # Valori prossimi a zero indicano una debole autocorrelazione o assenza di autocorrelazione.
    plt.bar(range(len(autocorr)), autocorr)

    # Aggiungi un titolo al grafico
    plt.title('Autocorrelazione della serie temporale')
    filename='tmp/atf.png'
    # Mostra il grafico
    plt.savefig(filename)

    return filename