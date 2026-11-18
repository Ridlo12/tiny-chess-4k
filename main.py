import os,json,urllib.request as u
L=[0,100,320,330,500,900,0]
W=[0,0,4,8,14,24,40,0]
I=[0,0,0,10,15,10,5,0]
D=[0,0,(-33,-31,-18,-14,14,18,31,33),(-17,-15,15,17),(-16,-1,1,16),(-17,-16,-15,-1,1,15,16,17)]
D+=[D[5]]
Y={0:2,7:1,112:8,119:4}
b=[0]*128;s=1;c=0;e=-1;w=4;k=116;n=0;X=0;H=[]
def F(f):
 global s,c,e,w,k,b
 b=[0]*128;p=f.split()
 q=''.join(h*int(h)if h.isdigit()else h for h in p[0]if h!='/')
 for j,h in enumerate(q):
  if h.isdigit():continue
  i=(7-j//8)*16+j%8
  v='pnbrqk'.index(h.lower())+1
  if h.islower():v=-v
  b[i]=v
  if abs(v)==6:w,k=(i,k)if v>0 else(w,i)
 s=1 if p[1]=='w' else-1;c=sum(1<<'KQkq'.index(h)for h in p[2]if h in'KQkq')
 e=-1 if p[3]=='-'else(int(p[3][1])-1)*16+ord(p[3][0])-97
def Q(m):
 f=m&127;y=(m>>7)&127;p=(m>>14)&7
 return'%c%d%c%d%s'%(97+(f&7),(f>>4)+1,97+(y&7),(y>>4)+1,'nbrq'[p-2]if p else'')
def J(q,o,v,ds):
 return any(not((q+d)&136)and b[q+d]==v*o for d in ds)
def K(q,o):
 if J(q,o,1,(-15*o,-17*o))or J(q,o,2,D[2])or J(q,o,6,D[6]):return 1
 for d in D[6]:
  y=q+d
  while not(y&136):
   v=b[y]
   if v:
    if v==5*o or v==(3*o if d in D[3]else 4*o):return 1
    break
   y+=d
 return 0
def G():
 m=[]
 N=lambda f,y:[m.append(f|(y<<7)|(p<<14))for p in(5,4,3,2)]if(y>>4)==t else m.append(f|(y<<7))
 for i in range(128):
  if i&136:continue
  v=b[i]
  if not v or v*s<0:continue
  a=abs(v)
  if a==1:
   d=16*s;t=(0,7)[s>0];y=i+d
   if not(y&136)and not b[y]:
    N(i,y)
    if(i>>4)==(1,6)[s<0]and not b[i+2*d]:m.append(i|((i+2*d)<<7))
   for z in(d-1,d+1):
    y=i+z
    if y&136:continue
    if b[y]and b[y]*s<0:N(i,y)
    elif y==e:m.append(i|(y<<7)|(1<<17))
  elif a in(2,6):
   for z in D[a]:
    y=i+z
    if not(y&136)and(not b[y] or b[y]*s<0):m.append(i|(y<<7))
   if a==6:
    j=4 if s>0 else 116
    for d in(2,-2):
     h=(1 if d>0 else 2)*(1 if s>0 else 4);r=3 if d>0 else-4
     if c&h and i==j and b[j+r]==(4 if s>0 else-4) and not K(j,-s) and all(not b[j+x]for x in((1,2)if d>0 else(-1,-2,-3))) and not any(K(j+x,-s)for x in((1,2)if d>0 else(-1,-2))):m.append(j|((j+d)<<7))
  else:
   for z in D[a]:
    y=i+z
    while not(y&136):
     x=b[y]
     if not x:m.append(i|(y<<7));y+=z;continue
     if x*s<0:m.append(i|(y<<7))
     break
 return m
def M(m):
 global s,c,e,w,k
 H.append((list(b),s,c,e,w,k))
 f=m&127;y=(m>>7)&127;p=(m>>14)&7
 v=b[f]
 if m>>17&1:
  q=y-16*s;b[y]=v;b[q]=0;b[f]=0
 else:b[y]=p*s if p else v;b[f]=0
 if abs(v)==6:
  if s>0:w=y
  else:k=y
  if abs(y-f)==2:r=f+3 if y>f else f-4;b[(f+y)//2]=b[r];b[r]=0
  c&=~(3 if s>0 else 12)
 for q in(f,y):c&=~Y.get(q,0)
 e=(f+y)//2 if abs(v)==1 and abs(y-f)==32 else-1
 s=-s
def U():
 global s,c,e,w,k
 x=H.pop();b[:]=x[0];s=x[1];c=x[2];e=x[3];w=x[4];k=x[5]
def O(m):
 y=(m>>7)&127
 return 10*L[abs(b[y])or(m>>17&1)]+900*((m>>14)&7>0)
def S(d,A,B):
 global n,X
 n+=1
 if n>150000:X=1;return 0
 if d<=0:
  x=0
  for i in range(128):
   v=b[i]
   if i&136 or not v:continue
   a=abs(v);r=i>>4;f=min(i&7,7-(i&7))
   if v<0:r=7-r
   y=L[a]
   if a==1:y+=W[r]+(I[r]if f==3 else 0)
   elif a==2:y+=6*(f+min(r,7-r))-20
   x+=y if v>0 else-y
  x*=s
  if x>=B:return B
  if x>A:A=x
 z=[m for m in G() if d>0 or b[(m>>7)&127]or m>>14]
 z.sort(key=O,reverse=True);j=0
 for m in z:
  M(m)
  if K([k,w][s<0],s):U();continue
  j+=1
  y=-S(d-1,-B,-A)
  U()
  if X:return 0
  if y>=B:return B
  if y>A:A=y
 if d>0 and j==0:return-99999 if K([k,w][s>0],-s)else 0
 return A
def R(f,lg):
 global n,X
 F(f);lg=set(lg);n=0;X=0
 z=[m for m in G() if Q(m)in lg]
 z.sort(key=O,reverse=True)
 b0=z[0];sc={}
 for d in range(1,10):
  a=-10**9;bb=None
  for m in z:
   M(m)
   if K([k,w][s<0],s):U();continue
   y=-S(d-1,-10**9,-a)
   U()
   if X:break
   sc[m]=y
   if y>a:a=y;bb=m
  if X:break
  if bb:b0=bb
  z.sort(key=lambda m:-sc.get(m,-10**9))
 return Q(b0)
if __name__=='__main__':
 E=os.environ['MAKEFUN_ENV_URL']
 def P(a,d):
  q=u.Request(E+a,json.dumps(d).encode(),{'Content-Type':'application/json'})
  return json.loads(u.urlopen(q).read())
 while(g:=P('/game',{}))['status']!='done':
  if g['status']=='your_move':P('/move',{'game':g['game'],'move':R(g['fen'],g['legal_moves'])})
