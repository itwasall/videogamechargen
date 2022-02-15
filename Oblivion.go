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
	name           string    `yaml:"name"`
	specialisation string    `yaml:"specialisation"`
	attributes     [2]string `yaml:"attributes`
	skills         [7]string `yaml:"skills"`
}

type OblClassList [21]OblClass

type OblBirthsign struct {
	name    string
	effects []map[string]int // map is keyed array
}

type Character struct {
	name string
}

func (c *OblClass) Parse(data []byte) error {
	return yaml.Unmarshal(data, c)
}

func main() {

	skill_file, err := ioutil.ReadFile("Oblivion/data/Classes.yml")
	if err != nil {
		log.Fatal(err)
	}
	var skill OblSkill
	if err := skill.Parse(skill_file); err != nil {
		log.Fatal(err)
	}

	fmt.Printf("%+v\n", skill)

	//for k := range data {
	//	fmt.Printf("%s\n", k)
	//for skill := range data[k].skills {
	//fmt.Printf("%v\n", data[k].skills[skill])
	//}
	// fmt.Printf(d)
	//}

}

/*
	fmt.Println("epic line")
	var class_list = make_classes()
	fmt.Println(class_list)
}
*/
