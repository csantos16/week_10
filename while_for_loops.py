# for loops = execute a block of code a fixed number of times.
# You can iterate over a range, string, sequence, etc,
# for x in range(1,21):
#     if x == 13:
#         continue
#     if x == 15:
#         continue
#     if x == 20:
#         continue
#     else:
#         print(x)
# for x in range(1,21):
#     if x == 13:
#         break
#     else:
#         print(x)
# scary = ("Freddy Krueger", "Jason Voorhees", "Michael Myers", "Pennywise", "Chucky" )
# for x in scary:
#     if scary == "Michael Myers":
#     scary = "Ghostface"
# print(scary)
#   for x in scary:
#     if x == "Jason Voorhees":
#         continue
#     else:
#         print(x)

movie = ("Terrifier", "Scream", "Saw", "Get out")
for x in movie:
     if movie == "Terrifier":
          continue
     if movie == "Scream":
          continue
     if x == "Saw":
          break
     else:
          print(x)
