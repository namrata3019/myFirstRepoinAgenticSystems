def calculate_averages(users):
    averages = {}
    for user in users:
        averages[user["name"]] = sum(user["scores"]) / len(user["scores"])
    return averages


def has_admin_access(roles):
    return "admin" in roles


def main():
    users = [
        {
            "name": "Alice",
            "scores": [80, 85, 82, 83],
            "roles": {"admin", "editor"}
        },
        {
            "name": "Bob",
            "scores": [70, 75, 78, 72],
            "roles": {"viewer"}
        },
        {
            "name": "Charlie",
            "scores": [90, 88, 92, 91],
            "roles": {"editor", "viewer"}
        }
    ]

    averages = calculate_averages(users)

    for user in users:
        result = (
            user["name"],
            averages[user["name"]],
            has_admin_access(user["roles"])
        )

        print("Name:", result[0])
        print("Average Score:", round(result[1], 2))
        print("Admin Access:", result[2])
        print()


main()
