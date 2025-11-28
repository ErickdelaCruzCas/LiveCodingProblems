


# Binary search (ascendente):
# mid > target → mover derecha↓ => R = mid - 1
# mid < target → mover izquierda↑ => L = mid + 1
# Si buscas en descendente, invierte ambas condiciones.

nums = [-1,0,3,5,9,12]
target = 9
# Orden Ascendete
def search(nums, target) -> int:
    L, R = 0, len(nums) - 1
    while L <= R:
        mid = (L + R) // 2
        if nums[mid] > target:
            R = mid - 1     # izquierda
        elif nums[mid] < target:
            L = mid + 1     # derecha
        else:
            return mid
    return -1


# Binary Search:
# ASC: mid > target → R = mid - 1 | mid < target → L = mid + 1
# DESC: mid > target → L = mid + 1 | mid < target → R = mid - 1
# Último índice siempre = len(arr) - 1

arr = [8, 7, 6, 5, 4, 3, 3, 1] 
target = 9
# Orden Descendente 
def binarySearch(arr, target):
    L, R = 0, len(arr) - 1
    while L <= R:
        mid = (L + R)
        if arr[mid] < target:   # target está a la izquierda
            R = mid - 1
        elif arr[mid] > target: # target está a la derecha
            L = mid + 1
        else:
            return mid
    return -1

