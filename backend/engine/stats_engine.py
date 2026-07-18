from backend.engine.history_engine import HistoryEngine


class StatsEngine:

    def __init__(self):
        self.history = HistoryEngine()

    def analyse(self, team_name):

        matches = self.history.last_matches(team_name, 10)

        played = 0

        wins = 0
        draws = 0
        losses = 0

        goals_for = 0
        goals_against = 0

        clean_sheets = 0
        failed_to_score = 0

        recent_points = 0
        recent_gf = 0
        recent_ga = 0

        home_gf = 0
        home_ga = 0
        home_games = 0

        away_gf = 0
        away_ga = 0
        away_games = 0

        for i, match in enumerate(matches):

            home = match["homeTeam"]["name"] == team_name

            home_goals = match["score"]["fullTime"]["home"]
            away_goals = match["score"]["fullTime"]["away"]

            if home_goals is None or away_goals is None:
                continue

            if home:
                gf = home_goals
                ga = away_goals
            else:
                gf = away_goals
                ga = home_goals

            played += 1

            goals_for += gf
            goals_against += ga

            if home:
                home_gf += gf
                home_ga += ga
                home_games += 1
            else:
                away_gf += gf
                away_ga += ga
                away_games += 1

            if ga == 0:
                clean_sheets += 1

            if gf == 0:
                failed_to_score += 1

            if gf > ga:
                wins += 1
                if i < 5:
                    recent_points += 3

            elif gf == ga:
                draws += 1
                if i < 5:
                    recent_points += 1

            else:
                losses += 1

            if i < 5:
                recent_gf += gf
                recent_ga += ga

        if played == 0:

            return {
                "played": 0,
                "wins": 0,
                "draws": 0,
                "losses": 0,
                "gf": 0,
                "ga": 0,
                "goal_difference": 0,
                "avg_gf": 0,
                "avg_ga": 0,
                "goal_difference_avg": 0,
                "points_per_game": 0,
                "recent_points": 0,
                "recent_points_per_game": 0,
                "recent_avg_gf": 0,
                "recent_avg_ga": 0,
                "home_avg_gf": 0,
                "home_avg_ga": 0,
                "away_avg_gf": 0,
                "away_avg_ga": 0,
                "clean_sheets": 0,
                "failed_to_score": 0,
                "clean_sheet_rate": 0,
                "failed_to_score_rate": 0
            }

        recent_matches = min(played, 5)

        return {

            "played": played,

            "wins": wins,
            "draws": draws,
            "losses": losses,

            "gf": goals_for,
            "ga": goals_against,

            "goal_difference": goals_for - goals_against,

            "avg_gf": round(goals_for / played, 2),
            "avg_ga": round(goals_against / played, 2),

            "goal_difference_avg": round(
                (goals_for - goals_against) / played,
                2
            ),

            "points_per_game": round(
                (wins * 3 + draws) / played,
                2
            ),

            "recent_points": recent_points,

            "recent_points_per_game": round(
                recent_points / recent_matches,
                2
            ),

            "recent_avg_gf": round(
                recent_gf / recent_matches,
                2
            ),

            "recent_avg_ga": round(
                recent_ga / recent_matches,
                2
            ),

            "home_avg_gf": round(
                home_gf / max(home_games, 1),
                2
            ),

            "home_avg_ga": round(
                home_ga / max(home_games, 1),
                2
            ),

            "away_avg_gf": round(
                away_gf / max(away_games, 1),
                2
            ),

            "away_avg_ga": round(
                away_ga / max(away_games, 1),
                2
            ),

            "clean_sheets": clean_sheets,

            "failed_to_score": failed_to_score,

            "clean_sheet_rate": round(
                clean_sheets / played,
                2
            ),

            "failed_to_score_rate": round(
                failed_to_score / played,
                2
            )

        }