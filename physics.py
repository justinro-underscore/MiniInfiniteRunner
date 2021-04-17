def is_touching(box1, box2):
  (b1_x1, b1_y1, b1_x2, b1_y2) = box1
  (b2_x1, b2_y1, b2_x2, b2_y2) = box2
  x = (b1_x1 >= b2_x1 and b1_x1 <= b2_x2) or (b1_x2 >= b2_x1 and b1_x2 <= b2_x2) or (b2_x1 >= b1_x1 and b2_x1 <= b1_x2) or (b2_x2 >= b1_x1 and b2_x2 <= b1_x2)
  y = (b1_y1 >= b2_y1 and b1_y1 <= b2_y2) or (b1_y2 >= b2_y1 and b1_y2 <= b2_y2) or (b2_y1 >= b1_y1 and b2_y1 <= b1_y2) or (b2_y2 >= b1_y1 and b2_y2 <= b1_y2)
  return x and y