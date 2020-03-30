def tickets(people):
    cash = []
    for i in people:
      if i == 25 and sum(people) == 25:
        return "Yes"
        cash.append(i)
      elif i == 50 and sum(cash)>25:
          return "Yes"
          cash.append(i)
      elif i == 100 and sum(cash) < 75:
          return "Yes"
          cash.append(i)
      else:
        return "NO"


g = tickets([25, 100, 100, 25])
print(g)
