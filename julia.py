import bpy

#from bpy import context


class createJulia():
    def genJulia(res, precision):
        # resolution
        mandel_res = res
        vert_count = (mandel_res + 1) ** 2

        zoom = 0.1
        x_offset = 0
        y_offset = 0
        randomiser = 1

        # precision = 100
        scale = 1/zoom

        bpy.ops.mesh.primitive_grid_add(x_subdivisions = mandel_res + 1, y_subdivisions = mandel_res + 1, size = 0.5)

        vert_coord = bpy.context.active_object.data

        for vert in range(0, vert_count):
            x_loc = vert_coord.vertices[vert].co[0]
            y_loc = vert_coord.vertices[vert].co[1]
            
            x_final = (x_loc * scale) + x_offset
            y_final = (y_loc * scale) + y_offset
            
            z_loc = complex(x_final, y_final) ** 2 - randomiser
            
            count = 1
            
            while count < precision and 0 < abs(z_loc) < 2 :
                z_loc = z_loc ** 2 - randomiser
                count += 1
                
            z_final = (count ** 0.02) * 1
            
            vert_coord.vertices[vert].co[2] = z_final
            
    