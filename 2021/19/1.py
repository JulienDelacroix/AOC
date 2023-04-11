import sys
import numpy as np
import itertools
from queue import Queue

def compute_rotations():
    for x, y, z in itertools.permutations([0, 1, 2]):
        for sign_x, sign_y, sign_z in itertools.product([-1, 1], repeat=3):
            rot = np.zeros((3, 3))
            rot[0, x] = sign_x
            rot[1, y] = sign_y
            rot[2, z] = sign_z
            if np.linalg.det(rot) == 1:
                yield rot

def check_sensor_view(reference_view, reference_set, view):
    for rot in rotations:
        transformed_view = list(map(lambda p: np.matmul(rot, p), view))
        for p0_ref in reference_view:
            for px_ref in transformed_view:
                offset = p0_ref - px_ref
                translated_view = list(map(lambda p: tuple(p + offset), transformed_view))
                if sum(p in reference_set for p in translated_view) >= 12:
                    return True, rot, offset
    return False, None, None

sensors = []
for block in sys.stdin.read().split("\n\n"):
    pos_list = []
    for line in block.splitlines()[1:]:
        pos = tuple(map(int, line.split(",")))
        pos_list.append(pos)
    sensors.append(pos_list)

rotations = [ r for r in compute_rotations() ]
queue = Queue()
done = set()
parents = {}

done.add(0)
queue.put(0)
while not queue.empty():
    sensor_ref = queue.get()
    view_ref = sensors[sensor_ref]
    print(sensor_ref, queue.queue, done)

    reference_view = list(map(lambda p: np.array(p), view_ref))
    reference_set = set(view_ref)

    for sensor, view in enumerate(sensors):
        if sensor in done: continue

        match, rotation, offset = check_sensor_view(reference_view, reference_set, view)
        if match:
            done.add(sensor)
            queue.put(sensor)
            parents[sensor] = (sensor_ref, rotation, offset)

all_beacons = set()
for sensor, view in enumerate(sensors):

    sensor_beacons = view
    while sensor in parents:
        sensor, rot, offset =  parents[sensor]
        sensor_beacons = list(map(lambda p: tuple(np.matmul(rot, p) + offset), sensor_beacons))
    all_beacons.update(sensor_beacons)

print(len(all_beacons))
