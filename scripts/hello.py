#!/usr/bin/env python3
import dev_aberto
import gettext
from babel.dates import format_datetime
gettext.install('cli', localedir='locale') 

if __name__ == '__main__':
    date, name = dev_aberto.hello()
    
    print(_('Último commit feito em:'), format_datetime(date), _('por'), name)
