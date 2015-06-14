#! /usr/bin/python
#  // vim: set et ts=4 sw=4 fdm=marker:
first= 'first'
second='second'
third ='third'
third_io ='third -io'
fourth ='fourth'

imperfect='imperfect'
perfect='perfect'
true=True
false=False
null=None
def personstr(number):
    if number == 1: return first
    if number == 2: return second
    if number == 3: return third

class verbconf:
    def __init__(self, person, singular, tense):
        self.person(person)
        self.singular(singular)
        self.tense(tense)

    def person(self, v=null):   
        if v: self._person=v;   
        return self._person

    def singular(self, v=null): 
        if v!=null: self._singular=v; 
        return self._singular

    def tense(self, v=null):    
        if v: self._tense=v;    
        return self._tense

class verb:
    def __init__(self, pp1, pp2, pp3, pp4):
        self._pp1=pp1; self._pp2=pp2
        self._pp3=pp3; self._pp4=pp4

    def iscopula(self):
        # to be or not to be
        return self.principleparts() == \
            ('sum', 'esse', 'fuI', 'futUrus')
            

    def principleparts(self):
        return self._pp1, self._pp2, self._pp3, self._pp4

    def principlepart(self, which):
        if which == first:  return self._pp1
        if which == second: return self._pp2
        if which == third:  return self._pp3
        if which == fourth: return self._pp4

    def conjugation(self):
        last_three=self._pp2[-3:]
        if   last_three=="Are":
            return first
        elif last_three=="Ere":
            return second
        elif last_three=="ere":
            if self._pp1[0:-2]=="io":
                return third_io
            else:
                return third
        elif last_three=="Ire":
            return fourth

    def continuous_aspect_stem(self):
        # aka: present system
        # Lop off the suffix of pp1
        # FIXME: It's unclear whether Ere
        # should be lopped off or just re
        # BUG: There is an exception for third_io
        # and fourth conjugation but it isn't clear
        # what it is. See page 36.
        return self._pp2[0:-2]

    def completed_aspect_stem(self):
        # aka: perfect system
        return self._pp3[0:-1]

    def tense_indicator(self, tense):
        # Should this me a static method?
        # TODO: Add (self, vc) "overload"
        if tense == imperfect: 
            return 'ba' # were doing

    def pronoun(self, vc):
        # Should this me a static method?
        person=vc.person() 
        if vc.tense() == imperfect:
            if vc.singular():
                if person == first: return 'm'
                if person == second: return 's'
                if person == third: return 't'
            else:
                if person == first: return 'mus'
                if person == second: return 'tis'
                if person == third: return 'nt'
        elif vc.tense() == perfect:
            if vc.singular():
                if person == first: return 'I'
                if person == second: return 'istI'
                if person == third: return 'it'
            else:
                if person == first: return 'imus'
                if person == second: return 'istis'
                if person == third: return 'Erunt'

    def conjugate(self, verbconf):
        vc=verbconf
        if vc.tense() == imperfect:
            if not self.iscopula():
                pstem = self.continuous_aspect_stem()
                tindicator = self.tense_indicator(vc.tense())
                pnoun = self.pronoun(vc)
                return pstem + tindicator + pnoun
            else:
                if vc.singular():
                    if person == first: return 'eram'
                    if person == second: return 'erAs'
                    if person == third: return 'erat'
                else:
                    if person == first: return 'erAmus'
                    if person == second: return 'erAtis'
                    if person == third: return 'erant'
        elif vc.tense() == perfect:
            pstem = self.completed_aspect_stem()
            pnoun = self.pronoun(vc)
            return pstem + pnoun
            
v = verb('sum', 'esse', 'fuI', 'futUrus')
print "%s %s %s %s" % (v.principlepart(first),   \
                        v.principlepart(second), \
                        v.principlepart(third),  \
                        v.principlepart(fourth))
print
print "COPULA:                  %s" % ('No', 'Yes')[v.iscopula()]
print "CONJUGATION:             %s" % v.conjugation()
print "CONTINUOUS_ASPECT_STEM:  %s" % v.continuous_aspect_stem()
print "COMPLETED_ASPECT_STEM:   %s" % v.completed_aspect_stem()

print "\nIMPERFECT"
print "\tPERSON  SINGULAR PLURAL"
for person in range(1, 4):
    person = personstr(person)
    print "\t" + person.upper() + " " + \
        "\t" +  v.conjugate( verbconf(person, true,  imperfect) ) + " " + \
        "\t " + v.conjugate( verbconf(person, false, imperfect) )

print "\nPERFECT"
print "\tPERSON  SINGULAR PLURAL"
for person in range(1, 4):
    person = personstr(person)
    print "\t" + person.upper() + " " + \
        "\t" +  v.conjugate( verbconf(person, true,  perfect) ) + " " + \
        "\t " + v.conjugate( verbconf(person, false, perfect) )

