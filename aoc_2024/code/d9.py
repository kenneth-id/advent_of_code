SAMPLE = "2333133121414131402"


def get_block(input):
    block = []
    cur_id = 0
    for i, c in enumerate(input):
        if i % 2 == 0:
            block.extend([cur_id] * int(c))
            cur_id += 1
        else:
            block.extend("." * int(c))

    return block


def get_block2(input):
    block = []
    cur_id = 0
    for i, c in enumerate(input):
        if i % 2 == 0:
            if c != "0":
                block.append((cur_id, int(c)))
            cur_id += 1
        else:
            if c != "0":
                block.append((".", int(c)))

    return block, cur_id - 1


def defragment_2(block, max_id):
    cur_block = block.copy()
    cur_id = max_id

    while cur_id > 0:
        left = 0
        right = len(cur_block) - 1

        while left < right and cur_block[right][0] != cur_id:
            right -= 1

        file_id, num_rep = cur_block[right][0], cur_block[right][1]
        block_len = num_rep
        while left < right:
            if cur_block[left][0] == ".":
                dot_len = cur_block[left][1]
                if dot_len >= block_len:
                    leftover = dot_len - block_len
                    new_block = (
                        cur_block[:left]
                        + [(file_id, num_rep)]
                        + ([(".", leftover)] if leftover else [])
                        + cur_block[left + 1 : right]
                        + [(".", num_rep)]
                        + cur_block[right + 1 :]
                    )
                    cur_block = new_block
                    break
                else:
                    left += 1
            else:
                left += 1

        cur_id -= 1

    return cur_block


def checksum_2(defragmented):
    checksum = 0

    cur_pos = 0
    for elem, num_rep in defragmented:
        if elem != ".":
            for _ in range(num_rep):
                checksum += cur_pos * elem
                cur_pos += 1
        else:
            cur_pos += num_rep
    return checksum


def defragment(block):
    left = 0
    right = len(block) - 1
    n = len(block)

    while left < right and left < n:
        while block[right] == "." and right > left:
            right -= 1

        while block[left] != "." and left < right:
            left += 1

        block[left], block[right] = block[right], block[left]
        left += 1


def checksum(block):
    checksum = 0
    for i, elem in enumerate(block):
        if elem != ".":
            checksum += i * elem
    return checksum


with open("/Users/kennethlee/workspace/aoc/2024/input/d9.txt") as f:
    input = f.read().strip()
    # input = SAMPLE.strip()
    block, max_id = get_block2(input)
    defragmented = defragment_2(block, max_id)
    # defragment(block)
    print(checksum_2(defragmented))
