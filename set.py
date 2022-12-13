star = {2,4,6,2,10,12, "yes","no", 2.4,233,0+1j}
star1 = set((2,4,6,2,10,12))
star1.add("12222")
star.add("12222")
star1.pop()
star.remove("yes")
star.discard("yes")
star.remove("yes")

print(star1)
print(star)


