bl_addon_info = {
    'name' : 'Count them polys',
    'author' : 'Nathan Letwory (jesterKing)',
    'version' : '0.1',
    'blender' : (2,5,3),
    'location' : 'View3D > Specials > Count',
    'description' : 'Count how many triangles and quads are in a mesh',
    'category' : 'Mesh'
}

import bpy

class jesterKing_CountTrisQuads(bpy.types.Operator):
    '''Count triangles and quads'''
    bl_idname = 'mesh.count'
    bl_label = 'Count'
    bl_options = {'REGISTER'}
    
    def poll(self, context):
        o = context.active_object
        return (o and o.type == 'MESH')
    
    def execute(self, context):
        t = 0
        q = 0
        o = context.active_object
        if o.selected and o.type=='MESH':
            m = o.data
            for f in m.faces:
                if len(f.verts)==3:
                    t = t + 1
                else:
                    q = q + 1
        
        self.report({'INFO'}, 'I counted in the active mesh: ' + str(t) + ' triangles and ' + str(q) + ' quads')
        
        return {'FINISHED'}

menu_func = (lambda self, context: self.layout.operator(jesterKing_CountTrisQuads.bl_idname, text='Count'))

def register():
    bpy.types.register(jesterKing_CountTrisQuads)
    bpy.types.VIEW3D_MT_edit_mesh_specials.append(menu_func)
    bpy.types.VIEW3D_MT_edit_mesh_vertices.append(menu_func)

def unregister():
    bpy.types.unregister(jesterKing_CountTrisQuads)
    bpy.types.VIEW3D_MT_edit_mesh_specials.remove(menu_func)
    bpy.types.VIEW3D_MT_edit_mesh_vertices.remove(menu_func)

if __name__ == "__main__":
    register()

