import bpy
active_obj = bpy.context.object

for obj in bpy.context.selected_objects:
    if obj != active_obj:
        # resolution U
        obj.data.resolution_u = active_obj.data.resolution_u 
        # added
        obj.data.extrude = active_obj.data.extrude
        obj.data.bevel_depth = active_obj.data.bevel_depth
        obj.data.render_resolution_u = active_obj.data.render_resolution_u
        obj.data.twist_mode = active_obj.data.twist_mode
        obj.data.bevel_resolution = active_obj.data.bevel_resolution
