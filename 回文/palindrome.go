package main

import (
	"fmt"
)

func Reverse(s string) string {

    runes := []rune(s)

    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }

    return string(runes)
}

func main() {

	str := make(chan string)

	go func() {
		for {
			s, _ := <-str // 文字列が送られるのを待って受け取る
			fmt.Printf("%s\n", Reverse(s))
		}
	}()

	fmt.Println("単語を入力してください（終了するには\"quit\"）")
	var s string

	for {
		fmt.Scan(&s)
		if s == "quit" {
			break
		}
		str <- s
	}
}
