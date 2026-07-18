class XGEngine:

    HOME_BASE_XG = 1.25
    AWAY_BASE_XG = 1.05

    def calculate(self, analysis):

        # ============================
        # MATCHUPS
        # ============================

        home_matchup = analysis["home_attack_vs_away_defense"] / 100
        away_matchup = analysis["away_attack_vs_home_defense"] / 100

        offensive_edge = analysis["offensive_edge"] / 100
        defensive_edge = analysis["defensive_edge"] / 100

        # ============================
        # ÍNDICES
        # ============================

        home_attack = analysis["home_attack_index"] / 100
        away_attack = analysis["away_attack_index"] / 100

        home_defense = analysis["home_defense_index"] / 100
        away_defense = analysis["away_defense_index"] / 100

        # ============================
        # CONTEXTO
        # ============================

        elo_factor = analysis["elo_difference"] / 800

        momentum = analysis["momentum"] / 100

        # ============================
        # XG LOCAL
        # ============================

        home_xg = (

            self.HOME_BASE_XG

            + home_attack * 0.45
            + home_matchup * 0.65

            - away_defense * 0.25

            + offensive_edge * 0.35

            + elo_factor * 0.40

            + momentum * 0.30

        )

        # ============================
        # XG VISITANTE
        # ============================

        away_xg = (

            self.AWAY_BASE_XG

            + away_attack * 0.45
            + away_matchup * 0.65

            - home_defense * 0.25

            - offensive_edge * 0.35

            - elo_factor * 0.40

            - momentum * 0.30

        )

        # ============================
        # AJUSTE DEFENSIVO
        # ============================

        home_xg -= max(defensive_edge, 0) * 0.10
        away_xg += min(defensive_edge, 0) * 0.10

        # ============================
        # LÍMITES
        # ============================

        home_xg = round(
            max(0.20, min(4.50, home_xg)),
            2
        )

        away_xg = round(
            max(0.20, min(4.50, away_xg)),
            2
        )

        return {

            "home_xg": home_xg,

            "away_xg": away_xg

        }