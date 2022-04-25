package main

func CheckParenteses(v string) bool {
	var a []int
	for _, i := range v {
		if i == '(' {
			a = append(a, 1)
		} else {
			if i == ')' {
				if len(a) == 0 {
					return false
				}
				a = a[1:]
			}
		}
	}
	return len(a) == 0
}
