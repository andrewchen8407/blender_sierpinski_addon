bl_info = {
    "name": "Sierpinski Tetrahedron Generator",
    "author": "Andrew Chen",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Mesh > Sierpinski Tetrahedron",
    "description": "Generates a Sierpinski Tetrahedron fractal",
    "category": "Add Mesh",
}

import bpy
from bpy.types import Operator
from bpy.props import IntProperty
import bmesh
from mathutils import Vector

def create_tetrahedron(bm, v1, v2, v3, v4):
    """Create a single tetrahedron in the BMesh."""
    verts = [bm.verts.new(v1), bm.verts.new(v2), bm.verts.new(v3), bm.verts.new(v4)]
    faces = [
        (verts[0], verts[1], verts[2]),
        (verts[0], verts[1], verts[3]),
        (verts[0], verts[2], verts[3]),
        (verts[1], verts[2], verts[3]),
    ]
    for face in faces:
        bm.faces.new(face)

def sierpinski_tetrahedron(bm, v1, v2, v3, v4, level):
    """Recursively generate a Sierpinski Tetrahedron."""
    if level == 0:
        create_tetrahedron(bm, v1, v2, v3, v4)
    else:
        # Calculate midpoints of edges
        m12 = (v1 + v2) / 2
        m13 = (v1 + v3) / 2
        m14 = (v1 + v4) / 2
        m23 = (v2 + v3) / 2
        m24 = (v2 + v4) / 2
        m34 = (v3 + v4) / 2
        
        # Recursively subdivide into four smaller tetrahedrons
        sierpinski_tetrahedron(bm, v1, m12, m13, m14, level - 1)
        sierpinski_tetrahedron(bm, m12, v2, m23, m24, level - 1)
        sierpinski_tetrahedron(bm, m13, m23, v3, m34, level - 1)
        sierpinski_tetrahedron(bm, m14, m24, m34, v4, level - 1)

class SierpinskiTetrahedronOperator(Operator):
    """Operator to generate a Sierpinski Tetrahedron."""
    bl_idname = "mesh.add_sierpinski_tetrahedron"
    bl_label = "Add Sierpinski Tetrahedron"
    bl_options = {'REGISTER', 'UNDO'}

    level: IntProperty(
        name="Level",
        description="Recursion level for the fractal",
        default=2,
        min=0,
        max=5
    )

    def execute(self, context):
        # Create a new mesh and object
        mesh = bpy.data.meshes.new("SierpinskiTetrahedron")
        obj = bpy.data.objects.new("SierpinskiTetrahedron", mesh)
        bpy.context.collection.objects.link(obj)

        # Initialize BMesh
        bm = bmesh.new()

        # Define initial tetrahedron vertices (unit size, centered)
        v1 = Vector((0.0, 0.0, 1.0))
        v2 = Vector((0.9428, 0.0, -0.3333))
        v3 = Vector((-0.4714, 0.8165, -0.3333))
        v4 = Vector((-0.4714, -0.8165, -0.3333))

        # Generate the fractal
        sierpinski_tetrahedron(bm, v1, v2, v3, v4, self.level)

        # Transfer BMesh data to the mesh and clean up
        bm.to_mesh(mesh)
        bm.free()

        return {'FINISHED'}

def menu_func(self, context):
    """Add the operator to the Add > Mesh menu."""
    self.layout.operator(SierpinskiTetrahedronOperator.bl_idname, icon='MESH_CUBE')

def register():
    """Register the operator and menu item."""
    bpy.utils.register_class(SierpinskiTetrahedronOperator)
    bpy.types.VIEW3D_MT_add.append(menu_func)

def unregister():
    """Unregister the operator and menu item."""
    bpy.utils.unregister_class(SierpinskiTetrahedronOperator)
    bpy.types.VIEW3D_MT_add.remove(menu_func)

if __name__ == "__main__":
    register()
