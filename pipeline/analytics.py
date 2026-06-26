import pandas as pd


def team_win_percentage(matches):
    """
    Calculate win percentage for every IPL team.
    """

    # Remove matches with no winner
    completed_matches = matches.dropna(subset=["winner"])

    # Matches played
    team1 = completed_matches["team1"].value_counts()
    team2 = completed_matches["team2"].value_counts()

    matches_played = team1.add(team2, fill_value=0)

    # Matches won
    matches_won = completed_matches["winner"].value_counts()

    # Summary
    summary = pd.DataFrame({
        "Matches Played": matches_played,
        "Matches Won": matches_won
    }).fillna(0)

    summary["Win Percentage"] = (
        summary["Matches Won"] /
        summary["Matches Played"] * 100
    ).round(2)

    summary = summary.sort_values(
        by="Win Percentage",
        ascending=False
    )

    return summary

def top_run_scorers(deliveries, top_n=10):
    """
    Return the top run scorers.
    """

    runs = (
        deliveries
        .groupby("batter")["batsman_runs"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index()
    )

    runs.columns = ["Batter", "Runs"]

    return runs

def top_wicket_takers(deliveries, top_n=10):
    """
    Return the top wicket takers.
    """

    wickets = deliveries[
        deliveries["is_wicket"] == 1
    ]

    wickets = (
        wickets
        .groupby("bowler")
        .size()
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index(name="Wickets")
    )

    return wickets

def most_sixes(deliveries, top_n=10):
    """
    Players with most sixes.
    """

    sixes = deliveries[
        deliveries["batsman_runs"] == 6
    ]

    sixes = (
        sixes
        .groupby("batter")
        .size()
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index(name="Sixes")
    )

    return sixes

def most_fours(deliveries, top_n=10):
    """
    Players with most fours.
    """

    fours = deliveries[
        deliveries["batsman_runs"] == 4
    ]

    fours = (
        fours
        .groupby("batter")
        .size()
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index(name="Fours")
    )

    return fours

def strike_rate(deliveries, min_balls=100):
    """
    Calculate strike rate for batters.
    """

    stats = deliveries.groupby("batter").agg(
        Runs=("batsman_runs", "sum"),
        Balls=("ball", "count")
    )

    stats = stats[stats["Balls"] >= min_balls]

    stats["Strike Rate"] = (
        stats["Runs"] / stats["Balls"] * 100
    ).round(2)

    return (
        stats.sort_values("Strike Rate", ascending=False)
        .reset_index()
    )
def economy_rate(deliveries, min_balls=60):
    """
    Calculate economy rate for bowlers.
    """

    stats = deliveries.groupby("bowler").agg(
        Runs=("total_runs", "sum"),
        Balls=("ball", "count")
    )

    stats = stats[stats["Balls"] >= min_balls]

    stats["Overs"] = stats["Balls"] / 6

    stats["Economy"] = (
        stats["Runs"] / stats["Overs"]
    ).round(2)

    return (
        stats.sort_values("Economy")
        .reset_index()
    )

def boundary_percentage(deliveries):
    """
    Calculate percentage of boundaries scored by each batter.
    """

    total_balls = deliveries.groupby("batter").size()

    boundary_balls = deliveries[
        deliveries["batsman_runs"].isin([4, 6])
    ].groupby("batter").size()

    stats = pd.DataFrame({
        "Balls": total_balls,
        "Boundary Balls": boundary_balls
    }).fillna(0)

    stats["Boundary %"] = (
        stats["Boundary Balls"] /
        stats["Balls"] * 100
    ).round(2)

    return (
        stats.sort_values("Boundary %", ascending=False)
        .reset_index()
    )

def dot_ball_percentage(deliveries):
    """
    Calculate dot ball percentage for bowlers.
    """

    total = deliveries.groupby("bowler").size()

    dots = deliveries[
        deliveries["total_runs"] == 0
    ].groupby("bowler").size()

    stats = pd.DataFrame({
        "Balls": total,
        "Dot Balls": dots
    }).fillna(0)

    stats["Dot Ball %"] = (
        stats["Dot Balls"] /
        stats["Balls"] * 100
    ).round(2)

    return (
        stats.sort_values("Dot Ball %", ascending=False)
        .reset_index()
    )

def venue_statistics(matches):
    """
    Return number of matches played at each venue.
    """

    venue_stats = (
        matches.groupby("venue")
        .size()
        .sort_values(ascending=False)
        .reset_index(name="Matches")
    )

    return venue_stats

def player_of_match_awards(matches, top_n=10):
    """
    Players with the most Player of the Match awards.
    """

    awards = (
        matches["player_of_match"]
        .value_counts()
        .head(top_n)
        .reset_index()
    )

    awards.columns = ["Player", "Awards"]

    return awards

def highest_team_scores(deliveries, top_n=10):
    """
    Highest innings totals in IPL history.
    """

    scores = (
        deliveries
        .groupby(["match_id", "inning", "batting_team"])["total_runs"]
        .sum()
        .reset_index()
    )

    scores = scores.sort_values(
        "total_runs",
        ascending=False
    ).head(top_n)

    return scores

def toss_decision_percentage(matches):
    """
    Percentage of toss decisions.
    """

    decisions = (
        matches["toss_decision"]
        .value_counts(normalize=True)
        .mul(100)
        .round(2)
        .reset_index()
    )

    decisions.columns = ["Decision", "Percentage"]

    return decisions

