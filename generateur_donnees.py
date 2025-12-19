taille = 10

res_csv = ""

for x in range(-taille, taille + 1):
    for y in range(-taille, taille + 1):
        res_csv += f"{x}, {y}, {x**2 - y**2}\n"

with open("data.csv", mode="w") as f:
    f.write(res_csv)