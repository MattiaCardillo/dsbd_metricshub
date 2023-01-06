ETL data pipeline -> si crei un microservizio che, per ogni metrica esposta:
- calcoli un set di metadati con i relativi valori (autocorrelazione? stazionarietà?
stagionalità?)
- calcoli il valore di max, min, avg, dev_std della metriche per 1h,3h, 12h;
- Inoltri in un topic Kafka “promethuesdata” un messaggio contenente i valori
calcolati.
Si crei un sistema di monitoraggio interno che renda visibile (tramite REST, log o come
exporter) il tempo necessario all’esecuzione delle varie funzionalità (quanto tempo serve a
generare i dati delle 12 ore per una metrica?