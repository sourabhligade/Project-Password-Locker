#! python3
# pw.py - An insecure password locker program.
PASSWORDS={'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6','blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt','luggage': '12345'}
import sys ,pyperclip
if len(sys.argv)<2:
    print('Usage:python chapterproject1.py [account] - copy account password')
    sys.exit()

account=sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for' + account + 'copied to clipboard.')
else:
    print('There is no account names ' + account)