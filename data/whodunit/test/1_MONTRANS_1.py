for _ in range(int(input())):
  a, b, c = map(int, input().split())
  i, m_index, m_money = 0, 0, a*100+b
  p_money={m_money}
  while a*100+b>c:
    i += 1
    if c > b:
      a -= 1
      b += 100
    b -= c
    a,b = b,a
    if a*100+b in p_money:
      break
    p_money.add(a*100+b)
    if a*100+b > m_money:
      m_index=i
      m_money=a*100+b
  print(m_index)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  