import bpy

class createMenger():
    def genMenger(level, step_w):
        # level = 4 
        width = 3**level
        step = step_w / width
        px = -1.0
        py = -1.0
        pz = 0
        mesh = bpy.data.meshes.new(name="Menger")
        coords = []
        faces = []
        idx = 0;
        for x in range(0,width):
            py = -1.0
            for y in range(0,width):
                pz = 0.0
                for z in range(0,width):
                    t = True
                    w = width / 3
                    while ( w >= 1  ):
                        tx = ((int( x/w ) % 3 )!= 1)
                        ty = ((int( y/w ) % 3 )!= 1)
                        tz = ((int( z/w ) % 3 )!= 1)
                        t = t and ((tx and ty ) or (tx and tz) or (ty and tz ))
                        w  = w/3
                    if t == True:
                        coords.append(( px, py, pz ))
                        coords.append(( px + step, py, pz ))
                        coords.append(( px + step, py + step, pz ))
                        coords.append(( px, py+step , pz ))
                        coords.append(( px, py, pz + step))
                        coords.append(( px + step, py, pz + step ))
                        coords.append(( px + step, py + step, pz + step ))
                        coords.append(( px, py+step , pz + step ))
                        faces.append(( idx, idx+1, idx+2, idx+3 ))
                        faces.append(( idx, idx+1, idx+5, idx+4 ))
                        faces.append(( idx+1, idx+2, idx+6, idx+5 ))
                        faces.append(( idx+2, idx+3, idx+7, idx+6 ))
                        faces.append(( idx+3, idx+0, idx+4, idx+7 ))
                        faces.append(( idx+4, idx+5, idx+6, idx+7 ))

                        idx += 8
                    pz+=step
                py+=step
            px+=step
        object = bpy.data.objects.new( 'MESH', mesh )
        bpy.context.collection.objects.link(object)
        #removed old method:
        # bpy.context.scene.objects.link( object )

        mesh.from_pydata( coords, [], faces )
        mesh.update( calc_edges=True )