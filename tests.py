'''
Unit Testing for firecall
==================
'''

import firecall
import unittest


class firecallTests(unittest.TestCase):

    def setUp(self):
        self.url = 'https://firebase.firebaseio.com/users/mugo'
        self.firebase = firecall.Firebase(self.url)

    def tearDown(self):
        pass

    def callback(self, data):
        return str(data)

    def test_valid_urls(self):
        URLS = {
            'http_protocol': 'http://my_firebase.firebaseio.com',
            'non_firebaseio.com_domain': 'https://gochomugo.github.io',
            'leading_hyphen': 'https://-my-firebase.firebaseio.com',
            'trailing_hyphen': 'https://my-firebase-.firebaseio.com',
            'dollar_in_childname': 'https://my-firebase.firebaseio.com/user$',
            'period_in_childname': 'https://my-firebase.firebaseio.com/user.s',
            'bracket[_in_childname': 'https://my-firebase.firebaseio.com/user[s',
            'bracket]_in_childname': 'https://my-firebase.firebaseio.com/user]s',
            'ctrl_char_x00': 'https://my_firebase.firebaseio.com/use\x00r',
        }
        for key in URLS:
            self.assertRaises(ValueError, firecall.general.valid_url,
                              URLS[key])

    def test_attr(self):
        url = 'https://firebase.firebaseio.com'
        auth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        firebase = firecall.Firebase(url, auth=auth)
        attrs = firebase.attr()
        self.assertTrue(url in attrs, 'url in .attr() missing')
        self.assertTrue(auth in attrs, 'token in .attr() missing')

    def test_root(self):
        root = self.firebase.root()
        correct_root = 'https://firebase.firebaseio.com'
        self.assertEqual(root, correct_root, 'Incorrect .root()')

    def test_name(self):
        name = self.firebase.name()
        correct_name = 'mugo'
        self.assertEqual(name, correct_name, 'Incorrect .name()')

    def test_toString(self):
        toString = self.firebase.toString()
        correct_toString = self.url
        self.assertEqual(toString, correct_toString, 'Incorrect .toString()')

    def test_url_correct(self):
        corrected_url = self.firebase.url_correct('/gocho')
        correct_url = ''.join([self.url, '/gocho', '.json'])
        self.assertEqual(corrected_url, correct_url, 'Correcting URL fails')
        corrected_url = self.firebase.url_correct('/gocho', auth='AUTH')
        correct_url = ''.join([self.url, '/gocho', '.json', '?', 'auth=AUTH'])
        self.assertEqual(corrected_url, correct_url, 'Correcting URL fails')
        corrected_url = self.firebase.url_correct('/gocho', export=True)
        correct_url = ''.join([self.url, '/gocho', '.json', '?',
                               'format=export'])
        self.assertEqual(corrected_url, correct_url, 'Correcting URL fails')
        corrected_url = self.firebase.url_correct('/gocho',
                                                  auth='AUTH', export=True)
        correct_url = ''.join([self.url, '/gocho', '.json', '?', 'auth=AUTH',
                               '&', 'format=export'])
        self.assertEqual(corrected_url, correct_url, 'Correcting URL fails')

    def test_parent(self):
        parent = self.firebase.parent()
        parent_url = parent.attr()[1]
        correct_url = 'https://firebase.firebaseio.com/users'
        self.assertEqual(parent_url, correct_url, '.parent() fails')

    def test_child(self):
        child = self.firebase.child(point='/gocho')
        child_url = child.attr()[1]
        correct_url = 'https://firebase.firebaseio.com/users/mugo/gocho'
        self.assertEqual(child_url, correct_url, '.child() fails')

    def _test_None_returns(self):
        dummy_res = self.firebase.get('/')
        self.assertIsNone(dummy_res, '.get fails to return None')
        dummy_res = self.firebase.put('/')
        self.assertIsNone(dummy_res, '.put fails to return None')
        dummy_res = self.firebase.post('/')
        self.assertIsNone(dummy_res, '.post fails to return None')
        dummy_res = self.firebase.update('/')
        self.assertIsNone(dummy_res, '.update fails to return None')
        dummy_res = self.firebase.delete('/')
        self.assertIsNone(dummy_res, '.delete fails to return None')
        dummy_res = self.firebase.export('/')
        self.assertIsNone(dummy_res, '.export fails to return None')


if __name__ == '__main__':
    unittest.main()
