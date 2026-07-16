import Team from "../models/Team";

const teams = {
  "LaLiga EA Sports": [
    new Team({
      id: 1,
      name: "FC Barcelona",
      country: "España",
      competition: "LaLiga EA Sports",
      logo: "",
    }),

    new Team({
      id: 2,
      name: "Real Madrid CF",
      country: "España",
      competition: "LaLiga EA Sports",
      logo: "",
    }),

    new Team({
      id: 3,
      name: "Atlético de Madrid",
      country: "España",
      competition: "LaLiga EA Sports",
      logo: "",
    }),

    new Team({
      id: 4,
      name: "Athletic Club",
      country: "España",
      competition: "LaLiga EA Sports",
      logo: "",
    }),
  ],

  "Premier League": [
    new Team({
      id: 101,
      name: "Manchester City",
      country: "Inglaterra",
      competition: "Premier League",
      logo: "",
    }),

    new Team({
      id: 102,
      name: "Arsenal",
      country: "Inglaterra",
      competition: "Premier League",
      logo: "",
    }),

    new Team({
      id: 103,
      name: "Liverpool",
      country: "Inglaterra",
      competition: "Premier League",
      logo: "",
    }),
  ],

  "Serie A": [],

  "Bundesliga": [],

  "Ligue 1": [],

  "Champions League": [],

  "Europa League": [],

  "Conference League": [],
};

export default teams;