func twoSum(nums []int, target int) []int {
	hashMap := make(map[int]int, 0)
	var diff int

	for i, num := range nums {
		diff = target-num
		if pair, ok := hashMap[diff]; ok {
			return []int{pair, i}
		}
		hashMap[num] = i
	}

	return []int{0,0}
}