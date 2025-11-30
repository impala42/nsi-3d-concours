taille = 10

res = [[] for i in range(taille*2)]
res_csv = ""

for x in range(-taille, taille):
    for y in range(-taille, taille):
        res_csv += f"{x}, {y}, {x**2 + y**2}\n"




f = open("data.csv", mode="w")
f.write(res_csv)