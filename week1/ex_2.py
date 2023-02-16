anna, laura, oscar = list(map(int,input().split()))
jealous = []
if laura > anna and oscar > anna:
    jealous.append('Anna')
if anna > laura:
    jealous.append('Laura')
if laura > oscar or anna > oscar:
    jealous.append('Oscar')

if not jealous:
    jealous.append(None)

for name in sorted(jealous):
    print(name)
