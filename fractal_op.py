import bpy
from bpy.types import Operator
from . mandelbrot import createMandel
from . julia import createJulia
from . menger import createMenger


class ADD_OT_fractal_one(bpy.types.Operator):
    bl_idname = "add.mandelbrot"
    bl_label = "Mandelbrot Generator"

    my_int: bpy.props.IntProperty(name="Number of iteractions",min= 5,max=50, default=5)
    my_intB: bpy.props.IntProperty(name="Resolution",min= 10,max=1000, default=1000)
    my_intC: bpy.props.IntProperty(name="Size",min=2,max=6, default=5)
    # my_bool: bpy.props.BoolProperty(name="Animate")
    # my_string: bpy.props.StringProperty(name="String Value")

    def execute(self, context):
        message = (
            "Popup Values: %f" %
            (self.my_int)
        )
        self.report({'INFO'}, message)
        createMandel.genMan(self.my_int, self.my_intB, self.my_intC)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

class ADD_OT_fractal_two(bpy.types.Operator):
    bl_idname = "add.julia"
    bl_label = "Julia Generator"

    my_int: bpy.props.IntProperty(name="Number of iteractions",min= 1,max=200, default=1)
    my_intB: bpy.props.IntProperty(name="Precision",min= 10,max=1000, default=500)
    # my_bool: bpy.props.BoolProperty(name="Toggle Option")
    # my_string: bpy.props.StringProperty(name="String Value")

    def execute(self, context):
        message = (
            "Popup Values: %f" %
            (self.my_int)
        )
        self.report({'INFO'}, message)
        createJulia.genJulia(self.my_int, self.my_intB)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

class ADD_OT_fractal_three(bpy.types.Operator):
    bl_idname = "add.menger"
    bl_label = "Menger Sponge Generator"

    my_int: bpy.props.IntProperty(name="Level",min= 1,max=10, default=4)
    my_floatB: bpy.props.FloatProperty(name="Width",min= 0.1,max=4.0, default=2.1)
    # my_bool: bpy.props.BoolProperty(name="Toggle Option")
    # my_string: bpy.props.StringProperty(name="String Value")

    def execute(self, context):
        message = (
            "Popup Values: %f" %
            (self.my_int)
        )
        self.report({'INFO'}, message)
        createMenger.genMenger(self.my_int, self.my_floatB)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)