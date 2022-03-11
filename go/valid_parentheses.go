package leetcode

// Time complexity: O(n) where n the length of the input string is
// Space complexity: O(n)
func isValid(s string) bool {
	stack := make([]rune, 0)

	for _, el := range []rune(s) {
		if el == '(' || el == '[' || el == '{' {
			stack = append(stack, el)
		} else if len(stack) > 0 &&
			((el == ')' && stack[len(stack)-1] == '(') ||
				(el == ']' && stack[len(stack)-1] == '[') ||
				(el == '}' && stack[len(stack)-1] == '{')) {
			stack = stack[0 : len(stack)-1]
		} else {
			return false
		}
	}
	return len(stack) == 0
}
