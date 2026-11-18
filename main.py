import json,os,urllib.request
I=10**9;M=10**6;B=150000;ND=0
V=[0,100,320,330,500,900,0]
S=['','@@@@ABB<A?>@@@@DAABEBBDFJJJJ@@@@','68::8<@A:ABC:@CD:ACD:@BC8<@@68::','<>>>>A@@>BBB>@BB>AAB>@AB>@@@<>>>','@'*32,'@'*32,'@'*32]
T=[[(ord(c)-64)*5 for c in s] for s in S]
KN=[33,31,18,14,-14,-18,-31,-33]
KI=[16,-16,1,-1,17,15,-17,-15]
DR=[KN,[17,15,-17,-15],[16,-16,1,-1],KI,KI]
SQ=[r*16+f for r in range(8) for f in range(8)]
KS=[4,116]
class E(Exception):pass
def at(b,q,y):
 u=y<<3
 for o in(-15,-17)if y==0 else(15,17):
  t=q+o
  if not(t&136)and b[t]==(1 if y==0 else 9):return 1
 for z,v in((KN,2),(KI,6)):
  for o in z:
   t=q+o
   if not(t&136)and b[t]==v|u:return 1
 for o in KI:
  t=q+o
  while not(t&136):
   p=b[t]
   if p:
    if(p&8)==u and((p&7)==5 or(p&7)==(3 if abs(o)>14 else 4)):return 1
    break
   t+=o
 return 0
def gn(b,s,c):
 m=[];u=s<<3
 for q in SQ:
  p=b[q]
  if p==0 or(p&8)!=u:continue
  t=p&7
  if t==1:
   d=16-32*s;l=7-7*s;w=q+d
   if not(w&136)and b[w]==0:
    if(w>>4)==l:
     for r in(5,4,3,2):m.append(q|(w<<7)|(r<<14))
    else:
     m.append(q|(w<<7))
     if not c and(q>>4)==1+5*s and b[w+d]==0:m.append(q|((w+d)<<7))
   for w in(q+d-1,q+d+1):
    if w&136:continue
    if b[w]!=0 and(b[w]&8)!=u:
     if(w>>4)==l:
      for r in(5,4,3,2):m.append(q|(w<<7)|(r<<14))
     else:m.append(q|(w<<7))
  else:
   z=DR[t-2];v=2<t<6
   for o in z:
    w=q+o
    while not(w&136):
     x=b[w]
     if x:
      if(x&8)!=u:m.append(q|(w<<7))
      break
     if not c:m.append(q|(w<<7))
     if not v:break
     w+=o
   if t==6 and not c and q==4+112*s and not at(b,q,1-s):
    r=4+8*s
    if b[q+3]==r and not b[q+1]and not b[q+2]and not at(b,q+1,1-s)and not at(b,q+2,1-s):m.append(q|((q+2)<<7))
    if b[q-4]==r and not b[q-1]and not b[q-2]and not b[q-3]and not at(b,q-1,1-s)and not at(b,q-2,1-s):m.append(q|((q-2)<<7))
 return m
def mk(b,m,s):
 f=m&127;t=m>>7&127;p=m>>14&7;pc=b[f]
 b[t]=(p|(s<<3))if p else pc;b[f]=0
 if(pc&7)==6 and abs(t-f)==2:
  if t>f:b[f+1]=b[f+3];b[f+3]=0
  else:b[f-1]=b[f-4];b[f-4]=0
 if(pc&7)==6:KS[s]=t
def ev(b,s):
 x=0
 for q in SQ:
  p=b[q]
  if p:
   t=p&7;r=q>>4;f=q&7;w=min(f,7-f)
   x+=(-1 if p&8 else 1)*(V[t]+T[t][(7-r if p&8 else r)*4+w])
 return x if s==0 else -x
def od(m,b):
 m.sort(key=lambda z:(10*V[b[z>>7&127]&7]-V[b[z&127]&7])if b[z>>7&127] else 0,reverse=True)
 return m
def S(b,D,A,L,s,y):
 global ND;ND+=1
 if ND>B:raise E
 Q=D<=0
 if Q:
  z=ev(b,s)
  if z>=L:return L
  if z>A:A=z
 c=at(b,KS[s],1-s)if Q else 0
 k=0 if c or not Q else 1
 m=od(gn(b,s,k),b);bs=-I
 for x in m:
  o=b[:];k2=KS[:];mk(b,x,s)
  if at(b,KS[s],1-s):b[:]=o;KS[:]=k2;continue
  w2=-S(b,D-1,-L,-A,1-s,y+1)
  if w2>bs:bs=w2
  if w2>A:A=w2
  b[:]=o;KS[:]=k2
  if A>=L:break
 if bs==-I:
  if at(b,KS[s],1-s):return -M+y
  return A if Q else 0
 return A if Q else bs
def rt(b,s,lg):
 global ND
 ls=set(lg);m=[x for x in gn(b,s,0)if uc(x)in ls]
 if len(m)<2:return m[0]if m else None
 ND=0;bs=None
 for D in range(1,10):
  try:
   A=-I;L=I;w2=-I;bm=None
   for x in od(m,b):
    o=b[:];k=KS[:];mk(b,x,s)
    if at(b,KS[s],1-s):b[:]=o;KS[:]=k;continue
    z=-S(b,D-1,-L,-A,1-s,1);b[:]=o;KS[:]=k
    if z>w2:w2=z;bm=x
    if z>A:A=z
   if bm is not None:bs=bm
  except E:break
 return bs
def uc(m):
 f=m&127;t=m>>7&127;p=m>>14&7
 return'%c%d%c%d'%(97+f%8,f//16+1,97+t%8,t//16+1)+('nbrq'[p-2]if p else'')
def pf(a):
 z=a.split();b=[0]*128;q=112
 for ch in z[0]:
  if ch=='/':q-=24
  elif ch.isdigit():q+=int(ch)
  else:
   c='PNBRQK'.find(ch.upper())+1
   if ch.islower():c+=8
   b[q]=c
   if c&7==6:KS[c>>3]=q
   q+=1
 return b,0 if z[1]=='w' else 1
def pt(u,o):
 r=urllib.request.urlopen(u,json.dumps(o).encode());return json.loads(r.read())
def main():
 u=os.environ['MAKEFUN_ENV_URL']
 while 1:
  try:g=pt(u+'/game',{})
  except:break
  if g.get('status')=='done':break
  if g.get('status')!='your_move':continue
  b,s=pf(g['fen']);lg=g.get('legal_moves',[]);mv=rt(b,s,lg);w=mv and uc(mv)
  if w not in lg:
   if not lg:break
   w=lg[0]
  try:pt(u+'/move',{'game':g['game'],'move':w})
  except:pass
main()
