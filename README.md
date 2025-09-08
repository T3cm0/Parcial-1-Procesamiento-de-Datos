# Parcial – Procesamiento de Datos (Fútbol)

Notebook y utilidades para convertir y analizar datasets de fútbol (equipos/jugadores/resultados) en **CSV/Delta**, pensado para usarse en **Databricks** o localmente con Python.

## Estructura
```
parcial_procesamiento_datos_repo/
├─ notebooks/
│  └─ Parcial_Procesamiento_Datos.ipynb
├─ data/
│  └─ sample/            
├─ docs/
├─ requirements.txt
├─ .gitignore
└─ LICENSE
```

## Uso en Databricks (recomendado)
1. Sube los archivos a un **Volume** p.ej. `/Volumes/workspace/default/parcial`.
2. Abre `notebooks/Parcial_Procesamiento_Datos.ipynb` y ajusta:
   ```python
   BASE = "/Volumes/workspace/default/parcial"
   IN   = f"{BASE}/temporadas.json"
   OUT  = f"{BASE}/csv_out"
   ```
3. Ejecuta las celdas de ingestión/transformación.

## Convertir `temporadas.json` a CSV (sin Spark)
```bash
python scripts/convert_temporadas_to_csv.py   --in /dbfs/Volumes/workspace/default/parcial/temporadas.json   --out /dbfs/Volumes/workspace/default/parcial/csv_out
```

## Licencia
MIT © 2025 Sebastian Rodriguez
