# practice list
scores = [90, 70, 60, 50, 80]
print(scores)
things = [90, "yes", True]
print(things)
print(things[0])
print(things[1])
print(things[2])
print(things[-1])
print(things[-2])
print(scores[1:3])
print(scores[:3])
scores[0] = 30
print(scores[:3])
print(scores[2:])

scores.extend(things)
print(scores)
scores.append("nono")
print(scores)
scores.insert(2, -100)
print(scores)
scores.remove(-100)
print(scores)
#scores.clear()
#print(scores)
scores.pop()
print(scores)
#scores.sort()
#print(scores)
tmp = [12, 15, 13]
tmp.sort()
print(tmp)
print(tmp.index(15))
#print(tmp.index(-1))
tmp.append(15)
print(tmp)
print(tmp.index(15))
print(tmp.count(15))



