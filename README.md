Progetto prova in itinere DSBD aa2022-2023

Sia X una applicazione o un componente di una applicazione (K8s, docker, applicazione) che
espone metriche attraverso un Prometheus exporter.
L’exporter può essere già sviluppato o da sviluppare (per team composti da più studenti)
Si configuri un server Prometheus per fare scraping delle metriche esposte dall’exporter.

ETL data pipeline -> si crei un microservizio che, per ogni metrica esposta:
- calcoli un set di metadati con i relativi valori (autocorrelazione? stazionarietà?
stagionalità?)
- calcoli il valore di max, min, avg, dev_std della metriche per 1h,3h, 12h;
- predica il valore di max, min, avg nei successivi 10 minuti per un set ristretto di 5
metriche (SLA Set da SLA Manager)
- Inoltri in un topic Kafka “promethuesdata” un messaggio contenente i valori
calcolati.
Si crei un sistema di monitoraggio interno che renda visibile (tramite REST, log o come
exporter) il tempo necessario all’esecuzione delle varie funzionalità (quanto tempo serve a
generare i dati delle 12 ore per una metrica?)

Data Storage -> si crei un microservizio che avvii un consumer group del topic
“promethuesdata” e, per ogni messaggio prelevato, memorizzi i valori calcolati in un DB a
scelta.

Data Retrieval -> si crei un microservizio che offre una interfaccia REST-o gRPC-based- che
permetta di estrarre in modo strutturato le informazioni generate dall’applicazione ETL e contenute nel DB.
Si rendano disponibili:
- QUERY di tutte le metriche disponibili in Prometheus
- Per ogni metrica
o QUERY dei metadati.
o QUERY dei valori max, min, avg,dev_std per le ultime 1,3,12 ore.
o QUERY dei valori predetti