# https://www.educative.io/m/closest-meeting-point for MXM matrix
'''
def shortest_distance_travelled_2(m, points):
m: size of the grid
points: coordinates of the occupied locations on the grid

BF 
1. For each candidate position in the MXM grid, find the distance from all people(locations occupied by people): TC: O(M^2)
   1.1. For each point in points list: find and add distance from other points
   1.2. update distance and res_x, res_y if distance is less than the min seen so far
2. return res_x, res_y
'''
import math

class point:
  
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
def compute_distance_from_others(point, points):
  dist = 0.0
  for other_point in points:
    if other_point.x != point.x or other_point.y != point.y:
      dist += math.sqrt(pow(other_point.x - point.x, 2) + pow(other_point.y - point.y, 2))
  return dist

def shortest_distance_travelled(m, points):  
  #pt = point(1, 1)
  res_x, res_y = None, None
  min_dist = 1.5 * m + 1 # more than the max possible value of distance in square matrix
  for cand_point in points:
    for other_point in points:
      if other_point.x != cand_point.x or other_point.y != cand_point.y:
        total_dist = compute_distance_from_others(cand_point, points)
        if total_dist < min_dist:
          min_dist = total_dist
          res_x = cand_point.x
          res_y = cand_point.y
      else:
        continue    
  return point(res_x, res_y)
