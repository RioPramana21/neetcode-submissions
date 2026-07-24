func isAnagram(s string, t string) bool {
	var count [26]int

	lenS := len(s)
	lenT := len(t)

	if lenS != lenT {
		return false
	}

	for i := range lenS {
		count[s[i]-'a']++
		count[t[i]-'a']--
	}

	if count != [26]int{0} {
		return false
	}

	return true
}