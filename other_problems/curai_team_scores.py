"""
Suppose that one football fan club has designed a website, and they've asked you to create a program for determining the final scoreboard, based on match results which should be published on the website.

It is widely accepted that in football competitions the scores are calculated like this:

The winning team receives 3 points.
The losing team receives 0 points.
In the event of a draw, both teams receive 1 point.
You are given the match results in the format "<team name 1> <goals for team 1>:<goals for team 2> <team name 2>" (For example, Liverpool 3:2 PSG would mean that Liverpool scored 3 points and PSG scored 2, so Liverpool wins).

Your task is to return the final scoreboard - a list of teams names alongside their total points. The scoreboard should be sorted in descending order of points. If there are any ties, return these teams in any order.

Note: Unlike a real league, the teams have not necessarily all played the same number of matches.

Example

For matches = ["Liverpool 3:2 PSG", "RedStar 0:0 Napoli", "PSG 6:1 RedStar", "Napoli 1:0 Liverpool"], the output can be solution(matches) = ["Napoli 4", "Liverpool 3", "PSG 3", "RedStar 1"].

Since Liverpool and PSG have the same number of points, ["Napoli 4", "PSG 3", "Liverpool 3", "RedStar 1"] would also be accepted.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string matches

It is guaranteed that team names do not contain spaces. Each name has at most 16 characters.

Guaranteed constraints:
1 ≤ matches.length ≤ 100.

[output] array.string

Return the array of teams with their total points, sorted in descending order of points.
"""

from collections import Counter


def solution(matches):
    match_summary_map = Counter()
    for match_data in matches:
        s = match_data.split()
        scores = s[1].split(":")
        team_a_name = s[0]
        team_b_name = s[2]

        if int(scores[0]) > int(scores[1]):
            match_summary_map.update({team_a_name: 3})
            if not match_summary_map[team_b_name]:
                match_summary_map.update({team_b_name: 0})
        elif int(scores[0]) == int(scores[1]):
            match_summary_map.update({team_a_name: 1})
            match_summary_map.update({team_b_name: 1})
        else:
            match_summary_map.update({team_b_name: 3})
            if not match_summary_map[team_a_name]:
                match_summary_map.update({team_a_name: 0})

    result = []
    for item in match_summary_map.most_common():
        result.append(item[0] + " " + str(item[1]))
    return result
