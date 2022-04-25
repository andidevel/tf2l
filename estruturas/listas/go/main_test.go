package main

import "testing"

func TestCheckParenteses(t *testing.T) {
	test_cases := map[string]bool{
		"(())":               true,
		"()()(()())":         true,
		"())":                false,
		")(":                 false,
		"f(x) = ((x+2)/3)*4": true,
	}

	for s, b := range test_cases {
		got := CheckParenteses(s)
		if got != b {
			t.Errorf("[%s] Expect %v, got %v\n", s, b, got)
		}
	}
}
