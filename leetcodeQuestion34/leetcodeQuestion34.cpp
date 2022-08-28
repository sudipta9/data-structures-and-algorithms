#include <bits/stdc++.h>
using namespace std;

int firstOccurrence(int arr[], int n, int target)
{
    int start = 0;
    int end = n - 1;
    int mid = (start + (end - start) / 2);
    int leftPos = -1;
    while (start <= end)
    {
        if (arr[mid] == target)
        {
            leftPos = mid;
            end = mid - 1;
        }
        else if (arr[mid] < target)
        {
            start = mid + 1;
        }
        else if (arr[mid] > target)
        {
            end = mid - 1;
        }
        mid = (start + (end - start) / 2);
    }
    return leftPos;
}

int lastOccurrence(int arr[], int n, int target)
{
    int start = 0;
    int end = n - 1;
    int mid = (start + (end - start) / 2);
    int rightPos = -1;
    while (start <= end)
    {
        if (arr[mid] == target)
        {
            rightPos = mid;
            start = mid + 1;
        }
        else if (arr[mid] < target)
        {
            start = mid + 1;
        }
        else if (arr[mid] > target)
        {
            end = mid - 1;
        }
        mid = (start + (end - start) / 2);
    }
    return rightPos;
}

int main()
{
    int arr[7] = {1, 2, 3, 3, 3, 4, 7};
    cout << "[" << firstOccurrence(arr, 7, 3) << ", " << lastOccurrence(arr, 7, 3) << "]" << endl;
}