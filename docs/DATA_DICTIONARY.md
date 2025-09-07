# Diccionario de Datos (resumen)

## Equipo–Partido
- `match_id (int)`: identificador del partido.
- `team_id (int)`: identificador del equipo.
- `team_name (str)`: nombre del equipo.
- `team (str)`: local/visitante (L/V).
- `team_rating (double)`: calificación algorítmica del equipo.
- `date (date)`: fecha del partido.
- `won_corners (int)`: córners ganados.
- `att_sv_low_centre (int)`: tiros a puerta salvados (zona baja-centro).
- `won_contest (int)`: duelos ganados.
- `total_tackle (int)`: entradas (tackles).
- `aerial_lost (int)`: duelos aéreos perdidos.
- `possession_percentage (double)`: % posesión.
- `accurate_pass (int)`: pases completados.

## Perfil de jugador (plantilla)
- `name, club, age, position, position_cat, market_value, page_views, fpl_*` etc.: metadatos del jugador y variables ingenierizadas del dataset.

## Jugador–Partido
- `match, team, player_name, player_id`: identificadores.
- `player_position_value/info`: posición/rol en el partido.
- `player_rating (double)`: rating del jugador.
- `good_high_claim (int)`: atrapadas altas con éxito (GK).
- `touches, saves, total_pass, accurate_pass, fouls` etc.: eventos/acciones.
- `total_scoring_att, ontarget_scoring_att, shot_off_target, blocked_scoring_att`:
  tiros totales, a puerta, fuera, bloqueados.
- `aerial_won/lost, total_tackle, won_contest`: duelos y defensa.
- `formation_place (int)`: índice de posición en la formación.

## Resultados de partido (formato clásico)
- `HomeTeam, AwayTeam, FTHG, FTAG, FTR, HTHG, HTAG, HTR, HS/AS, HST/AST, HC/AC, HF/AF, HY/AY, HR/AR`:
  métricas standard de resultado, tiros, córners, faltas y tarjetas.
