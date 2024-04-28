from django.shortcuts import render,redirect
from anastruct import SystemElements
from .program import get_plot
# Create your views here.

#_________GUI Home Page__________

def home(request):
    return render(request,"Home.html")

def Results(request):
    if request.method=='POST':
        E = float(request.GET['E'])
        I = float(request.GET['I'])
        A = float(request.GET['A'])
        Elements = eval(request.GET['Elements'])
        FixedSupports = eval(request.GET['FixedSupports'])
        RollerSupports = eval(request.GET['RollerSupports'])
        PinnedSupports = eval(request.GET['PinnedSupports'])
        PointLoads = eval(request.GET['PointLoads'])
        udl = eval(request.GET['udl'])
        print(E,I,A,Elements)
        print("55"*1000)
        return redirect('Results')
    LoadDiagram = get_plot(DiagramType="LoadDiagram")
    ReactionsDiagram = get_plot(DiagramType="ReactionsDiagram")
    SFD = get_plot(DiagramType="SFD")
    BMD = get_plot(DiagramType="BMD")
    Displacement = get_plot(DiagramType="Displacement")
    return render(request,"Results.html",{'LoadDiagram':LoadDiagram,
                                       'ReactionsDiagram':ReactionsDiagram,
                                       'SFD':SFD,
                                       'BMD':BMD,
                                       'Displacement':Displacement})

def temp(request):
    LoadDiagram = get_plot(DiagramType="LoadDiagram")
    ReactionsDiagram = get_plot(DiagramType="ReactionsDiagram")
    SFD = get_plot(DiagramType="SFD")
    BMD = get_plot(DiagramType="BMD")
    Displacement = get_plot(DiagramType="Displacement")
    return render(request,"temp.html",{'LoadDiagram':LoadDiagram,
                                       'ReactionsDiagram':ReactionsDiagram,
                                       'SFD':SFD,
                                       'BMD':BMD,
                                       'Displacement':Displacement})