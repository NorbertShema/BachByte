class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        total_apples = sum(apple)

        # Sort capacities from largest to smallest
        capacity.sort(reverse=True)

        used_boxes = 0

        for box in capacity:
            total_apples -= box # remove the box capacity from the apples.
            used_boxes += 1 # increment the number of boxes

            if total_apples <= 0:
                return used_boxes

        return used