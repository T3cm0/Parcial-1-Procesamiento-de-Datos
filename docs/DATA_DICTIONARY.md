# Diccionario de Datos (resumen)

### Glosario jugadores.csv
- `name (string)`: nombre del jugador.
- `club (string)`: club actual.
- `age (int)`: edad del jugador (años).
- `position (string)`: posición principal (p. ej., GK/DF/MF/FW).
- `position_cat (int)`: categoría numérica de posición (definida por el dataset; p. ej., 1=GK, 2=DF, 3=MF, 4=FW).
- `market_value (double)`: valor de mercado estimado (no es la tarifa de traspaso).
- `page_views (int)`: vistas de página/popularidad (según la fuente del dataset).
- `fpl_value (double)`: “valor” en Fantasy Premier League (p. ej., puntos/precio).
- `fpl_sel (string)`: “Selected by %” — porcentaje de mánagers FPL que poseen al jugador (ej.: "23.4" o "23.4%").
- `fpl_points (int)`: puntos FPL acumulados (según el sistema oficial).
- `region (string)`: región del jugador en el dataset (ej.: "Europe").
- `nationality (string)`: país/nacionalidad del jugador.
- `new_foreign (int)`: indicador (0/1) de extranjero recién incorporado al club en la temporada (según reglas del dataset).
- `age_cat (int)`: categoría/bins de edad (definida por el dataset; confirmar mapeo real).
- `club_id (int)`: identificador del club en el proveedor/dataset.
- `big_club (int)`: indicador (0/1) de “club grande” (criterio del dataset; ej., Big-6).
- `new_signing (int)`: indicador (0/1) de fichaje reciente (aclarar si incluye cesiones).

### Glosario resultados_futbol.csv
- `Season (string)`: temporada (p. ej., "2018/2019").
- `DateTime (timestamp)`: fecha y hora del kickoff.
- `HomeTeam (string)`: equipo local.
- `AwayTeam (string)`: equipo visitante.
- `FTHG (int)`: goles del local al final del partido.
- `FTAG (int)`: goles del visitante al final del partido.
- `FTR (string)`: resultado final — H (gana local), D (empate), A (gana visitante).
- `HTHG (string/int)`: goles del local al descanso.
- `HTAG (string/int)`: goles del visitante al descanso.
- `HTR (string)`: resultado al descanso — H/D/A.
- `Referee (string)`: árbitro principal.
- `HS (string/int)`: tiros del equipo local.
- `AS (string/int)`: tiros del equipo visitante.
- `HST (string/int)`: tiros a puerta del local.
- `AST (string/int)`: tiros a puerta del visitante.
- `HC (string/int)`: córners del local.
- `AC (string/int)`: córners del visitante.
- `HF (string/int)`: faltas cometidas por el local.
- `AF (string/int)`: faltas cometidas por el visitante.
- `HY (string/int)`: amarillas del local.
- `AY (string/int)`: amarillas del visitante.
- `HR (string/int)`: rojas del local.

### Glosario TeamsJSON.csv
- `match_id (int)`: identificador único del partido.
- `team_id (int)`: identificador del equipo (proveedor).
- `team_name (string)`: nombre del equipo.
- `team (string)`: condición en el partido — "L" local, "V" visitante.
- `team_rating (double)`: calificación algorítmica del rendimiento del equipo.
- `date (date)`: fecha del partido.
- `won_corners (int)`: córners ganados por el equipo.
- `att_sv_low_centre (int)`: tiros a puerta del rival parados por el portero, dirigidos a la zona baja–central.
- `won_contest (int)`: duelos ganados (aéreos/terrestres según proveedor).
- `total_tackle (int)`: entradas (tackles) realizadas.
- `aerial_lost (int)`: duelos aéreos perdidos.
- `possession_percentage (double)`: porcentaje de posesión (0–100).
- `accurate_pass (int)`: pases completados por el equipo.

### Glosario JugadoresJSON.csv
- `match (int)`: identificador del partido. 
- `team (int)`: identificador/código del equipo en ese partido.  
- `player_name (string)`: nombre del jugador en el registro del partido.  
- `player_id (int)`: identificador del jugador.  
- `player_position_value (int)`: codificación numérica de la posición/rol en el partido.  
- `player_position_info (string)`: texto descriptivo de la posición/rol en el partido.  
- `player_rating (double)`: calificación algorítmica del rendimiento individual.  
- `good_high_claim (int)`: **portero** – balones aéreos altos atrapados con éxito (no “punch”).  
- `touches (int)`: toques de balón.  
- `saves (int)`: **portero** – paradas (tiros a puerta detenidos).  
- `total_pass (int)`: pases intentados.  
- `formation_place (int)`: índice/posición dentro del once según el dibujo táctico.  
- `accurate_pass (int)`: pases completados (acertados).  
- `aerial_won (int)`: duelos aéreos ganados.  
- `aerial_lost (int)`: duelos aéreos perdidos.  
- `fouls (int)`: faltas cometidas.  
- `total_scoring_att (int)`: tiros totales (attempts).  
- `total_tackle (int)`: entradas realizadas.  
- `won_contest (int)`: duelos ganados (incluye aéreos/terrestres según proveedor).  
- `penalty_conceded (int)`: penaltis concedidos por el jugador.  
- `blocked_scoring_att (int)`: tiros del rival bloqueados.  
- `man_of_the_match (int)`: indicador del premio “Jugador del partido”.
