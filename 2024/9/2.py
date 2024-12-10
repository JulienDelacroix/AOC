import queue
import collections

Block = collections.namedtuple('Block', ['pos', 'size'])

file_blocks = []
sorted_free_blocks = [ queue.PriorityQueue() for _ in range(10) ]

current_pos = 0
for i, v in enumerate(input()):
    block_size = int(v)
    if i % 2:
        sorted_free_blocks[block_size].put(Block(current_pos, block_size))
    else:
        file_blocks.append(Block(current_pos, block_size))
    current_pos += block_size

res = 0
while len(file_blocks):
    file = file_blocks.pop()
    file_id = len(file_blocks)
        
    free_list = [ sorted_free_blocks[s].get() for s in range(file.size, 10) if not sorted_free_blocks[s].empty() ]
    free = min(free_list)
    for b in free_list:
        if b != free:
            sorted_free_blocks[b.size].put(b)
             
    if file.pos < free.pos:
        res += sum(range(file.pos, file.pos + file.size)) * file_id
    else:
        moved = min(free.size, file.size)
        res += sum(range(free.pos, free.pos + moved)) * file_id
        sorted_free_blocks[moved].put(Block(file.pos, moved))
        if moved < free.size:
            sorted_free_blocks[free.size - moved].put(Block(free.pos + moved, free.size - moved))
        if moved < file.size:
            file_blocks.append(Block(file.pos + moved, file.size - moved))

print(res)
