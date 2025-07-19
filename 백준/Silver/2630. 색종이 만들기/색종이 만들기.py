n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
cnt_blue = 0 
cnt_white = 0
def cut_paper(length,x,y):
    global cnt_white
    global cnt_blue
    #나눠서 바로 해결할 수 있는 문제가 되었음 
    if length == 1:
        if paper[x][y] == 1 :
            cnt_blue += 1
        else :
            cnt_white += 1
        return

    for i in range(x,x+length):
        for j in range(y,y+length):
            if paper[i][j] != paper[x][y] :
                cut_paper(length//2,x,y)
                cut_paper(length//2,x+length//2,y)
                cut_paper(length//2,x,y+length//2)
                cut_paper(length//2,x+length//2,y+length//2)
                return
                
    
    if paper[x][y] == 1:
        cnt_blue += 1
        
    else:
        cnt_white += 1
    return
   

cut_paper(n,0,0)
print(cnt_white)
print(cnt_blue)

    