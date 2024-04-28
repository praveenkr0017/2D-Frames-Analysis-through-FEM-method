# Code to incorporate the matplotlib/anastrut figures in django

import matplotlib.pyplot as plt
import base64
from io import BytesIO
from anastruct import SystemElements 

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(DiagramType:str):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))

    ss = SystemElements(EA=15000, EI=5000)

    # Add beams to the system.
    ss.add_element(location=[0, 5])
    ss.add_element(location=[[0, 5], [5, 5]])
    ss.add_element(location=[[5, 5], [5, 0]])

    # Add a fixed support at node 1.
    ss.add_support_fixed(node_id=1)

    # Add a rotational spring support at node 4.
    ss.add_support_spring(node_id=4, translation=3, k=4000)

    # Add loads.
    ss.point_load(Fx=30, node_id=2)
    ss.q_load(q=-10, element_id=2)

    # Solve
    ss.solve()

    # Get visual results.
    if DiagramType == "LoadDiagram":
        ss.show_structure(show=False)
        plt.title("Loading Diagram")
    elif DiagramType == "ReactionsDiagram":        
        Reactions = ss.show_reaction_force(show=False)
        plt.title("Reactions Diagram")
    elif DiagramType == "SFD":
        SFD = ss.show_shear_force(show=False)
        plt.title("Shear Force Diagram")
    elif DiagramType == "BMD":
        BMD = ss.show_bending_moment(show=False)
        plt.title("Bending Moment Diagram")
    elif DiagramType == "Displacement":
        Displacement_Diagram = ss.show_displacement(show=False)
        plt.title("Displacement")

    #Diagrams = [Loading_Diagram,Reactions,SFD,BMD,Displacement_Diagram]

    plt.tight_layout()
    graph = get_graph()
    return graph
