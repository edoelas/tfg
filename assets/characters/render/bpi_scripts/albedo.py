import bpy
import math

character = bpy.data.objects["Character"]
plane = bpy.data.objects["Plane"]
axis = bpy.data.objects["Axis"]
path = "/home/edoelas/git/tfg/assets/characters/tests/action1_normal/"

for angle in range(0,1):
    bpy.context.view_layer.objects.active = axis
    bpy.context.object.rotation_euler[2] = 0.125*math.pi*angle
    
    character.select_set(True)
    bpy.context.view_layer.objects.active = plane

    for frame in range(0,120,5):
        bpy.context.scene.frame_set(frame)
        print(frame)

        bpy.ops.object.bake(type='NORMAL',normal_space='OBJECT', use_selected_to_active=True,margin = 0)

        img = bpy.data.images['normal_map']
        name = path + str(frame) + '_' + str(angle) + '.png'
        print(name)
        img.save_render(name)


 