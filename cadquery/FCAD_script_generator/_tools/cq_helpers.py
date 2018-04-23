from math import sqrt

def v_add(p1, p2):
    return (p1[0]+p2[0],p1[1]+p2[1])

def v_sub(p1, p2):
    return (p1[0]-p2[0],p1[1]-p2[1])

def get_third_arc_point1(starting_point, end_point):
    px = v_sub(end_point, starting_point)
    return v_add((px[0]*(1-1/sqrt(2)),px[1]*(1/sqrt(2))),starting_point)

def get_third_arc_point2(starting_point, end_point):
    px = v_sub(end_point, starting_point)
    return v_add((px[0]*(1/sqrt(2)),px[1]*(1-1/sqrt(2))),starting_point)

def add_p_to_chain(chain, rel_point):
    chain.append(v_add(chain[len(chain)-1], rel_point))

def mirror(chain, direction="x"):
    result = []
    for point in chain:
        if direction=="x":
            result.append((point[0]*-1,point[1]))
        else:
            result.append((point[0],point[1]*-1))

    return result

def poline(points, plane):
    sp = points.pop()
    plane=plane.moveTo(sp[0],sp[1])
    plane=plane.polyline(points)
    return plane

def union_all(objects):
    o = objects[0]
    for i in range(1,len(objects)):
        o = o.union(objects[i])
    return o
