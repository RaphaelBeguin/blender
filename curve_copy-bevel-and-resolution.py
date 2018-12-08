import bpy
active_obj = bpy.context.object

for obj in bpy.context.selected_objects:
    if obj != active_obj:
        # resolution U
        obj.data.resolution_u = active_obj.data.resolution_u 
        # We could also access other proerties like bevel
        obj.data.bevel_depth = active_obj.data.bevel_depth
