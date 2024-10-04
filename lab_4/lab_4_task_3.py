#----------------------------- Реалізувати задачу про базу даних з голосування депутатів.

# База депутатів
deputies = {
    1: {"name": "Депутат 1", "party": "Партія A", "vote": None},
    2: {"name": "Депутат 2", "party": "Партія B", "vote": None},
    3: {"name": "Депутат 3", "party": "Партія A", "vote": None},
}

# Функція для проведення голосування
def vote_on_issue(issue, votes):
    print(f"Голосування по питанню: {issue}")
    for dep_id, dep_info in deputies.items():
        if dep_id in votes:
            deputies[dep_id]["vote"] = votes[dep_id]
        else:
            deputies[dep_id]["vote"] = "утримався"

    # Підрахунок голосів
    results = {"за": 0, "проти": 0, "утримався": 0}
    for dep_info in deputies.values():
        vote = dep_info["vote"]
        results[vote] += 1

    print(f"Результати голосування: {results}")
    return results

# Приклад голосування
votes = {1: "за", 3: "проти", 2: "проти"}
vote_on_issue("Питання про бюджет", votes)
