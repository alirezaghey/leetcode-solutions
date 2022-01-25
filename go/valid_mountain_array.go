package leetcode

// Time complexity: O(n)
// Space complexity: O(1)
// Alternative solution
func validMountainArray(arr []int) bool {
	N := len(arr)
	if N < 3 {
		return false
	}

	peaks := 0
	for i := 1; i < N-1; i++ {
		if arr[i] == arr[i-1] || arr[i] == arr[i+1] {
			return false
		}
		if arr[i] < arr[i-1] && arr[i] < arr[i+1] {
			return false
		}
		if arr[i] > arr[i-1] && arr[i] > arr[i+1] {
			peaks++
		}
		if peaks > 1 {
			return false
		}
	}
	return peaks == 1

}

// Time complexity: O(n)
// Space complexity: O(1)
func validMountainArray2(arr []int) bool {
	if len(arr) < 3 {
		return false
	}

	foundPeak := false
	for i := 1; i < len(arr)-1; i++ {
		if foundPeak == false {
			if arr[i] <= arr[i-1] {
				return false
			}
			if arr[i] == arr[i+1] {
				return false
			}
			if arr[i] > arr[i+1] {
				foundPeak = true
			}
		} else {
			if arr[i] <= arr[i+1] {
				return false
			}
		}
	}
	return foundPeak
}
