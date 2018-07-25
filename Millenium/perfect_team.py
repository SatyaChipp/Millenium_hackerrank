def differentTeams(skills):
    skills_ = {'p', 'c', 'm', 'b', 'z'}
    team_length = len(skills)
    if team_length < 5:  # not enough members to form a team
        return 0
    else:
        if (team_length % 5) == 0:
            counter = Counter(skills)
            if skills_.issubset(set(counter.keys())):
                if len(set(list(counter.values()))) == 1:  ##all values equal
                    return team_length // 5
                else:
                    sd = sorted(counter.values())[0]  # get least value of repeated skills
                    return sd
            else:
                return 0
        else:
            counter = Counter(skills)
            if skills_.issubset(set(counter.keys())):
                sd = sorted(counter.values())[0]  # get least value of repeated skills
                return sd
            else:
                return 0
