import bpy

'''
#generating a 10*10 array
x = 2
y = 1

while y < 10:
    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(x, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, True, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
    y = y+1
'''

cubes = bpy.data.collections["cubes"].objects
offset =0


for x in cubes:
    x.scale = [0, 0, 0]
    x.keyframe_insert(data_path = 'scale', frame =1 + offset)
    x.scale = [1, 1, 5]
    x.keyframe_insert(data_path = 'scale', frame =50 + offset )    
    x.scale = [1, 1, .5]
    x.keyframe_insert(data_path = 'scale', frame =70 + offset)
    x.scale = [1, 1, 1]
    x.keyframe_insert(data_path = 'scale', frame =80 + offset)
    offset = offset +1