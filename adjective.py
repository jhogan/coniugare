#! /usr/bin/python

first_second='first/second'
third='third'

null=None
true=True
false=False

male='male'
female='female'
neuter='neuter'

singular = 'singular'
plural = 'plural'

nominative='nominative'
genitive='genitive'
vocative='vocative'
accusative='accusative'
dative='dative'
ablative='ablative'
locative='locative'
cases={nominative : [ ('us', 'a',  'um'), ('I',    'ae',   'a')    ],\
       genitive   : [ ('I',  'ae', 'I'),  ('Orum', 'Arum', 'Orum') ],\
       dative     : [ ('O',  'ae', 'O'),  ('Is',   'Is',   'Is')   ],\
       accusative : [ ('um', 'am', 'um'), ('Os',   'As',   'a')    ],\
       ablative   : [ ('O',  'A',  'O'),  ('Is',   'Is',   'Is')   ]}

class adjective:
    def __init__(self, ns_male, ns_female, ns_neuter):
        self._ns_male = ns_male
        self._ns_female = ns_female
        self._ns_neuter = ns_neuter

    def declension(self):
        return first_second

    def stem(self):
        # The only example in the book was bonus so I'm
        # not sure if there are other affixes
        return self.nominative(singular, male).rstrip('us')

    def nominative(self, number=null, gender=null):
        if not gender:
            return  self.nominative(number, male), \
                    self.nominative(number, female), \
                    self.nominative(number, neuter)
        if self.declension() == first_second:
            if number == singular:
                if gender == male:
                    return self._ns_male
                if gender == female:
                    return self.stem() + self._ns_female
                if gender == neuter:
                    return self.stem() + self._ns_neuter
            else:
                if gender == male:
                    return self.stem() + "I"
                if gender == female:
                    return self.stem() + "ae"
                if gender == neuter:
                    return self.stem() + "a"

    def getCase(self, case, number, gender=null):
        if not gender:
            return  self.getCase(case, number, male), \
                    self.getCase(case, number, female), \
                    self.getCase(case, number, neuter)
        affixes=cases[case]
        if self.declension() == first_second:
            if number == singular:
                affixes=affixes[0]
                if gender == male:
                    return self.stem() + affixes[0]
                if gender == female:
                    return self.stem() + affixes[1]
                if gender == neuter:
                    return self.stem() + affixes[2]
            else:
                affixes=affixes[1]
                if gender == male:
                    return self.stem() + affixes[0]
                if gender == female:
                    return self.stem() + affixes[1]
                if gender == neuter:
                    return self.stem() + affixes[2]

    def genitive(self, number=null, gender=null):
        return self.getCase('genitive', number, gender)

    def dative(self, number=null, gender=null):
        return self.getCase('dative', number, gender)

    def accusative(self, number=null, gender=null):
        return self.getCase('accusative', number, gender)

    def ablative(self, number=null, gender=null):
        return self.getCase('ablative', number, gender)



a = adjective('bonus', 'a', 'um')
print "Declension: %s" % a.declension()

print "Case        Masc      Fem       Neut"
print "            singular"
print "Nominative  %s        %s        %s  " % a.nominative(singular)
print "Genitive    %s        %s        %s  " % a.genitive(singular)
print "Dative      %s        %s        %s  " % a.dative(singular)
print "Accusative  %s        %s        %s  " % a.accusative(singular)
print "Ablative    %s        %s        %s  " % a.ablative(singular)
print "\n"
print "            plural"
print "Nominative  %s        %s        %s  " % a.nominative(plural)
print "Genitive    %s        %s        %s  " % a.genitive(plural)
print "Dative      %s        %s        %s  " % a.dative(plural)
print "Accusative  %s        %s        %s  " % a.accusative(plural)
print "Ablative    %s        %s        %s  " % a.ablative(plural)

