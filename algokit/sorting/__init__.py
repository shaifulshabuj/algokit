from typing import List, Any

class Sorting:
    @staticmethod
    def bubble_sort(arr: List[Any]) -> List[Any]:
        """
        Implementation of bubble sort algorithm.
        Time Complexity: O(n²)
        Space Complexity: O(1)
        """
        n = len(arr)
        arr_copy = arr.copy()
        
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr_copy[j] > arr_copy[j + 1]:
                    arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
        
        return arr_copy
    
    @staticmethod
    def quick_sort(arr: List[Any]) -> List[Any]:
        """
        Implementation of quick sort algorithm.
        Time Complexity: O(n log n) average, O(n²) worst case
        Space Complexity: O(log n)
        """
        if len(arr) <= 1:
            return arr
        
        arr_copy = arr.copy()
        
        def _quick_sort(arr, low, high):
            if low < high:
                pivot_idx = _partition(arr, low, high)
                _quick_sort(arr, low, pivot_idx - 1)
                _quick_sort(arr, pivot_idx + 1, high)
        
        def _partition(arr, low, high):
            pivot = arr[high]
            i = low - 1
            
            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1
        
        _quick_sort(arr_copy, 0, len(arr_copy) - 1)
        return arr_copy
    
    @staticmethod
    def merge_sort(arr: List[Any]) -> List[Any]:
        """
        Implementation of merge sort algorithm.
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        if len(arr) <= 1:
            return arr
        
        arr_copy = arr.copy()
        
        def _merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = _merge_sort(arr[:mid])
            right = _merge_sort(arr[mid:])
            
            return _merge(left, right)
        
        def _merge(left, right):
            result = []
            i = j = 0
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        
        return _merge_sort(arr_copy)
    
    @staticmethod
    def heap_sort(arr: List[Any]) -> List[Any]:
        """
        Implementation of heap sort algorithm.
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """
        arr_copy = arr.copy()
        n = len(arr_copy)
        
        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            Sorting._heapify(arr_copy, n, i)
        
        # Extract elements one by one
        for i in range(n - 1, 0, -1):
            arr_copy[0], arr_copy[i] = arr_copy[i], arr_copy[0]
            Sorting._heapify(arr_copy, i, 0)
        
        return arr_copy
    
    @staticmethod
    def _heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            Sorting._heapify(arr, n, largest)
