extends MeshInstance

func _input(event):
	if event.is_action("R_LEFT"):
		self.rotate(Vector3(0,1,0),-PI/8)
		
	elif event.is_action("R_RIGHT"):
		self.rotate(Vector3(0,1,0),PI/8)
		
	else:
		pass
