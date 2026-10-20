boxes = list(map(int, input("Enter space seperated Box IDs: ").strip().split()))


def count_boxes(boxes):
    if boxes == []:
        return 0

    return 1 + count_boxes(boxes[1:])


print(count_boxes(boxes=boxes))
