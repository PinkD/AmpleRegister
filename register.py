from _md5 import md5


class Register:
    def __init__(self, uid, challenge_code, software):
        self._part_1 = 'AmpleSoundUser'
        if uid:
            self._uid = uid
        else:
            self._uid = '123456'
        self._challenge_code = challenge_code
        self._part_4 = 'App'
        if software:
            self._software = software
        else:
            self._software = 'AGG2'
        self._part_6 = 'AmpleThisIsNewStart!Sound', 'XSDAmpleThisIsNewStart!SoundCJ'
        self._part_7 = 'WindowsIsStable'

    def _get_challenge_code(self):
        if self._challenge_code:
            return self._challenge_code[:-1].split('#').pop()
        else:
            raise ValueError('bad challenge code')

    def _get_salt(self):
        return self._part_6[0]

    def get_key(self):
        challenge_code = self._get_challenge_code()
        salt = self._get_salt()
        source = self._part_1 + self._uid + challenge_code + self._part_4 + self._software + salt + self._part_7
        # print(source)
        return md5(source.encode()).hexdigest().upper()
