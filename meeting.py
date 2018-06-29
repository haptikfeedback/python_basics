attendees = ["Ken", "Alena", "Treasure"]
attendees.append("Ashley")
attendees.extend(["James", "Guil"])
optional_attendees = ["Ben J.", "Dave"]
potential_attendees = attendees + optional_attendees

print("There are", len(potential_attendees), "potential attendees currently")


