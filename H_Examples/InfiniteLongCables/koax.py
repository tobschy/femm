# Phase3.py

import femm
import matplotlib.pyplot as plt
import numpy as np

femm.openfemm()
femm.newdocument(0)

# define some parameters.  These can then
# be used to draw the geometry parametrically
r = 1 / 2
R = 2
h = 1 / 0.0254

# define some materials
femm.mi_addmaterial("Air")
femm.mi_addmaterial("Cu", 1, 1, 0, 0, 58)

# draw geometry of interest
femm.mi_drawarc(
    (-r),
    0,
    (r),
    0,
    180,
    1,
)
femm.mi_drawarc(
    (r),
    0,
    (-r),
    0,
    180,
    1,
)
femm.mi_addcircprop("i0", 1, 1)
femm.mi_addblocklabel(0, 0)
femm.mi_selectlabel(0, 0)
femm.mi_setblockprop("Cu", 1, 0, "i0", 0, 0, 1)
femm.mi_clearselected()

femm.mi_drawarc(
    (-R + r),
    0,
    (R - r),
    0,
    180,
    1,
)
femm.mi_drawarc(
    (R - r),
    0,
    (-R + r),
    0,
    180,
    1,
)

femm.mi_drawarc(
    (-R - r),
    0,
    (R + r),
    0,
    180,
    1,
)
femm.mi_drawarc(
    (R + r),
    0,
    (-R - r),
    0,
    180,
    1,
)
femm.mi_addcircprop("i1", -1, 1)
femm.mi_addblocklabel(-R, 0)
femm.mi_selectlabel(-R, 0)
femm.mi_setblockprop("Cu", 1, 0, "i1", 0, 0, 1)
femm.mi_clearselected()

femm.mi_addblocklabel(R + r + 1, 0)
femm.mi_selectlabel(R + r + 1, 0)
femm.mi_setblockprop("Air", 1, 0, "<None>", 0, 0, 1)
femm.mi_clearselected()

femm.mi_addblocklabel(R / 2, 0)
femm.mi_selectlabel(R / 2, 0)
femm.mi_setblockprop("Air", 1, 0, "<None>", 0, 0, 1)
femm.mi_clearselected()

# draw boundary
femm.mi_makeABC(3, 10 * R, 0, 0, 0)

# Save, analyze, and view results
femm.mi_probdef(60, "inches", "planar", 1e-8, h, 30)
femm.mi_saveas("Phase3.fem")
femm.mi_analyze()
femm.mi_loadsolution()
femm.mi_zoomin()

femm.mo_showdensityplot(1, 0, 5e-7, 8e-6, "bmag")
femm.mo_zoom(-2 * (R + r + 1), -(R + r + 1), 2 * (R + r + 1), (R + r) + 1)

# plot H values at x axis between the wires
x = np.multiply((R + r + 1) / 1000, np.array(range(1000)))
Hx = []
for xval in x:
    [a, b] = femm.mo_geth(xval, 0)
    Hx.append((abs(a) ** 2 + abs(b) ** 2) ** 0.5)
plt.plot(x, Hx)
plt.xlabel("x")
plt.ylabel("|H(x)|")
plt.grid()
plt.show()

femm.closefemm()
