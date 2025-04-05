file=open(

R,C=#row and columns
m=
sr,sc=
rq,cq=

move_count=0
nodes_ledt_in_layer=1
nodes_in_next_layer=0

reached_end =false

visited=
dr=[-1,+1,0,0]
dc=[0,0,+1,-1]
def solve():
    rq.enque(sr)
    cq.enque(sc)
    visited[sr][sc]=True
    while rq.size>0:
        r=rq.dequeue
        c=cq.dequeue
        if n[r][c]=='E':
            reached_end=True
            break
            explore_neighbours(r,c)
            nodes_left_in_laye--
            if nodes_left_in_layer==0:
                noded_left_in_layer==0:
                noded_left_in_layer=nodes_in_next_layer
                noded_in_next_layer=0
                move_count++
        if reached_end:
            return move_count
        return -1
def explore_neighbours(r,c):
    for(i in range[0,4]):
        rr=r+dr[i]
        cc=c+dc[i]
    #skip out bounds position
if rr<0 or cc<0:
    continue
if rr>=R or cc>=C:
    continue
    #skip the visited cells or vlovked cells
if visited[rr][[cc]:
    continue
if m[rr][cc] =='#':
    continue
rq.enqueue(rr)
cq.enqueue(cc)
visited[rr][cc]= True
nodes_in_next_layer++
    
