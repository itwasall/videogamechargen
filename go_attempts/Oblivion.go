package main

import (
	"fmt"
	"io/ioutil"
	"log"

	"gopkg.in/yaml.v2"
	//"gopkg.in/yaml.v3"
)

type OblSkill struct {
	name  string
	value int
}

type OblSkillList [21]OblSkill

type OblClass struct {
	name           string
	specialisation string
	attributes     [2]string
	skills         [7]string
}

type OblClassList [21]OblClass

type OblBirthsign struct {
	name    string
	effects []map[string]int // map is keyed array
}

type Character struct {
	name string
}

func main() {

	skill_file, err := ioutil.ReadFile("../Oblivion/data/Classes.yml")
	if err != nil {
		log.Fatal(err)
	}

	data := make(map[string]OblClass)

	err2 := yaml.Unmarshal(skill_file, &data)

	if err2 != nil {
		log.Fatal(err2)
	}

	for k := range data {
		fmt.Printf("%s\n", k)
		for skill := range data[k].skills {
			fmt.Printf("%s\n", data[k].skills[skill])
		}
		// fmt.Printf(d)
	}

}

/*
	fmt.Println("epic line")
	var class_list = make_classes()
	fmt.Println(class_list)
}
*/
