import re
t7 = open('gp7_djvu.txt', encoding='utf-8', errors='replace').read()
t4 = open('gp4_djvu.txt', encoding='utf-8', errors='replace').read()

def w(t,a,b): return re.sub(r'\n\s*\n+','\n', t[a:b])

print('===== DE SYNTHESI OPENING gp7 757300-762800')
print(w(t7,757300,762800)[:5600])
print()
print('===== GP4 DISCOURS REGION 1118500-1123500')
print(w(t4,1118500,1123500)[:4200])
