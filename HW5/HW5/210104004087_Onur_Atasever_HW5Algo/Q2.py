import math

def convexHullFinder(pointsList):
    #Calculates the convex hull of a set of points using the QuickHull algorithm.
    if len(pointsList) < 3:
        return pointsList

    # Sorting the points and selecting extremities
    sortedPoints = sorted(pointsList, key=lambda coord: coord[0])
    extremeLeft = sortedPoints[0]
    extremeRight = sortedPoints[-1]
    hullPoints = [extremeLeft, extremeRight]

    # Removing the extreme points for further processing
    sortedPoints.remove(extremeLeft)
    sortedPoints.remove(extremeRight)

    # Classifying the remaining points
    upperHalf, lowerHalf = partitionPoints(extremeLeft, extremeRight, sortedPoints)
    hullPoints += hullConstruction(extremeLeft, extremeRight, upperHalf)
    hullPoints += hullConstruction(extremeRight, extremeLeft, lowerHalf)

    return hullPoints

def hullConstruction(anchor1, anchor2, subsetPoints):
    #Constructs hull segments from a subset of points.
    if not subsetPoints:
        return []

    # Identifying the farthest point
    maxDistancePoint = max(subsetPoints, key=lambda singlePoint: lineToPointDistance(anchor1, anchor2, singlePoint))
    subsetPoints.remove(maxDistancePoint)
    segmentHull = [maxDistancePoint]

    # Splitting points around the farthest point
    upperSegment, lowerSegment = partitionPoints(anchor1, maxDistancePoint, subsetPoints)
    nextSegmentUpper, nextSegmentLower = partitionPoints(maxDistancePoint, anchor2, subsetPoints)

    # Recursive hull construction
    segmentHull += hullConstruction(anchor1, maxDistancePoint, upperSegment)
    segmentHull += hullConstruction(maxDistancePoint, anchor2, nextSegmentUpper)

    return segmentHull

def partitionPoints(startPoint, endPoint, pointSet):
    #Partitions a set of points based on their position relative to a line.
    aboveLine = []
    belowLine = []
    lineSlope = (endPoint[1] - startPoint[1]) / (endPoint[0] - startPoint[0]) if endPoint[0] != startPoint[0] else float('inf')
    lineIntercept = startPoint[1] - lineSlope * startPoint[0]

    for point in pointSet:
        if point[1] > lineSlope * point[0] + lineIntercept:
            aboveLine.append(point)
        elif point[1] < lineSlope * point[0] + lineIntercept:
            belowLine.append(point)

    return aboveLine, belowLine

def lineToPointDistance(pointA, pointB, externalPoint):
    #Calculates the perpendicular distance of a point from a line.
    a = pointA[1] - pointB[1]
    b = pointB[0] - pointA[0]
    c = pointA[0] * pointB[1] - pointB[0] * pointA[1]

    return abs(a * externalPoint[0] + b * externalPoint[1] + c) / math.sqrt(a ** 2 + b ** 2)

# Test run of the
def testConvexHull():
    testPoints = [(1,1), (2,5), (3,3), (5,3), (3,2), (2,2)]
    print(convexHullFinder(testPoints))

testConvexHull()
