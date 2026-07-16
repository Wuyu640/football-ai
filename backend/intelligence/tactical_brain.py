from backend.config.tactical_weights import TACTICAL_WEIGHTS


class TacticalBrain:

    def analyse(self, home_profile, away_profile):

        score = 0
        reasons = []

        w = TACTICAL_WEIGHTS

        # Ataque vs defensa

        if (
            home_profile.attack == "High"
            and
            away_profile.defense == "Weak"
        ):
            score += w["attack_vs_defense"]
            reasons.append(
                "El ataque local puede explotar la debilidad defensiva rival."
            )

        if (
            away_profile.attack == "High"
            and
            home_profile.defense == "Weak"
        ):
            score -= w["attack_vs_defense"]
            reasons.append(
                "El ataque visitante puede explotar la defensa local."
            )

        # Porterías a cero

        diff = (
            home_profile.clean_sheet_rate
            - away_profile.clean_sheet_rate
        )

        score += diff * w["clean_sheet"]

        # Regularidad anotando

        diff = (
            home_profile.scoring_rate
            - away_profile.scoring_rate
        )

        score += diff * w["scoring_rate"]

        # Promedio goleador

        diff = (
            home_profile.avg_goals_for
            - away_profile.avg_goals_for
        )

        score += diff * w["avg_goals"]

        # Solidez defensiva

        diff = (
            away_profile.avg_goals_against
            - home_profile.avg_goals_against
        )

        score += diff * w["defense_strength"]

        # Forma

        diff = (
            home_profile.win_rate
            - away_profile.win_rate
        )

        score += diff * w["win_rate"]

        if abs(diff) > 0.30:
            reasons.append(
                "Existe una diferencia clara de forma."
            )

        # Forma reciente

        diff = (
            home_profile.recent_points
            - away_profile.recent_points
        )

        score += diff * w["recent_points"]

        if abs(diff) >= 6:
            reasons.append(
                "La forma reciente favorece claramente a un equipo."
            )

        # Ataque reciente

        diff = (
            home_profile.recent_avg_gf
            - away_profile.recent_avg_gf
        )

        score += diff * w["recent_attack"]

        # Defensa reciente

        diff = (
            away_profile.recent_avg_ga
            - home_profile.recent_avg_ga
        )

        score += diff * w["recent_defense"]

        # Tendencia Over

        diff = (
            home_profile.over25_rate
            - away_profile.over25_rate
        )

        score += diff * w["over25"]

        # Tendencia BTTS

        diff = (
            home_profile.btts_rate
            - away_profile.btts_rate
        )

        score += diff * w["btts"]

        # Rendimiento casa / fuera

        diff = (
            home_profile.home_avg_gf
            - away_profile.away_avg_gf
        )

        score += diff * w["home_attack"]

        if diff > 1:
            reasons.append(
                "El local suele marcar mucho más en casa."
            )

        elif diff < -1:
            reasons.append(
                "El visitante suele rendir muy bien fuera."
            )

        # Ataque muy en forma

        if (
            home_profile.avg_goals_for > 2
            and
            home_profile.recent_avg_gf > 2
        ):
            score += w["hot_attack"]
            reasons.append(
                "El ataque local atraviesa un gran momento."
            )

        if (
            away_profile.avg_goals_for > 2
            and
            away_profile.recent_avg_gf > 2
        ):
            score -= w["hot_attack"]
            reasons.append(
                "El ataque visitante atraviesa un gran momento."
            )

        return {

            "score": round(score, 2),

            "reasons": reasons

        }