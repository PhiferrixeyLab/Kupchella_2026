#Midsagittal Plane Visualization

import numpy as np
import slicer
import vtk

msp_node = slicer.util.getNode('MSP')  
msp_points = np.array([msp_node.GetNthControlPointPosition(i) for i in range(msp_node.GetNumberOfControlPoints())])  

mean_msp = np.mean(msp_points, axis=0)  
cov_matrix = np.cov(msp_points.T)  
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)  
plane_normal = eigenvectors[:, np.argmin(eigenvalues)]  
plane_normal /= np.linalg.norm(plane_normal)  

plane_size = 50  

plane_center = mean_msp  
plane_axis1 = np.cross(plane_normal, [1, 0, 0])  
if np.linalg.norm(plane_axis1) < 1e-6:  
    plane_axis1 = np.cross(plane_normal, [0, 1, 0])  
plane_axis1 /= np.linalg.norm(plane_axis1)  
plane_axis2 = np.cross(plane_normal, plane_axis1)  

p1 = plane_center + plane_size * (plane_axis1 + plane_axis2)  
p2 = plane_center + plane_size * (plane_axis1 - plane_axis2)  
p3 = plane_center - plane_size * (plane_axis1 + plane_axis2)  
p4 = plane_center - plane_size * (plane_axis1 - plane_axis2)  

plane_polydata = vtk.vtkPolyData()  
points = vtk.vtkPoints()  
cells = vtk.vtkCellArray()  

points.InsertNextPoint(p1)  
points.InsertNextPoint(p2)  
points.InsertNextPoint(p3)  
points.InsertNextPoint(p4)  

quad = vtk.vtkQuad()  
quad.GetPointIds().SetId(0, 0)  
quad.GetPointIds().SetId(1, 1)  
quad.GetPointIds().SetId(2, 2)  
quad.GetPointIds().SetId(3, 3)  

cells.InsertNextCell(quad)  
plane_polydata.SetPoints(points)  
plane_polydata.SetPolys(cells)  

plane_model_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode", "Midsagittal_Plane")  
plane_model_node.SetAndObservePolyData(plane_polydata)  

plane_display = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelDisplayNode")  
plane_model_node.SetAndObserveDisplayNodeID(plane_display.GetID())  
plane_display.SetColor(0, 1, 1)  
plane_display.SetOpacity(0.7)  
