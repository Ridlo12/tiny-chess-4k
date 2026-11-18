import os,json,urllib.request as u
L=[0,100,320,330,500,900,0]
W=[0,0,4,8,14,24,40]
I=[0,0,0,10,15,10,5]
b=[0]*128;H=[];T=[0]*64;Z=0
def F(f):
 global s,c,e,w,k,V,b
 V=0;b=[0]*128;a,d,j,l,_,_=f.split();i=112
 for h in a:
  if h=='/':i-=24
  elif h>'9':
   v='pnbrqk'.index(h.lower())+1
   if h>'Z':v=-v
   b[i]=v
   if v==6:w=i
   elif v==-6:k=i
   V+=C(v,i);i+=1
  else:i+=int(h)
 s=1-2*(d=='b');c=0
 for h in j:c|=1<<'KQkq'.find(h)if h>'-'else 0
 e=-1 if l=='-' else (int(l[1])-1)*16+ord(l[0])-97
def Q(m):
 f=m&127;y=m>>7&127;p=(m>>14)&7
 return f"{'abcdefgh'[f&7]}{f//16+1}{'abcdefgh'[y&7]}{y//16+1}{'nbrq'[p-2] if p else ''}"
def J(q,o):
 for z in(15,17):
  if not((y:=q-z*o)&136) and b[y]==o:return 1
 for d in N:
  y=q+d
  if not(y&136) and b[y]==2*o:return 1
 for d in K:
  y=q+d
  while not(y&136):
   v=b[y]
   if v:
    if v*o==6 and y==q+d or v*o==5 or v*o==(3 if d*d in(225,289) else 4):return 1
    break
   y+=d
 return 0
N=(-33,-31,-18,-14,14,18,31,33)
K=(-17,-16,-15,-1,1,15,16,17)
D=[N,(-17,-15,15,17),(-16,-1,1,16),K,K]
def G():
 m=[]
 for i,v in enumerate(b):
  if i&136:continue
  if not v or v*s<0:continue
  a=abs(v)
  if a==1:
   d=16*s;Y=[]
   y=i+d
   if not(y&136) and not b[y]:
    Y.append(y)
    if (i>>4)==1+5*(s<0) and not b[i+2*d]:Y.append(i+2*d)
   for z in(d-1,d+1):
    y=i+z
    if y&136:continue
    if b[y]*s<0:Y.append(y)
    elif y==e:Y.append(y+128)
   for y in Y:
    if y>127:m.append(i|((y&127)<<7)|(1<<17))
    elif (y>>4)==7*(s>0):
     for p in(5,4,3,2):m.append(i|(y<<7)|(p<<14))
    else:m.append(i|(y<<7))
  else:
   for z in D[a-2]:
    y=i+z
    if a in(2,6):
     if not(y&136) and b[y]*s<=0:m.append(i|(y<<7))
    else:
     while not(y&136) and not b[y]:m.append(i|(y<<7));y+=z
     if not(y&136) and b[y]*s<0:m.append(i|(y<<7))
   if a==6 and i==4+112*(s<0):
    for t in(1,-1):
     if c&1<<(s<0)*2+(t<0) and not b[i+t] and not b[i+2*t] and (t>0 or not b[i+3*t]) and b[i+3*t if t>0 else i-4]==4*s and all(not J(i+d,-s)for d in(0,t,2*t)):m.append(i|((i+2*t)<<7))
 return m
def C(v,i):
 a=abs(v);f=min(i&7,7-i&7);r=(i>>4)^7*(v<0)
 t=W[r]+I[r]*(f==3) if a==1 else 6*(f+min(r,7-r))-20 if a==2 else 0
 return (L[a]+t)*v//a
def M(m):
 global s,c,e,w,k,V
 f=m&127;y=m>>7&127;p=(m>>14)&7;v=b[f]
 cq=y-16*s if m>>17 else y;cap=b[cq]
 nv=p*s or v
 rf=rt=-1
 if abs(v)==6 and abs(y-f)==2:rf=f+3-7*(y<f);rt=f+1-2*(y<f)
 H.append((f,y,v,cap,cq,rf,rt,c,e,w,k,V))
 V+=-C(v,f)+C(nv,y)
 if cap:V-=C(cap,cq)
 if rf>=0:
  rk=b[rf];V+=-C(rk,rf)+C(rk,rt);b[rt]=rk;b[rf]=0
 if m>>17:b[y]=v;b[cq]=0;b[f]=0
 else:b[y]=nv;b[f]=0
 if abs(v)==6:w,k=(y,k)if s>0 else(w,y);c&=~(3<<2*(s<0))
 for q,z in((0,2),(7,1),(112,8),(119,4)):
  if q in(f,y):c&=~z
 e=f+16*s if v*v==1 and y-f==32*s else -1
 s=-s
def U():
 global s,c,e,w,k,V
 f,y,v,cap,cq,rf,rt,c,e,w,k,V=H.pop()
 b[f]=v;b[cq]=cap
 if cq!=y:b[y]=0
 if rf>=0:b[rf]=b[rt];b[rt]=0
 s=-s
def O(m):
 y=m>>7&127;f=m&127
 return 10*L[abs(b[y]) or m>>17]+900*((m>>14)&7>0)-L[abs(b[f])]//10+500*(m==Z)
def S(d,A,B,p):
 global n,X,Z
 n+=1
 if n>3e5:X=1;return 0
 if d<=0:
  x=V*s
  if x>=B:return B
  if x>A:A=x
  z=[m for m in G() if b[m>>7&127]or m>>14]
 else:z=G()
 Z=T[p];z.sort(key=O,reverse=True);j=0
 for m in z:
  M(m)
  if J(w if s<0 else k,s):U();continue
  j+=1
  y=-S(max(d-1,0),-B,-A,p+1)
  U()
  if X:return 0
  if y>=B:
   if d>0:T[p]=m
   return B
  if y>A:A=y
 if d>0 and j==0:return-99999+p if J(w if s>0 else k,-s) else 0
 return A
def R(f,lg):
 global n,X
 F(f);n=0;X=0
 z=[m for m in G() if Q(m) in lg]
 if not z:return lg[0]
 z.sort(key=O,reverse=True)
 b0=z[0];sc={}
 for d in range(1,10):
  a=-1e9;bb=0
  for m in z:
   M(m)
   if J(w if s<0 else k,s):U();continue
   y=-S(d-1,-1e9,-a,1)
   U()
   if X:break
   sc[m]=y
   if y>a:a=y;bb=m
  if X:break
  if bb:b0=bb
  z.sort(key=lambda m:-sc.get(m,-1e9))
 return Q(b0)
E=os.getenv('MAKEFUN_ENV_URL')
def P(a,d):
 return json.load(u.urlopen(E+a,json.dumps(d).encode()))
if E:
 while 1:
  g=P('/game',{});t=g['status']
  if t=='done':break
  if t!='your_move':continue
  P('/move',{'game':g['game'],'move':R(g['fen'],g['legal_moves'])})
