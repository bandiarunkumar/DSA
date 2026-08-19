class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}

        # Store reserved seats for each affected row
        for row, seat in reservedSeats:
            rows.setdefault(row, set()).add(seat)

        # Assume every row can initially fit 2 groups
        answer = 2 * n

        for seats in rows.values():
            left = all(seat not in seats for seat in [2, 3, 4, 5])
            middle = all(seat not in seats for seat in [4, 5, 6, 7])
            right = all(seat not in seats for seat in [6, 7, 8, 9])

            if left and right:
                # Two groups can sit
                continue
            elif left or middle or right:
                # Only one group can sit
                answer -= 1
            else:
                # No group can sit
                answer -= 2

        return answer