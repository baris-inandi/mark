package main

import "io/ioutil"

func readFile(filename string) ([]byte, error) {
	return ioutil.ReadFile(filename)
}
func main() {
	readFile("test.txt")
}
