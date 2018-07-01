attendees = ["Ken", "Alena", "Treasure"]
attendees.append("Ashley")
attendees.extend(["James", "Guil"])
optional_attendees = ["Ben J.", "Dave"]
potential_attendees = attendees + optional_attendees

print("There are", len(potential_attendees), "potential attendees currently")

to_line = ", ".join(attendees)
cc_line = ", ".join(optional_attendees)
print("TO: " + to_line)
print("CC: " + cc_line)
