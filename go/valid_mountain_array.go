package leetcode

// Time complexity: O(n)
// Space complexity: O(1)
func validMountainArray(arr []int) bool {
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
