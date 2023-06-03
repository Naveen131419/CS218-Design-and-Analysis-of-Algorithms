n = int(input())
l=[]
for i in (input().split()):
    l.append(int(i))
# count = 0
# while(sorted(l) != l):
#     for i in range(n-1):
#         if(l[i]>l[i+1]):
#             temp = l[i]
#             l[i] = l[i+1]
#             l[i+1] = temp
#             count+=1
#     n-=1
# def cocktail_shaker_sort(arr):
#     n = len(arr)
#     swapped = True
#     start = 0
#     end = n-1
#     swaps = 0
#     while (swapped == True):
#         swapped = False
#         # move the largest element to the end of the list
#         for i in range(start, end):
#             if (arr[i] > arr[i+1]):
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#                 swapped = True
#                 swaps += 1
#         if (swapped == False):
#             break
#         swapped = False
#         end = end-1
#         # move the smallest element to the beginning of the list
#         for i in range(end-1, start-1, -1):
#             if (arr[i] > arr[i+1]):
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#                 swapped = True
#                 swaps += 1
#         start = start+1
#     return arr, swaps
# l, count = cocktail_shaker_sort(l)
# print(count)


class Sorter:
    def count_inversions(self, arr):
        _, num_intercambios = self._merge_sort(arr)
        return num_intercambios

    def _merge_sort(self, arr):
        if len(arr) <= 1:
            return arr, 0
        else:
            mid = len(arr) // 2
            left, a = self._merge_sort(arr[:mid])
            right, b = self._merge_sort(arr[mid:])
            merged, c = self._merge(left, right)
            return merged, a + b + c

    def _merge(self, left, right):
        i = j = 0
        merged = []
        count = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                count += len(left) - i
        merged += left[i:]
        merged += right[j:]
        return merged, count

s = Sorter()

print(s.count_inversions(l))