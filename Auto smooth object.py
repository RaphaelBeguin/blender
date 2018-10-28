import bpy
bpy.context.object.data.use_auto_smooth = True
bpy.ops.object.shade_smooth()
bpy.ops.object.subdivision_set(level=2)
