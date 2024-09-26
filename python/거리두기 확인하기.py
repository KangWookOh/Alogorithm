def check_distance (place):
    def valid(x,y):
        return 0 <= x < 5 and 0 <= y < 5
    def check_side(x,y):
        directions =[(1,0),(-1,0),(0,1),(0,-1)]
        for dx,dy in directions:
            nx,ny = x + dx, y + dy
            if valid(nx,ny) and place[nx][ny] == 'P':
                return False
        return True
    def check_diagonal(x,y):
        diagoanls =[(1,1),(1,-1),(-1,1),(-1,-1)]
        for dx,dy in diagoanls:
            nx,ny = x + dx , y + dy
            if valid(nx,ny) and place[nx][ny] == 'P':
                if place[x][ny] != 'X' or place[nx][y] !='X':
                    return False
        return True
    def check_twoPlace(x,y):
        twoPlace =[(2,0),(-2,0),(0,2),(0,-2)]
        for dx,dy in twoPlace:
            nx,ny = x + dx , y + dy
            if valid(nx,ny) and place[nx][ny] == 'P':
                mx,my = x + dx //2 , y + dy //2
                if place[mx][my] != 'X':
                    return False
        return True

    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                if not check_side(i,j) or not check_diagonal(i,j) or not check_twoPlace(i,j):
                    return 0
    return 1

def solution(places):
    return [check_distance(place) for place in places]






