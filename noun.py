first= 'first'
second='second'
third= 'third'
fourth='fourth'
fifth= 'fifth'

vowels=('a', 'e', 'i', 'o', 'u')

singular = 'singular'
plural = 'plural'

f='female'
m='male'

null=None
true=True
false=False

class noun:
<<<<<<< .mine
    def __init__(self, nominative, genitive_singular, gender):
        self._nominative = nominative
=======
    def __init__(self, nominative_singular, genitive_singular, gender):
        self._nominative_singular = nominative_singular
        self._genitive_singular = genitive_singular
>>>>>>> .r1025
        self._gender = gender
        self._genitive_singular = genitive_singular

<<<<<<< .mine
    def setgenitive_singular(self, v):
        dashix = v.find('-');
        if (dashix > 0):
            suf = v[dashix+1:]

            
        
    

        

    def nominative(self): return self._nominative
=======
    def gender(self):     return self._gender
>>>>>>> .r1025

    def stem(self):
        gen = self._genitive_singular
        dashix = gen.find('-')
        if dashix != -1:
            nom = self.nominative(singular)
            if nom[-1:] in vowels: 
                stem = nom[0:-1]
            elif nom[-2:] == 'us':
                stem = nom[0:-2]
            return stem
        else:
            if gen[-2:] in ('ae', 'is', 'us', 'ei'):
                return gen[0:-2]
            elif gen[-1:] == 'i':
                return gen[0:-1]

<<<<<<< .mine
=======
    def genitive_suffix(self):
        gen = self._genitive_singular
        dashix = gen.find('-')
        if gen[0:1] == '-':
            return gen[1:]
        else:
            if gen[-2:] in ('ae', 'is', 'us', 'ei'):
                return gen[-2:]
            elif gen[-1:] == 'i':
                return gen[-1:]

>>>>>>> .r1025
    def nominative(self, number=null): 
        # TODO Neuters follow the 'double neuter rule'
        # but this isn't explained in the book
        if (number==null):
            return (self.nominative(singular), \
                    self.nominative(plural))

<<<<<<< .mine
    def declination(self):
        gencase = self.genitive_singular
        if gencase[0:1] != "-":
            stemchg
=======
        if number == singular:
            return self._nominative_singular
        else:
            dec = self.declension()
            stem = self.stem()
            if dec == first:  return stem + "ae"
            if dec == second: return stem + "i"
            if dec == third:  return stem + "Es"
            if dec == fourth: return stem + "ae"
            if dec == fifth:  return stem + "ae"
>>>>>>> .r1025

    def genitive(self, number=null):  
        if (number==null):
            return (self.genitive(singular), \
                    self.genitive(plural))
        stem = self.stem()
        if number == singular:
            gen = self._genitive_singular
            if gen[0:1] == '-':
                return stem + self.genitive_suffix()
            else:
                return gen
        else:
            dec = self.declension()
            if dec == first:  return stem + 'Arum'
            if dec == second: return stem + 'Orum'
            if dec == third:  return stem + 'um'
            if dec == fourth: return stem + 'uum'
            if dec == fifth:  return stem + 'Erum'

    def dative(self, number=null):  
        if (number==null):
            return (self.dative(singular), \
                    self.dative(plural))
        dec = self.declension()
        stem = self.stem()
        if number == singular:
            if dec == first:  return stem + 'ae'
            if dec == second: return stem + 'O'
            if dec == third:  return stem + 'I'
            if dec == fourth: return stem + 'uI'
            if dec == fifth:  return stem + 'eI'
        if number == plural:
            if dec == first:  return stem + 'Is'
            if dec == second: return stem + 'Is'
            if dec == third:  return stem + 'ibus'
            if dec == fourth: return stem + 'ibus'
            if dec == fifth:  return stem + 'Ebus'

    def accusative(self, number=null):  
        if (number==null):
            return (self.accusative(singular), \
                    self.accusative(plural))
        dec = self.declension()
        stem = self.stem()
        if number == singular:
            if dec == first:  return stem + 'am'
            if dec == second: return stem + 'um'
            if dec == third:  return stem + 'em'
            if dec == fourth: return stem + 'um'
            if dec == fifth:  return stem + 'em'
        if number == plural:
            if dec == first:  return stem + 'As'
            if dec == second: return stem + 'Os'
            if dec == third:  return stem + 'Es'
            if dec == fourth: return stem + 'Us'
            if dec == fifth:  return stem + 'Es'

    def ablative(self, number=null):  
        if (number==null):
            return (self.ablative(singular), \
                    self.ablative(plural))
        dec = self.declension()
        stem = self.stem()
        if number == singular:
            if dec == first:  return stem + 'A'
            if dec == second: return stem + 'O'
            if dec == third:  return stem + 'e'
            if dec == fourth: return stem + 'u'
            if dec == fifth:  return stem + 'E'
        if number == plural:
            if dec == first:  return stem + 'Is'
            if dec == second: return stem + 'Is'
            if dec == third:  return stem + 'ibus'
            if dec == fourth: return stem + 'Us'
            if dec == fifth:  return stem + 'Ebus'
            
    def declension(self):
        suffix = self.genitive_suffix()

        if suffix == "ae": return first
        if suffix == "i":  return second
        if suffix == "is": return third
        if suffix == "us": return fourth
        if suffix == "Ei": return fifth

    def gender_acronym(self):
        if self._gender == f: return 'f.'
        if self._gender == m: return 'm.'

    def str(self):
        return self.nominative(singular) + ' ' +  \
            self._genitive_singular + ' ' + \
            self.gender_acronym()

    

n = noun('ala', '-ae', m)
print n.str()

print "\nDeclension: %s\n" % n.declension()
print "Case        Singular Plural"
print "Nominative  %s       %s" % n.nominative()
print "Genitive    %s       %s" % n.genitive()
print "Dative      %s       %s" % n.dative()
print "Accusative  %s       %s" % n.accusative()
print "Ablative    %s       %s" % n.ablative()

    
