class Solution:
    def isHappy(self, n: int) -> bool:

        # Helper function that performs the digit-square transformation.
        # It generates the "next" value in the sequence.
        # For example, x = 82 -> 8^2 + 2^2 = 64 + 4 = 68.
        def next_num(x):
            total = 0
            while x > 0:
                digit = x % 10
                total += digit * digit
                x //= 10
            return total

        # Floyd's cycle detection uses two pointers:
        # - slow: moves one transformation per iteration
        # - fast: moves two transformations per iteration
        #
        # If the sequence eventually becomes 1, fast will reach 1.
        # If the sequence falls into a cycle (unhappy number),
        # then the fast pointer will eventually "lap" the slow pointer
        # inside the cycle, meaning slow == fast at some point.
        slow = n
        fast = next_num(n)  # fast moves first step immediately

        # The key loop:
        # Continue until either fast reaches 1 (happy number)
        # or slow meets fast (cycle detected -> unhappy number).
        while fast != 1 and slow != fast:
            # slow moves ahead one step
            slow = next_num(slow)

            # fast moves two steps ahead
            fast = next_num(next_num(fast))

            # The moment slow == fast, both pointers are inside a repeating cycle.
            # That implies the number is not happy.

        # If fast == 1, the number is happy.
        # If fast != 1, a cycle was detected, and the number is unhappy.
        return fast == 1

        