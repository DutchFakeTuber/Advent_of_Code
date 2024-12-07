from itertools import product

TEST: str = open("test.txt")
DATA: str = open("input.txt")

def fetchData(data: str) -> list[tuple[tuple[int], tuple[int]]]:
    return list(tuple(tuple(map(int, parts.split(', '))) for parts in line.split(' @ ')) for line in data.splitlines())

def equation(a: tuple[int], b: tuple[int], va: tuple[int], vb: tuple[int]) -> None | list[int]:
    # Get two coordinates
    a, va = a[:2], (a[0]+va[0], a[1]+va[1])
    b, vb = b[:2], (b[0]+vb[0], b[1]+vb[1])
    # Slope = Delta(Y)/Delta(X)
    slopes: tuple[int] = ((a[1]-va[1])/(a[0]-va[0]), (b[1]-vb[1])/(b[0]-vb[0]))
    # Point-slope formula
    # y - y1 = slope * (x - x1) where y and x are unknown
    ay, ax = complex(0, a[1]).conjugate(), complex(slopes[0], slopes[0]*a[0]).conjugate()
    by, bx = complex(0, b[1]).conjugate(), complex(slopes[1], slopes[1]*b[0]).conjugate()
    A, B = complex(ax.real, ax.imag+(ay.imag*-1)), complex(bx.real, bx.imag+(by.imag*-1))
    AB: complex = complex(A.real+(B.real*-1), B.imag+(A.imag*-1))
    # Lines are parallel if 0
    if AB.real == 0: return None
    AB = AB.imag / AB.real
    return [AB, B.imag + (B.real * AB.real)]

def partOne(hailstones: list[tuple[int], tuple[int]], area: tuple) -> int:
    done: dict = dict()
    inside: int = 0
    for (a, va), (b, vb) in product(hailstones, hailstones):
        if not done.get((a, va), False):
            done[(a, va)] = True
        if done.get((b, vb), False) or (a, va) == (b, vb):
            continue
        coords: list[int] | None = equation(a, b, va, vb)
        if coords is None:
            continue
        if (a[0] < coords[0] if va[0] > 0 else a[0] > coords[0]) and (a[1] < coords[1] if va[1] > 0 else a[1] > coords[1]) \
                and (b[0] < coords[0] if vb[0] > 0 else b[0] > coords[0]) and (b[1] < coords[1] if vb[1] > 0 else b[1] > coords[1]):
            if area[0] <= coords[0] <= area[1] and area[0] <= coords[1] <= area[1]:
                inside += 1
    return inside

def eliminate(materialized: list[list[int]]) -> tuple[int]:
    # Gaussian elimination
    for i in range(len(materialized)):
        temp: int = materialized[i][i]
        materialized[i] = [num/temp for num in materialized[i]]
        for j in range(i+1, len(materialized)):
            temp: int = materialized[j][i]
            materialized[j] = [val - temp * materialized[i][num] for num, val in enumerate(materialized[j])]
    for i in range(len(materialized)-1, -1, -1):
        for j in range(i):
            temp = materialized[j][i]
            materialized[j] = [val - temp * materialized[i][num] for num, val in enumerate(materialized[j])]
    return materialized

def matrix(hailstones: list[tuple[tuple[int], tuple[int]]], coords: tuple[tuple[int]], vector: tuple[tuple[int]]) -> list[list[int]]:
    g: function = lambda h, v: h[v[0]][v[1]] # Getter function
    (c1, c2), (v1, v2) = coords, vector
    reform: list[list[int]] = [[-g(h,v2), g(h,v1), g(h,c2), -g(h,c1), g(h,c2)*g(h,v1)-g(h,c1)*g(h,v2)] for h in hailstones]
    return [[a - b for a, b in zip(r, reform[-1])] for r in reform[:4]]

def partTwo(hailstones: list[tuple[int], tuple[int]]) -> int:
    class H: x=(0, 0); y=(0, 1); z=(0, 2); vx=(1, 0); vy=(1, 1); vz=(1, 2)
    xy = eliminate(matrix(hailstones, (H.x, H.y), (H.vx, H.vy)))
    z = eliminate(matrix(hailstones, (H.z, H.y), (H.vz, H.vy)))
    return int(xy[0][-1] + xy[1][-1] + z[0][-1])

if __name__ == "__main__":
    hailstones: list[tuple[int], tuple[int]] = fetchData(DATA)
    print(partOne(hailstones, (2e14, 4e14)))
    print(partTwo(hailstones))
