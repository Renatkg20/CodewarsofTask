def duplicate_count(text):
  a = text.lower()
  l = []
  q = []
  for i in a:
    j = l.append(i)
  
  g = np.unique(l)
  if len(a) == len(g):
    print("0")
  elif len(a) > len(g):
    for w in g:
        h = a.count(w)
        if h > 1:
          u = q.append(h)

  return (len(q))
