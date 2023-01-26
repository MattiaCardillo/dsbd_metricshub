ETL data pipeline -> si crei un microservizio che, per ogni metrica esposta:
- calcoli un set di metadati con i relativi valori (autocorrelazione? stazionarietà?
stagionalità?)
- calcoli il valore di max, min, avg, dev_std della metriche per 1h,3h, 12h;
- Inoltri in un topic Kafka “promethuesdata” un messaggio contenente i valori
calcolati.
Si crei un sistema di monitoraggio interno che renda visibile (tramite REST, log o come
exporter) il tempo necessario all’esecuzione delle varie funzionalità (quanto tempo serve a
generare i dati delle 12 ore per una metrica?

Stazionarietà:
Una serie si dice stazionaria se non esibisce trend o stagionalità. quindi media, varianza e covarianza non dipendono dal tempo ma sono uguali in tutte i segmenti temporali.

Si può vedere se una serie è stazionaria tramite il test di dickey-fuller
-Prendo la serie 
-Effettuo il resample (gli do almeno frequenza = T)
-Vedo se è stazionaria con Adfuller

Stagionalità:
Una serie si dice "stagionale", se presenta pattern comportamentali che si ripresentano nel tempo.
-Prendo la serie (così com'è)
-Effettuo il resample, il rolling (?), ed il bfill (?)
-Effettuo la seasonal decompose effettuando tentativi con:
    -model="mul" | model ="add"
    -period = "100" ecc
    -Devo fare in modo che, guardando questi parametri il mio risultato finale abbia un residuo simile a rumore bianco
    (attorno allo zero)
    -Il trend inoltre non deve essere una funzione stagionale OK!

Autocorrelazione:
Una serie è autocorrelata quando c'è una correlazione dal campione k al k-1 per ogni kesimo elemento della serie

Autocorrelazione parziale:
Una serie è autocorrelata parzialmente quando c'è una correlazione dal campione k al k-1 per alcune porzioni della serie