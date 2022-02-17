#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Character:
    def __init__(self, name):
        self.name = name
        self.special = {
            'Strength': 1,
            'Perception': 1,
            'Endurance': 1,
            'Charisma': 1,
            'Intelligence': 1,
            'Agility': 1,
            'Luck': 1
        }
        self.derived_stats = self.get_derived()
        self.skills = self.get_skills()

    def get_derived(self):
        return {
            'Action Points': (self.special['Agility'] / 2) + 5,
            'Armor Class': self.special['Agility'],
            'Carry Weight': 25 + (self.special['Strength'] * 25),
            'Critial Chance': self.special['Luck'],
            'Damage Resistance': 0,
            'Healing Rate': max(self.special['Endurance']/3, 1),
            'Party Limit': self.special['Charisma'] / 2,
            'Perk Rate': 3,
            'Poison Resistance': self.special['Endurance'] * 5,
            'Radiation Resistance': self.special['Endurance'] * 2,
            'Sequence': self.special['Perception'] * 2,
            'Skill Rate': self.special['Intelligence'] + 5
        }

    def get_skills(self):
        return {
            'Small Guns': {
                'value': 5 + (4 * self.special['Agility']), 'stat': ['Agility'] },
            'Big Guns': {
                'value': 2 * self.special['Agility'], 'stat': ['Agility'] },
            'Energy Weapons': {
                'value': 2 * self.special['Agility'], 'stat': ['Agility'] },
            'Unarmed': {
                'value': 30 + (2 * (self.special['Agility'] + self.special['Strength'])), 'stat': ['Agility', 'Strength'] },
            'Melee Weapons': {
                'value': 30 + 2 * (self.special['Agility'] + self.special['Strength']), 'stat': ['Agility', 'Strength'] },
            'Throwing': {
                'value': 4 * self.special['Agility'], 'stat': ['Agility'] },
            'First Aid': {
                'value': 2 * (self.special['Perception'] + self.special['Intelligence']), 'stat': ['Perception', 'Intelligence'] },
            'Doctor': {
                'value': 5 + self.special['Perception'] + self.special['Intelligence'], 'stat': ['Perception', 'Intelligence'] },
            'Sneak': {
                'value': 5 + (3 * self.special['Agility']), 'stat': ['Agility'] },
            'Lockpick': {
                'value': 10 + self.special['Agility'] + self.special['Perception'], 'stat': ['Agility', 'Perception'] },
            'Steal': {
                'value': 3 * self.special['Agility'], 'stat': ['Agility'] },
            'Traps': {
                'value': 10 + self.special['Perception'] + self.special['Agility'], 'stat': ['Perception', 'Agility'] },
            'Science': {
                'value': 4 * self.special['Intelligence'], 'stat': ['Intelligence'] },
            'Repair': {
                'value': 3 * self.special['Intelligence'], 'stat': ['Intelligence'] },
            'Speech': {
                'value': 5 * self.special['Charisma'], 'stat': ['Charisma'] },
            'Barter': {
                'value': 4 * self.special['Charisma'], 'stat': ['Charisma'] },
            'Gambling': {
                'value': 5 * self.special['Luck'], 'stat': ['Luck'] },
            'Outdoorsman': {
                'value': 2 * (self.special['Endurance'] + self.special['Intelligence']), 'stat': ['Endurance', 'Intelligence'] }
        }

    def print_skills(self):
        for skill in self.skills:
            print(f"{skill}: {self.skills[skill]['value']}%")

jerry = Character('Jerry')
jerry.print_skills()
