func minStartValue(nums []int) int {
    best, curr := 1, 0
    
    for _, el := range nums {
        curr += el
        if curr < 1 {
            if next_best := 1 - curr; next_best > best {
            best = next_best
            }
        }
    }
    return best
}