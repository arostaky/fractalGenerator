# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Fractal Generator",
    "author" : "Patricio DI BACCO",
    "description" : "TP Final Algorithmique Artistique",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Object"
}

if "bpy" in locals():
    import importlib
    importlib.reload(fractal_op)
    importlib.reload(fractal_pnl)
import bpy
from . fractal_op import ADD_OT_fractal_one, ADD_OT_fractal_two, ADD_OT_fractal_three
from . fractal_pnl import FRACTAL_PT_Panel, ADD_MT_menu


classes = (ADD_OT_fractal_one, ADD_OT_fractal_two, ADD_OT_fractal_three, FRACTAL_PT_Panel, ADD_MT_menu )



def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
