from Vector3DClass import Vec3d
A = Vec3d(-6, 2, 2)
B = Vec3d(7, 5, 10)
plasma_speed = 100. # meters per second
AB = B-A
print("Vector to droid is", AB)
distance_to_target = AB.get_length()
print("Distance to droid is", distance_to_target, "meters")
plasma_heading = AB.normalized()
print("Heading is", plasma_heading)