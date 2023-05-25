lin = open("lineup.in", "r")

N = lin.readline()
constraints = [constraint.split(" must be milked beside ")
               for constraint in lin.read().splitlines()]





# print(constraints)
# line = ["Bessie"]
# # Insert person after Bessie
# placed = False
# for const in constraints:
#     if "Bessie" in const and not placed:
#         line.append("".join(const).replace("Bessie", ""))
#         placed = True
#     elif "Bessie" in const and placed:
#         line = [
#             line[1], "".join(const).replace("Bessie", "")
#         ].sort().insert(1, "Bessie")
