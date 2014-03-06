
import sys, random, math, pygame
from pygame.locals import *

class Node(object):
    """Node in a tree"""
    def __init__(self, point, parent):
        super(Node, self).__init__()
        self.point = point
        self.parent = parent


def dist(p1,p2):
    return sqrt((p1[0]-p2[0])*(p1[0]-p2[0])+(p1[1]-p2[1])*(p1[1]-p2[1]))

def step_from_to(p1, p2, epsilon):
    if dist(p1,p2) < epsilon:
        return p2
    else:
        theta = atan2(p2[1]-p1[1],p2[0]-p1[0])
        return p1[0] + epsilon*cos(theta), p1[1] + epsilon*sin(theta)

def point_circle_collision(p1, p2, radius):
    distance = dist(p1,p2)
    if (distance <= radius):
        return True
    return False
