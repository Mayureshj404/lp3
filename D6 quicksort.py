import random

class Solution:
    def quickSort_deterministic(self, arr, low, high):
        if low < high:
            pindex = self.partition(arr, low, high)
            self.quickSort_deterministic(arr, low, pindex - 1)
            self.quickSort_deterministic(arr, pindex + 1, high)
    
    def quickSort_randomized(self, arr, low, high):
        if low < high:
            pindex = self.randomizedPartition(arr, low, high)
            self.quickSort_randomized(arr, low, pindex - 1)
            self.quickSort_randomized(arr, pindex + 1, high)
    
    def randomizedPartition(self, arr, low, high):
        randomPivotIndex = random.randint(low, high)
        arr[low], arr[randomPivotIndex] = arr[randomPivotIndex], arr[low]
        return self.partition(arr, low, high)
    
    def partition(self, arr, low, high):
        pivot, i, j = arr[low], low, high
        while i < j:
            while i < high and arr[i] <= pivot: i += 1
            while arr[j] > pivot: j -= 1
            if i < j: arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]
        return j

# Get input from user
arr = list(map(int, input("Enter space-separated integers: ").split()))

# Create Solution instance
sol = Solution()

# Perform deterministic quicksort
arr_det = arr.copy()
sol.quickSort_deterministic(arr_det, 0, len(arr_det) - 1)
print("Sorted array (Deterministic QuickSort):", *arr_det)

# Perform randomized quicksort
arr_rand = arr.copy()
sol.quickSort_randomized(arr_rand, 0, len(arr_rand) - 1)
print("Sorted array (Randomized QuickSort):", *arr_rand)