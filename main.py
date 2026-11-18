import os,json,urllib.request as r
V=(0,100,320,330,500,900,0)
T=('','@@@@''JJJJ''BBDF''AABE''@@@D''A?>@''ABB<''@@@@','68::''8<@@'':@BC'':ACD'':@CD'':ABC''8<@A''68::','<>>>''>@@@''>@AB''>AAB''>@BB''>BBB''>A@@''<>>>','@@@@''ABBB'+'?@@@'*5+'@@@A','@'*32,'@'*32)
J=(31,33,14,18,-31,-33,-14,-18)
W=(1,-1,16,-16)
B=(15,17,-15,-17)
D=W+B
Y=((),(),J,B,W,D,D)
b=[0]*128;w=1;e=-1;k=[4,116];u=[];n=0
class E(Exception):pass
def A(q,y):
 for o in (-15,-17) if y>0 else (15,17):
  x=q+o
  if not x&0x88 and b[x]==y:return 1
 for o in J+D:
  x=q+o
  if not x&0x88 and ((b[x]==2*y and o in J) or (b[x]==6*y and o in D)):return 1
 for o in D:
  x=q
  while 1:
   x+=o
   if x&0x88:break
   p=b[x]
   if p:
    if p==5*y or p==(4*y if o in W else 3*y):return 1
    break
 return 0
def G(g):
 m=[]
 for f,p in enumerate(b):
  if not p or p*w<=0 or f&0x88:continue
  d=abs(p)
  if d==1:
   s=16*w;v=7*(w>0);y=6-5*(w>0)
   for o in (s-1,s,s+1):
    x=f+o
    if x&0x88:continue
    q=b[x]
    if o==s:
     if q or (g and x>>4!=v):continue
    elif not(q*w<0 or x==e):continue
    if x>>4==v:
     for q in (5,2,4,3):m.append(f+(x<<7)+(q<<14))
    else:m.append(f+(x<<7))
   if not g and f>>4==y and not b[f+s] and not b[f+2*s]:m.append(f+((f+2*s)<<7))
  else:
   for o in Y[d]:
    x=f
    while 1:
     x+=o
     if x&0x88:break
     q=b[x]
     if q:
      if q*w<0:m.append(f+(x<<7))
      break
     if not g:m.append(f+(x<<7))
     if d==2 or d==6:break
   if d==6 and not g:
    for kf in (4,116):
     for o in (1,-1):
      kt=kf+2*o;rf=kf+3*o-(o<0)
      if f==kf and b[rf]==4*w and not b[kf+o] and not b[kt] and (o>0 or not b[kf+3*o]) and not(A(kf,-w)|A(kf+o,-w)|A(kt,-w)):m.append(kf+(kt<<7))
 return m
def L(x,y):
 b[y]=b[x];b[x]=0
def K(m):
 global w,e
 f=m&127;t=(m>>7)&127;r=m>>14
 p=b[f];q=b[t];x=0;oe=e
 b[f]=0
 if abs(p)==1 and t==e and not q:
  x=t-16*w;b[x]=0
 z=r*w if r else p
 b[t]=z
 if abs(p)==6:
  k[0 if w>0 else 1]=t
  if abs(t-f)==2:L(t+1 if t>f else t-2,t-1 if t>f else t+1)
 e=(f+t)//2 if abs(p)==1 and abs(t-f)==32 else -1
 u.append((m,q,x,oe))
 w=-w
def U():
 global w,e
 m,q,x,oe=u.pop()
 f=m&127;t=(m>>7)&127;r=m>>14
 p=b[t]
 w=-w
 if abs(p)==6:
  k[0 if w>0 else 1]=f
  if abs(t-f)==2:L(t-1 if t>f else t+1,t+1 if t>f else t-2)
 b[f]=p if not r else w
 b[t]=q
 if x:b[x]=-w
 e=oe
def v():
 s=0
 for i,p in enumerate(b):
  if p:
   q=abs(p);s+=(V[q]+(ord(T[q][(7-(i>>4) if p>0 else i>>4)*4+min(i&7,7-(i&7))])-64)*5)*p//q
 return s*w
def S(d,al,be,pl):
 global n
 n+=1
 if n>50000:raise E
 me=w;ck=A(k[0 if me>0 else 1],-me)
 if d<=0 and not ck:
  s=v()
  if s>=be:return be
  if s>al:al=s
 ms=G(0 if d>0 or ck else 1)
 ms.sort(key=lambda m:-(10*V[abs(b[(m>>7)&127])]-V[abs(b[m&127])] if b[(m>>7)&127] else 0))
 bf=-9**9;bm=0
 for m in ms:
  K(m)
  if A(k[0 if me>0 else 1],-me):U();continue
  y=-S(d-1,-be,-al,pl+1)
  U()
  if y>bf:bf=y;bm=m
  if y>al:al=y
  if al>=be:break
 if not bm:return -100000+pl if ck else (0 if d>0 else al)
 return bf
def F(f):
 global b,w,e,k
 b=[0]*128;w=1;e=-1;k=[4,116];u.clear()
 p=f.split()
 s=''.join(' '*int(ch) if ch.isdigit() else ch for ch in p[0] if ch!='/')
 for i,ch in enumerate(s):
  if ch==' ':continue
  v='PNBRQK'.index(ch.upper())+1
  q=(7-i//8)*16+i%8
  b[q]=v if ch.isupper() else -v
  if v==6:k[0 if ch.isupper() else 1]=q
 w=1 if p[1]=='w' else -1
 if p[3]!='-':e=(ord(p[3][0])-97)+(int(p[3][1])-1)*16
def I(m):
 f=m&127;t=(m>>7)&127;r=m>>14
 return chr(97+(f&7))+str((f>>4)+1)+chr(97+(t&7))+str((t>>4)+1)+('' if not r else 'xxnbrq'[r])
def Z(m,d):
 K(m);y=-S(d-1,-9**9,9**9,1);U();return y
def R(f,leg):
 global n
 F(f);n=0
 ls=set(leg);ms=[m for m in G(0) if I(m) in ls]
 if not ms:return leg[0]
 bm=ms[0]
 for d in range(1,10):
  try:vs=[Z(m,d) for m in ms]
  except E:break
  ms=[m for _,m in sorted(zip(vs,ms),reverse=True)];bm=ms[0]
 return I(bm)
def H(p,d):
 return json.load(r.urlopen(os.getenv('MAKEFUN_ENV_URL','')+p,json.dumps(d).encode()))
g=H('/game',{})
while g.get('status')!='done':
 while g.get('status')=='your_move':
  g=H('/move',{'game':g['game'],'move':R(g['fen'],g['legal_moves'])})
 g=H('/game',{})
