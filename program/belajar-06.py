import os

nama = raw_input('siapa namamu? ')
os.system('say %s' % nama)
agama = raw_input('apa agamamu? ')
if agama == 'islam':
    print 'halo',nama, 'jaga solhat di masjid yaa'