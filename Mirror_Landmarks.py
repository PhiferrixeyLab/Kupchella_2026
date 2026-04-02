# Define Midsagittal plane and Mirror Landmarks Custom Script

import numpy as np

def reflect_landmarks():
    msp_landmarks = slicer.util.getNode('MSP')
    rlp_landmarks = slicer.util.getNode('RLP')
    rzc_curve = slicer.util.getNode('RZC')

    msp_points = []
    for i in range(msp_landmarks.GetNumberOfControlPoints()):
        position = [0.0, 0.0, 0.0]
        msp_landmarks.GetNthControlPointPosition(i, position)
        msp_points.append(np.array(position))

    msp_points = np.array(msp_points)
    mean_msp = np.mean(msp_points, axis=0)
    cov_matrix = np.cov(msp_points.T)
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
    plane_normal = eigenvectors[:, np.argmin(eigenvalues)]
    plane_normal = plane_normal / np.linalg.norm(plane_normal)
    plane_point = mean_msp

    rlp_points = []
    for i in range(rlp_landmarks.GetNumberOfControlPoints()):
        position = [0.0, 0.0, 0.0]
        rlp_landmarks.GetNthControlPointPosition(i, position)
        rlp_points.append(np.array(position))

    reflected_rlp_points = []
    for pt in rlp_points:
        vector = pt - plane_point
        distance = np.dot(vector, plane_normal)
        reflected_pt = pt - 2 * distance * plane_normal
        reflected_rlp_points.append(reflected_pt)

    reflected_rlp_node = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', 'LLP')
    for pt in reflected_rlp_points:
        reflected_rlp_node.AddControlPoint(pt)

    rzc_points = []
    for i in range(rzc_curve.GetNumberOfControlPoints()):
        position = [0.0, 0.0, 0.0]
        rzc_curve.GetNthControlPointPosition(i, position)
        rzc_points.append(np.array(position))

    reflected_rzc_points = []
    for pt in rzc_points:
        vector = pt - plane_point
        distance = np.dot(vector, plane_normal)
        reflected_pt = pt - 2 * distance * plane_normal
        reflected_rzc_points.append(reflected_pt)

    reflected_rzc_node = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsCurveNode', 'LZC')
    for pt in reflected_rzc_points:
        reflected_rzc_node.AddControlPoint(pt)

reflect_landmarks()
