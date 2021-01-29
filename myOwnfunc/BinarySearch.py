# -*- coding: utf-8 -*-
# 2020-02-03
# author Liu,Yuxin
# entre number:
def binarySearch(arr, l, r, x):
    # 基本判断
    if r >= l:
        mid = int(l + (r - l) / 2)

        # 元素整好的中间位置
        if arr[mid] == x:
            return mid

            # 元素小于中间位置的元素，只需要再比较左边的元素
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

            # 元素大于中间位置的元素，只需要再比较右边的元素
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # 不存在
        return -1

def BinarySearch( x, list):
    list.sort()
    low = 0
    high = len(list)-1
    mid = (low+high)//2
    while low <= high:
        mid = (low+high)//2
        if x > list[mid]:
            low = mid+1
        elif x == list[mid]:
            return mid
        else:
            high = mid-1









