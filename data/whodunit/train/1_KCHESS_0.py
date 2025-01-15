# KNIGHT CHESS
# Code : KCHESS

#  find next moves of king
def findNextKxKy(kx,ky):
	row_dir = [-1,-1,0,1,1,1,0,-1]
	col_dir = [0,1,1,1,0,-1,-1,-1]
	next_kx_ky = [(kx,ky)]
	for i in range(8):
		next_kx_ky.append(tuple([kx+row_dir[i],ky+col_dir[i]]))
	return next_kx_ky

# find next moves of all knight
def findNextKNPS(knps_arr):
	row_dir = [1,2,2,1,-1,-2,-2,-1]
	col_dir = [2,1,-1,-2,-2,-1,1,2]
	next_knps = set()
	for kn in knps_arr:
		for i in range(8):
			next_knps.add(tuple([kn[0]+row_dir[i],kn[1]+col_dir[i]]))
	return list(next_knps)


#  check if king has atleast one move to go ahead if not return true
def allKxKyInKnps(next_knps,next_kx_ky):
	for kxky in next_kx_ky:
		if not (kxky in next_knps):
			return False
	return True


t = int(input())
while t>0:
	knps = int(input())
	knps_arr = []
	for _ in range(knps):
		knps_arr.append(tuple(map(int,input().split())))
	kx,ky = map(int,input().split())

	next_knps = findNextKNPS(knps_arr)

	next_kx_ky = findNextKxKy(kx,ky)

	if(allKxKyInKnps(next_knps,next_kx_ky) == True):
		print("YES")
	else:
		print("NO")
	t-=1
