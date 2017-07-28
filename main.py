from register import Register

print('Please input software abbreviation(default:AGG2):')
software = input()
print('Please input user id(default:123456):')
uid = input()
print('Please input challenge code:')
challenge_code = input()

print('Your key is ' + Register(uid, challenge_code, software).get_key())
