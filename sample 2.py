import re

def re_process(string):
    patterns = ['will make', 'make', 'made', 'makes']
    for pattern in patterns:
            r = re.findall(rf'{pattern}', string)
            if r:
                return r[0]  # The string 
    return


class Convert:
    vowels = '[aeiou]'

    @classmethod
    def MAKE(cls, verb, pandiwa):
        if verb in ['make', 'makes']:
            return cls.__conv_make(pandiwa)
        elif verb == 'made':
            return cls.__conv_made(pandiwa)
        elif verb == 'will make':
            return cls.__conv_will_make(pandiwa)

    @classmethod
    def __conv_made(cls, pandiwa): # converts the pandiwa into a proper pandiwa
        result = re.sub(rf'({cls.vowels})', r'in\1', pandiwa, count=1)
        return result
    
    @classmethod
    def __conv_make(cls, pandiwa): # converts the pandiwa into a proper pandiwa
        result = re.sub(rf'(\w)({cls.vowels})', r'\1in\2\1\2', pandiwa, count=1)
        return result
    
    @classmethod
    def __conv_will_make(cls, pandiwa):  # converts the pandiwa into a proper pandiwa
        string = re.sub(rf'(\w)({cls.vowels})', r'\1\2\1\2', pandiwa, count=1)

        li = string.rsplit('o', 1)
        string = 'u'.join(li)

        result = re.search(rf'{cls.vowels}\Z', string)
        if result: # If the last letter is a vowel
            print('[vowel]')
            string = string + 'hin'
        else:  # If the last letter in a consonant
            print('[consonant]')
            string = string + 'in'
        return string

    


class Factory:

    def __init__(self, input_):

        self.input = input_  # Full string
        inputs = self.inputs = input_.split() # Splitted string

        self.subj = inputs[0].lower()  # gets the subject

        _result = re_process(input_)
        if not _result:
            raise Exception
        
        print(f'verb = {_result}')
        self.make = _result # the English VERB phrase

    @property
    def pandiwa(self):
        make = self.make
        _pandiwa = re.findall(rf'{make}\s(\w*)\s', self.input)
        print(f'pandiwa = {_pandiwa[0]}')
        return _pandiwa[0].lower()
    
    @property
    def simuno(self):
        table = {
            'i': 'ko',
            'you': 'mo',
            'he': 'niya',
            'she': 'niya',
            'we': 'natin',
            'they': 'nila'
        }
        result = table[self.subj]
        print(f'simuno = {result}')
        return result
  
    @property
    def output(self):
        last = self.inputs[-1]
        pandiwa = Convert.MAKE(self.make, self.pandiwa)
        s = ' '
        final_string = pandiwa + s + self.simuno + s + 'ang' + s + last[:-1] + last[-1]

        return final_string.capitalize()


program = Factory('I will make yakap the artista.')
print(program.output)  # Output: 'Yayakapin ko ang artista.'

        





