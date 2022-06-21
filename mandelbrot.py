import bpy

class createMandel():
    def genMan(iter, reso, msize):
        # définir iteration_max = 50
        iter_max = iter

        mandel_res = reso
        size_m = msize
        vert_count = mandel_res ** 2

        # un plan avec Blender
        bpy.ops.mesh.primitive_grid_add(x_subdivisions = mandel_res, y_subdivisions = mandel_res, size = size_m)

        vert_coord = bpy.context.active_object.data
        # Pour chaque point de coordonnées (x; y) du plan :  
        for vert in range(0, vert_count):
            x = vert_coord.vertices[vert].co[0]
            y = vert_coord.vertices[vert].co[1]
            #  définir c = x + iy  
            c = complex(x, y)
            z = 0
            i = 0
            
            #  Tant que module de z < 2 et i < iteration_max 
            while abs(z) < 2 and i < iter_max:
                z = z*z + c
                i = i + 1
            
            # si i = iteration_max 
            # dessiner le pixel correspondant au point de coordonné (x; y)    
            if i == iter_max:
                vert_coord.vertices[vert].co[2] = 0.5
        

        print('done with mandelbrot')