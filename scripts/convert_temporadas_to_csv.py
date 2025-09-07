import argparse, json
import pandas as pd
from pathlib import Path

def main(inp: str, out: str):
    inp_p = Path(inp)
    out_p = Path(out)
    out_p.mkdir(parents=True, exist_ok=True)

    with open(inp_p, encoding="utf-8") as f:
        data = json.load(f)

    teams_list = []
    players_list = []
    HomeTeam = True

    for match_id, teams in (data or {}).items():
        for team_id, entry in (teams or {}).items():
            team_details = (entry or {}).get("team_details", {}) or {}
            aggregate_stats = (entry or {}).get("aggregate_stats", {}) or {}
            player_stats_all = (entry or {}).get("Player_stats", {}) or {}

            # Team row
            row = dict(team_details)
            row.setdefault("team_id", team_id)
            row["match_id"] = match_id
            row["team"] = "L" if HomeTeam else "V"
            HomeTeam = not HomeTeam
            row.update(aggregate_stats)
            teams_list.append(row)

            # Players rows
            for pkey, pobj in (player_stats_all or {}).items():
                pdet = (pobj or {}).get("player_details", {}) or {}
                pms  = (pobj or {}).get("Match_stats", {}) or {}
                prow = {}
                prow.update(pdet)
                prow.update(pms)
                prow["match"] = match_id
                prow["team"] = team_id
                prow["player_name"] = pdet.get("player_name") or str(pkey)
                players_list.append(prow)

    df_teams = pd.DataFrame(teams_list)
    df_players = pd.DataFrame(players_list)

    def reorder(df, first_cols):
        existing = [c for c in first_cols if c in df.columns]
        rest = [c for c in df.columns if c not in existing]
        return df[existing + rest]

    df_teams = reorder(df_teams, ["match_id", "team_id", "team_name", "team"])
    df_players = reorder(df_players, ["match", "team", "player_name"])

    df_teams.to_csv(out_p / "TeamsJSON.csv", index=False, encoding="utf-8")
    df_players.to_csv(out_p / "JugadoresJSON.csv", index=False, encoding="utf-8")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True, help="Ruta del temporadas.json")
    ap.add_argument("--out", dest="out", required=True, help="Carpeta de salida CSV")
    args = ap.parse_args()
    main(args.inp, args.out)
