import bpy
from bpy.types import Panel, Menu

class ADD_MT_menu(bpy.types.Menu):
	bl_label = "Select Menu"
	bl_idname = "ADD_MT_menu"


	def draw(self, context):
		layout = self.layout
		layout.operator("add.mandelbrot")
		layout.operator("add.julia")
		layout.operator("add.menger")

class FRACTAL_PT_Panel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Fractal Generator"
    bl_category = "Fractal Generator"

    def draw(self, context):
            layout = self.layout
            row = layout.row()
            row.label(text="Fractal Selection: ")
            row = layout.row()
            row.menu("ADD_MT_menu")
            # row = layout.row()
            # row.operator("add.run_script", icon="SNAP_GRID")
