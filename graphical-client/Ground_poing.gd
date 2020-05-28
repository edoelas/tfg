extends Position3D


func _input(event):
	if event.is_action("LEFT"):
		self.translation -= Vector3(0.1,0,0)
		
	elif event.is_action("RIGHT"):
		self.translation += Vector3(0.1,0,0)
		
	elif event.is_action("UP"):
		self.translation -= Vector3(0,0,0.1)
		
	elif event.is_action("DOWN"):
		self.translation += Vector3(0,0,0.1)
		
	elif event.is_action("R_LEFT"):
		self.rotate(Vector3(0,1,0),-PI/8)
		
	elif event.is_action("R_RIGHT"):
		self.rotate(Vector3(0,1,0),PI/8)
		
	else:
		pass
