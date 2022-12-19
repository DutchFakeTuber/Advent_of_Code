from collections import deque
from Not_Enough_Materials import INPUT

def getData() -> list[dict]:
    return [dict(blueprint=int(line.split(' ')[1][:-1]),
                 ore=int(line.split(' ')[6]),
                 clay=int(line.split(' ')[12]),
                 obsidian=[int(line.split(' ')[18]), int(line.split(' ')[21])],
                 geode=[int(line.split(' ')[27]), int(line.split(' ')[30])])
            for line in INPUT.splitlines() if len(line) != 0]

def geodes(blueprint: dict, time: int) -> int:
    # M_OR, M_CL, M_OB, M_GE, A_OR, A_CL, A_OB, A_GE, TIME
    initial: tuple = (1, 0, 0, 0, 0, 0, 0, 0, time)
    MAX_ORE: int = max(blueprint['ore'], blueprint['clay'], blueprint['obsidian'][0], blueprint['geode'][0])
    queue: deque = deque([initial])
    seen: set = set()
    times: set = set()
    max_geodes: int = 0
    while len(queue):
        m_or, m_cl, m_ob, m_ge, a_or, a_cl, a_ob, a_ge, t = queue.popleft()
        if t not in times:
            times.add(t)
        max_geodes: int = max(max_geodes, a_ge)
        if t == 0:
            continue
        a_or: int = min(a_or, MAX_ORE + (MAX_ORE - m_or) * (t - 1))
        a_cl: int = min(a_cl, blueprint['obsidian'][1] + (blueprint['obsidian'][1] - m_cl) * (t - 1))
        a_ob: int = min(a_ob, blueprint['geode'][1] + (blueprint['geode'][1] - m_ob) * (t - 1))
        state: tuple = (m_or, m_cl, m_ob, m_ge, a_or, a_cl, a_ob, a_ge, t)
        if state in seen:
            continue
        seen.add(state)
        if a_or >= blueprint['ore'] and m_or < MAX_ORE:
            queue.append((m_or + 1, m_cl, m_ob, m_ge, a_or - blueprint['ore'] + m_or, a_cl + m_cl, a_ob + m_ob, a_ge + m_ge, t - 1))
        if a_or >= blueprint['clay'] and m_cl < blueprint['obsidian'][1]:
            queue.append((m_or, m_cl + 1, m_ob, m_ge, a_or + m_or - blueprint['clay'], a_cl + m_cl, a_ob + m_ob, a_ge + m_ge, t - 1))
        if a_or >= blueprint['obsidian'][0] and a_cl >= blueprint['obsidian'][1] and m_ob < blueprint['geode'][1]:
            queue.append((m_or, m_cl, m_ob + 1, m_ge, a_or + m_or - blueprint['obsidian'][0], a_cl - blueprint['obsidian'][1] + m_cl, a_ob + m_ob, a_ge + m_ge, t - 1))
        if a_or >= blueprint['geode'][0] and a_ob >= blueprint['geode'][1]:
            queue.append((m_or, m_cl, m_ob, m_ge + 1, a_or - blueprint['geode'][0] + m_or, a_cl + m_cl, a_ob - blueprint['geode'][1] + m_ob, a_ge + m_ge, t - 1))
        queue.append((m_or, m_cl, m_ob, m_ge, a_or + m_or, a_cl + m_cl, a_ob + m_ob, a_ge + m_ge, t - 1))
    return max_geodes

def partOne() -> int:
    blueprints: list[dict] = getData()
    return sum(b['blueprint'] * geodes(b, 24) for b in blueprints)

def partTwo() -> int:
    blueprints: list[dict] = getData()
    geode: list[int] = [geodes(b, 32) for b in blueprints[:3]]
    return geode[0] * geode[1] * geode[2]

def main() -> None:
    print(f'ANSWER PART ONE: {partOne()}')
    print(f'ANSWER PART TWO: {partTwo()}')
    
if __name__ == "__main__":
    main()
