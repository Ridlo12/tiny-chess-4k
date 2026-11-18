import os,json,urllib.request as u
L=[0,100,320,330,500,900,0]
W=[0,0,4,8,14,24,40,0]
I=[0,0,0,10,15,10,5,0]
E=(-17,-16,-15,-1,1,15,16,17)
D=[0,0,(-33,-31,-18,-14,14,18,31,33),(-17,-15,15,17),(-16,-1,1,16),E,E]
b=[0]*128;H=[]
def C(v,i):
 a=abs(v);f=i&7;f=min(f,7-f);r=i>>4
 if a==1:q=r if v>0 else 7-r;t=W[q]+I[q]*(f==3)
 elif a==2:t=6*(f+min(r,7-r))-20
 else:t=0
 return(L[a]+t)*v//a
def F(f):
 global s,c,e,w,k,b,V
 b=[0]*128;V=0;i=112;p=f.split()
 for h in p[0]:
  if h=='/':i=(i//16-1)*16
  elif h.isdigit():i+=int(h)
  else:
   v='pnbrqk'.index(h.lower())+1
   if h.islower():v=-v
   b[i]=v;V+=C(v,i)
   if v==6:w=i
   elif v==-6:k=i
   i+=1
 s=1 if p[1]=='w' else-1;c=0
 for h in p[2]:c|={'K':1,'Q':2,'k':4,'q':8}.get(h,0)
 e=-1 if p[3]=='-' else(int(p[3][1])-1)*16+ord(p[3][0])-97
def T(i):return chr(97+(i&7))+str(i//16+1)
def Q(m):
 f=m&127;y=(m>>7)&127;p=(m>>14)&7
 return T(f)+T(y)+('nbrq'[p-2]if p else'')
def J(q,o,v,ds):
 for d in ds:
  y=q+d
  while not(y&136):
   x=b[y]
   if x:
    if x==v or(x==5*o and v!=2*o):return 1
    break
   if abs(v)in(2,6):break
   y+=d
 return 0
def K(q,o):
 for d in(15,17):
  y=q-d*o
  if not(y&136)and b[y]==o:return 1
 return J(q,o,2*o,D[2])or J(q,o,6*o,D[6])or J(q,o,3*o,D[3])or J(q,o,4*o,D[4])
def G():
 m=[]
 for i in range(128):
  if i&136:continue
  v=b[i]
  if v*s<=0:continue
  a=abs(v)
  if a==1:
   d=16*s
   for z in(d,d-1,d+1):
    y=i+z
    if y&136:continue
    if z==d:
     if b[y]:continue
    elif b[y]:
     if(b[y]>0)==(s>0):continue
    elif y!=e:continue
    if(y>>4)==7*(s>0):
     for p in(5,4,3,2):m.append(i|(y<<7)|(p<<14))
    else:
     m.append(i|(y<<7)|((z!=d)*(not b[y])<<17))
     if z==d and(i>>4)==1+5*(s<0)and not b[i+2*d]:m.append(i|((i+2*d)<<7))
  else:
   for z in D[a]:
    y=i+z
    while not(y&136):
     x=b[y]
     if not x or x*s<0:m.append(i|(y<<7))
     if x or a in(2,6):break
     y+=z
   if a==6:
    for t,d in((1,1),(2,-1))if s>0 else((4,1),(8,-1)):
     if c&t and not b[i+d]and not b[i+2*d]and(d>0 or not b[i-3])and b[i+3*d-(d<0)]==4*s and all(not K(i+j*d,-s)for j in(0,1,2)):m.append(i|((i+2*d)<<7))
 return m
def M(m):
 global s,c,e,w,k,V
 f=m&127;y=(m>>7)&127;p=(m>>14)&7;ep=m>>17&1
 v=b[f]
 if ep:q=y-16*s;cap=b[q];cq=q
 else:cap=b[y];cq=y
 nv=p*s if p else v
 rf=rt=-1
 if abs(v)==6:
  if y-f==2:rf,rt=f+3,f+1
  elif f-y==2:rf,rt=f-4,f-1
 H.append((f,y,v,cap,cq,rf,rt,c,e,w,k,V))
 V+=-C(v,f)+C(nv,y)
 if cap:V-=C(cap,cq)
 if rf>=0:
  rk=b[rf];V+=-C(rk,rf)+C(rk,rt);b[rt]=rk;b[rf]=0
 if ep:b[y]=v;b[q]=0;b[f]=0
 else:b[y]=nv;b[f]=0
 if abs(v)==6:
  if s>0:w=y
  else:k=y
  c&=~(3<<2*(s<0))
 for q,t in((0,2),(7,1),(112,8),(119,4)):
  if f==q or y==q:c&=~t
 e=f+16*s if v*v==1 and abs(y-f)==32 else-1
 s=-s
def U():
 global s,c,e,w,k,V
 f,y,v,cap,cq,rf,rt,c,e,w,k,V=H.pop()
 b[f]=v
 if cq==y:b[y]=cap
 else:b[y]=0;b[cq]=cap
 if rf>=0:b[rf]=b[rt];b[rt]=0
 s=-s
def O(m):
 y=(m>>7)&127;f=m&127
 return 10*L[abs(b[y])or(m>>17&1)]+(900 if(m>>14)&7 else 0)-L[abs(b[f])]//10
def S(d,A,B):
 global n,X
 n+=1
 if n>30e4:X=1;return 0
 if d<=0:
  x=V*s
  if x>=B:return B
  if x>A:A=x
  z=[m for m in G() if b[m>>7&127]or m>>14];e=0
 else:z=G();e=d-1
 z.sort(key=O,reverse=True);j=0
 for m in z:
  M(m)
  if K((w,k)[s>0],s):U();continue
  j+=1
  y=-S(e,-B,-A)
  U()
  if X:return 0
  if y>=B:return B
  if y>A:A=y
 if d>0 and j==0:return-99999 if K((w,k)[s<0],-s)else 0
 return A
def R(f,lg):
 global n,X
 F(f);lg=set(lg);n=0;X=0
 z=[m for m in G() if Q(m)in lg]
 if not z:return lg.pop()
 z.sort(key=O,reverse=True)
 b0=z[0];sc={}
 for d in range(1,10):
  a=-1e9;bb=None
  for m in z:
   M(m)
   if K((w,k)[s>0],s):U();continue
   y=-S(d-1,-1e9,-a)
   U()
   if X:break
   sc[m]=y
   if y>a:a=y;bb=m
  if X:break
  if bb:b0=bb
  z.sort(key=lambda m:-sc.get(m,-1e9))
 return Q(b0)
if __name__=='__main__':
 E=os.environ['MAKEFUN_ENV_URL']
 def P(a,d):
  return json.loads(u.urlopen(u.Request(E+a,data=json.dumps(d).encode())).read())
 while 1:
  g=P('/game',{})
  if g.get('status')=='done':break
  if g.get('status')=='your_move':P('/move',{'game':g['game'],'move':R(g['fen'],g['legal_moves'])})
