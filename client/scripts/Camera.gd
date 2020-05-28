extends Camera

func _input(event):
	if event.is_action("ZOOM_OUT"):
		self.size += 1
		
	elif event.is_action("ZOOM_IN"):
		self.size -= 1
		
	else:
		pass
