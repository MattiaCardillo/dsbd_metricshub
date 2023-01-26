import pandas as pd
from statsmodels.tsa.stattools import adfuller, acf
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf

def parseIntoSeries(list, metricName):
    df = pd.DataFrame.from_records(list, columns=["timestamp", "value"])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s', yearfirst=True)

    # Imposta l'indice del dataframe come il campo temporale
    df.set_index("timestamp", inplace=True)

    # Adesso ho un dataframe con una colonna (i valori) e come indici ho tutti i timestamp

    #In questo momento la frequenza di campionamento è null, posso farmi un resampling forzando la frequenza ad 1 secondo.

    tsr = df.resample(rule='T').mean()

    # rolling --> media mobile --> riduco il rumore, ottengo una versione approssimata utile per effettuare delle predizioni. 
    # perdo dettagli ma ho una visione più chiara del trand della serie
    # tsrR = tsr.rolling(window=60).mean()
    # tsr = tsr.bfill()

    plt.title(metricName)
    plt.figure(figsize=(24,10), dpi=100)

    plt.xlabel('Time', fontsize=14)
    plt.ylabel('Values', fontsize=14)

    plt.plot(tsr, '-', label=metricName)

    plt.legend(title="series")

    filename='tmp/'+metricName
    plt.savefig(filename)
    plt.close()

    return tsr

def stationarityTest(ts):
    testResult = "No test"

    # Esegue il test di Dickey-Fuller sulla serie temporale x utilizzando il metodo AIC --> miglior subset di campioni
    result = adfuller(ts['value'], autolag="AIC")

    # Ottiene il valore p del test
    p_value = result[1]

    # Verifica se la serie temporale è stazionaria
    if p_value < 0.05:
        print("La serie temporale è stazionaria")
        testResult = "La serie temporale è stazionaria"
    else:
        testResult = "La serie temporale non è stazionaria"
    return testResult


def seasonabilityTest(ts, selectedMetric):

    try:
        ts = ts.rolling(window=60).mean()
        ts = ts.bfill()
        # Esegue la decomposizione stagionale della serie
        result = seasonal_decompose(ts['value'],model=selectedMetric['params']['model'], period=selectedMetric['params']['period'])

        # Stampa i componenti della decomposizione
        # print("Trend:", result.trend)
        # print("Stagionale:", result.seasonal)
        # print("Residui:", result.resid)

        # Crea il grafico
        plt.plot(result.trend)

        # Aggiungi un titolo al grafico
        plt.title('Trend della serie temporale')

        filename='tmp/trend'+selectedMetric['name']+'.png'
        plt.savefig(filename)
        plt.close()

        # Crea il grafico
        plt.plot(result.resid)

        # Aggiungi un titolo al grafico
        plt.title('Resuidi della serie temporale')

        filename='tmp/residui'+selectedMetric['name']+'.png'
        plt.savefig(filename)
        plt.close()

        # Crea il grafico
        plt.plot(result.seasonal)

        # Aggiungi un titolo al grafico
        plt.title('Stagionalità della serie temporale')

        filename='tmp/seasonability'+selectedMetric['name']+'.png'
        plt.savefig(filename)
        plt.close()
        
    except Exception as e:
        print(e)

    return filename

def autocorrelationTest(ts):
    # autocorr = acf(ts['value'], nlags=10)

    # # Stampa i valori di autocorrelazione
    # print(autocorr)

    # #I valori di autocorrelazione saranno compresi tra -1 e 1, dove valori prossimi a 1 indicano una forte autocorrelazione positiva 
    # # (cioè i dati tendono a seguire una tendenza), mentre valori prossimi a -1 indicano una forte autocorrelazione negativa 
    # # (cioè i dati tendono a muoversi in modo opposto alla tendenza). 
    # # Valori prossimi a zero indicano una debole autocorrelazione o assenza di autocorrelazione.
    # plt.bar(range(len(autocorr)), autocorr)
    plt = plot_acf(ts, title='acf',lags=50) #non stationary data decrease very slow

    # Aggiungi un titolo al grafico
    # plt.title('Autocorrelazione della serie temporale')
    filename='tmp/atf.png'
    # Mostra il grafico
    plt.savefig(filename)
    
    return filename