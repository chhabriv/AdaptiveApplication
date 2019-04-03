# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 01:41:39 2019

@author: viren
"""

class User:
    def __init__(self, name=None, age=0,
                 gender=None, budget=0, 
                 duration=0, tags=None,
                 is_first=True):
        self.name=name
        self.age=age
        self.gender=gender
        self.budget=budget
        self.duration=duration
        self.tags=tags
        self.is_first=is_first

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self.name = value

    @name.deleter
    def name(self):
        del self.name
        
    @property
    def age(self):
        return self.name

    @age.setter
    def age(self, value):
        self.age = value

    @age.deleter
    def age(self):
        del self.age

    @property
    def gender(self):
        return self.gender

    @gender.setter
    def gender(self, value):
        self.gender = value

    @gender.deleter
    def gender(self):
        del self.gender
        
    @property
    def budget(self):
        return self.budget

    @budget.setter
    def budget(self, value):
        self.budget = value

    @budget.deleter
    def budget(self):
        del self.budget
        
    @property
    def duration(self):
        return self.duration

    @duration.setter
    def duration(self, value):
        self.duration = value

    @duration.deleter
    def duration(self):
        del self.duration

    @property
    def tags(self):
        return self.tags

    @tags.setter
    def tags(self, value):
        self.tags = value

    @tags.deleter
    def tags(self):
        del self.tags
        
    @property
    def is_first(self):
        return self.is_first

    @is_first.setter
    def is_first(self, value):
        self.is_first = value

    @is_first.deleter
    def is_first(self):
        del self.is_first
