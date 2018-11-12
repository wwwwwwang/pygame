CUBE_SIZE = 10
for x in range(0, CUBE_SIZE+1, 5):
		edge_x = x == 0 or x == CUBE_SIZE
		
		for y in range(0, CUBE_SIZE+1, 5):
			edge_y = y == 0 or y == CUBE_SIZE
				
			for z in range(0, CUBE_SIZE+1, 5):
				edge_z = z == 0 or z == CUBE_SIZE
				print("x=%d,y=%d,z=%d,ex=%d,ey=%d,ez=%d"%(x,y,z,edge_x,edge_y,edge_z))