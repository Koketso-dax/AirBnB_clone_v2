#!/usr/bin/python3
''' Module for testing DBStorage '''

import unittest
import os
from datetime import datetime
import MySQLdb
from models.user import User
from models import storage


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                 'DBStorage test not supported')
class TestDBStorage(unittest.TestCase):
    ''' Tests for DBStorage '''

    def setUp(self):
        ''' Set up for testing '''
        self.db = MySQLdb.connect(user=os.getenv('HBNB_MYSQL_USER'),
                                  host=os.getenv('HBNB_MYSQL_HOST'),
                                  passwd=os.getenv('HBNB_MYSQL_PWD'),
                                  port=3306,
                                  db=os.getenv('HBNB_MYSQL_DB'))

    def tearDown(self):
        ''' Clean up after testing '''
        self.db.close()

    def test_new_and_save(self):
        ''' Test the new and save methods '''
        cur = self.db.cursor()
        cur.execute('SELECT COUNT(*) FROM users')
        old_count = cur.fetchall()[0][0]

        new_user = User(first_name='Jack',
                        last_name='Bond',
                        email='jack@bond.com',
                        password='12345')
        new_user.save()

        cur.execute('SELECT COUNT(*) FROM users')
        new_count = cur.fetchall()[0][0]

        self.assertEqual(new_count, old_count + 1)

    def test_new(self):
        ''' Test if a new object is correctly added to the database '''
        new_user = User(email='john2020@gmail.com',
                        password='password',
                        first_name='John',
                        last_name='Zoldyck')
        self.assertNotIn(new_user, storage.all().values())
        new_user.save()
        self.assertIn(new_user, storage.all().values())

        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM users WHERE id="{}"'.format(new_user.id))
        result = cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertIn('john2020@gmail.com', result)
        self.assertIn('password', result)
        self.assertIn('John', result)
        self.assertIn('Zoldyck', result)

    def test_delete(self):
        ''' Test if an object is correctly deleted from the database '''
        new_user = User(email='john2020@gmail.com',
                        password='password',
                        first_name='John',
                        last_name='Zoldyck')
        obj_key = 'User.{}'.format(new_user.id)

        new_user.save()
        self.assertIn(new_user, storage.all().values())

        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM users WHERE id="{}"'.format(new_user.id))
        result = cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertIn('john2020@gmail.com', result)
        self.assertIn('password', result)
        self.assertIn('John', result)
        self.assertIn('Zoldyck', result)
        self.assertIn(obj_key, storage.all(User).keys())

        new_user.delete()
        self.assertNotIn(obj_key, storage.all(User).keys())

    def test_reload(self):
        ''' Test reloading of the database session '''
        cursor = self.db.cursor()
        cursor.execute(
            'INSERT INTO users(id, created_at, updated_at, email, password' +
            ', first_name, last_name) VALUES(%s, %s, %s, %s, %s, %s, %s);',
            [
                '4447-by-me',
                str(datetime.now()),
                str(datetime.now()),
                'ben_pike@yahoo.com',
                'pass',
                'Benjamin',
                'Pike',
            ]
        )

        storage.reload()
        self.assertIn('User.4447-by-me', storage.all())

    def test_save(self):
        ''' Test if an object is successfully saved to the database '''
        new_user = User(email='john2020@gmail.com',
                        password='password',
                        first_name='John',
                        last_name='Zoldyck')

        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM users WHERE id="{}"'.format(new_user.id))
        result = cursor.fetchone()
        cursor.execute('SELECT COUNT(*) FROM users;')
        old_count = cursor.fetchone()[0]

        self.assertIsNone(result)
        self.assertNotIn(new_user, storage.all().values())

        new_user.save()

        cursor.execute('SELECT * FROM users WHERE id="{}"'.format(new_user.id))
        result = cursor.fetchone()
        cursor.execute('SELECT COUNT(*) FROM users;')
        new_count = cursor.fetchone()[0]

        self.assertIsNotNone(result)
        self.assertEqual(old_count + 1, new_count)
        self.assertIn(new_user, storage.all().values())
