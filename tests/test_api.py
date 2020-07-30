"""API tests"""
# pylint: disable=invalid-name
import secrets
import string
import uuid
import datetime as dt

DUMMY_ID = str(uuid.UUID('00000000-0000-0000-0000-000000000000'))
AUTHORS_URL = '/authors/'
BOOKS_URL = '/books/'
AUTH_URL = '/auth/'


class TestApi:
    """TEST API"""
    jwt_token = None
    author_1_id = author_1_etag = author_1 = None
    book_1_id = book_1_etag = book_1 = None
    book_2_id = book_2_etag = book_2 = None

    def test_login_jwt(self, test_client):
        """Login for JWT token"""
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(8))
        ret = test_client.post(AUTH_URL, query_string={'user': 'toto', 'password': password})
        ret_val = ret.json
        assert ret.status_code == 200
        TestApi.jwt_token = ret_val.pop('access_token')

    def test_authors_url(self, test_client):
        """GET AUTHORS_URL """
        ret = test_client.get(AUTHORS_URL)
        assert ret.status_code == 200
        assert ret.json == []

    def test_authors_post(self, test_client):
        """ADD AUTHORS"""
        TestApi.author_1 = {
            "first_name": "John",
            "last_name": "Doe",
            "birth_date": dt.datetime(1958, 10, 2).strftime('%Y-%m-%d')
        }
        headers_jwt = {
            'Authorization': 'Bearer {}'.format(TestApi.jwt_token)
        }

        ret = test_client.post(AUTHORS_URL, json=TestApi.author_1, headers=headers_jwt)
        assert ret.status_code == 201
        ret_val = ret.json
        TestApi.author_1_id = ret_val.pop('id')
        TestApi.author_1_etag = ret.headers['ETag']
        ret_val.pop('created_at')
        ret_val.pop('updated_at')
        assert ret_val == TestApi.author_1

    def test_authors_getlist(self, test_client):
        """GET LIST"""
        ret = test_client.get(AUTHORS_URL)
        assert ret.status_code == 200
        ret_val = ret.json
        assert len(ret_val) == 1
        assert ret_val[0]['id'] == TestApi.author_1_id

    def test_authors_getid(self, test_client):
        """GET AUTHORS  by ID"""
        ret = test_client.get(AUTHORS_URL + TestApi.author_1_id)
        assert ret.status_code == 200
        assert ret.headers['ETag'] == TestApi.author_1_etag
        ret_val = ret.json
        ret_val.pop('id')
        ret_val.pop('created_at')
        ret_val.pop('updated_at')
        assert ret_val == TestApi.author_1

    def test_authors_put(self, test_client):
        """PUT AUTHORS"""
        TestApi.author_1.update({'first_name': 'John2'})

        headers_jwt = {
            'Authorization': 'Bearer {}'.format(TestApi.jwt_token),
            'If-Match': TestApi.author_1_etag
        }

        ret = test_client.put(
            AUTHORS_URL + TestApi.author_1_id,
            json=TestApi.author_1,
            headers=headers_jwt
        )
        assert ret.status_code == 200
        ret_val = ret.json
        ret_val.pop('id')
        ret_val.pop('created_at')
        ret_val.pop('updated_at')
        TestApi.author_1_etag = ret.headers['ETag']
        assert ret_val == TestApi.author_1

    def test_authors_put404(self, test_client):
        """PUT AUTHORS  with wrong ID"""
        headers_jwt = {
            'Authorization': 'Bearer {}'.format(TestApi.jwt_token),
            'If-Match': TestApi.author_1_etag
        }
        ret = test_client.put(
            AUTHORS_URL + DUMMY_ID,
            json=TestApi.author_1,
            headers=headers_jwt
        )
        assert ret.status_code == 404

    def test_authors_get_filter(self, test_client):
        """GET AUTHORS  WITH FILTERS"""
        ret = test_client.get(AUTHORS_URL,
                              query_string={'first_name': TestApi.author_1.get("first_name")}
                              )
        assert ret.status_code == 200
        ret_val = ret.json

        assert len(ret_val) == 1
        assert set(v['id'] for v in ret_val) == {TestApi.author_1_id}

    def test_books_url(self, test_client):
        """GET BOOKS"""
        ret = test_client.get(BOOKS_URL)
        assert ret.status_code == 200
        # assert ret.json == []

    def test_books_post(self, test_client):
        """POST AUTHORS"""
        TestApi.book_1 = {
            'title': 'Ghostbusters',
            'author_id': TestApi.author_1_id
        }
        headers_jwt = {
            'Authorization': 'Bearer {}'.format(TestApi.jwt_token),
        }

        ret = test_client.post(BOOKS_URL, json=TestApi.book_1, headers=headers_jwt)
        assert ret.status_code == 201
        ret_val = ret.json
        TestApi.book_1_id = ret_val.pop('id')
        TestApi.book_1_etag = ret.headers['ETag']
        ret_val.pop('created_at')
        ret_val.pop('updated_at')
        assert ret_val == TestApi.book_1

    def test_books_post2(self, test_client):
        """POST BOOKS AGAIN"""
        TestApi.book_2 = {
            'title': 'Ghostbusters2',
            'author_id': DUMMY_ID
        }
        headers_jwt = {
            'Authorization': 'Bearer {}'.format(TestApi.jwt_token),
        }

        ret = test_client.post(BOOKS_URL, json=TestApi.book_2, headers=headers_jwt)
        assert ret.status_code == 400

        TestApi.book_2.update({'author_id': TestApi.author_1_id})
        ret = test_client.post(BOOKS_URL, json=TestApi.book_2, headers=headers_jwt)
        assert ret.status_code == 201
        ret_val = ret.json
        TestApi.book_2_id = ret_val.pop('id')
        TestApi.book_2_etag = ret.headers['ETag']
        ret_val.pop('created_at')
        ret_val.pop('updated_at')
        assert ret_val == TestApi.book_2

    def test_books_getid(self, test_client):
        """GET BOOK BY ID"""
        ret = test_client.get(BOOKS_URL + TestApi.book_1_id)
        assert ret.status_code == 200
        assert ret.headers['ETag'] == TestApi.book_1_etag
        ret_val = ret.json
        ret_val.pop('id')
        ret_val.pop('created_at')
        ret_val.pop('updated_at')
        assert ret_val == TestApi.book_1

    def test_books_put(self, test_client):
        """PUT BOOKS"""
        TestApi.book_1.update({'title': 'Ghostbusters1-m'})
        headers_jwt = {
            'Authorization': 'Bearer {}'.format(TestApi.jwt_token),
            'If-Match': TestApi.book_1_etag
        }

        ret = test_client.put(
            BOOKS_URL + TestApi.book_1_id, json=TestApi.book_1, headers=headers_jwt
        )
        assert ret.status_code == 200
        ret_val = ret.json
        ret_val.pop('id')
        ret_val.pop('created_at')
        ret_val.pop('updated_at')
        TestApi.book_1_etag = ret.headers['ETag']
        assert ret_val == TestApi.book_1

    def test_books_put404(self, test_client):
        """PUT BOOKS with wrong ID"""
        headers_jwt = {
            'Authorization': 'Bearer {}'.format(TestApi.jwt_token),
            'If-Match': TestApi.book_1_etag
        }
        # PUT wrong ID -> 404
        ret = test_client.put(
            BOOKS_URL + DUMMY_ID, json=TestApi.book_1, headers=headers_jwt
        )
        assert ret.status_code == 404

    def test_books_put400(self, test_client):
        """PUT BOOKS WITH unknow ID"""
        headers_jwt = {
            'Authorization': 'Bearer {}'.format(TestApi.jwt_token),
            'If-Match': TestApi.book_1_etag
        }
        TestApi.book_1.update({'author_id': DUMMY_ID})

        # PUT wrong author ID -> 400
        ret = test_client.put(
            BOOKS_URL + TestApi.book_1_id, json=TestApi.book_1, headers=headers_jwt
        )
        assert ret.status_code == 400

    def test_books_get_filter_authorid(self, test_client):
        """GET books with author_id 1 filter"""
        ret = test_client.get(BOOKS_URL, query_string={'author_id': TestApi.author_1_id})
        assert ret.status_code == 200
        ret_val = ret.json

        assert len(ret_val) == 2
        assert set(v['id'] for v in ret_val) == {TestApi.book_1_id, TestApi.book_2_id}

    def test_books_delete(self, test_client):
        """DELETE BOOKS"""
        headers_jwt = {
            'Authorization': 'Bearer {}'.format(TestApi.jwt_token),
            'If-Match': TestApi.book_1_etag
        }
        # DELETE
        ret = test_client.delete(
            BOOKS_URL + TestApi.book_1_id, headers=headers_jwt
        )
        assert ret.status_code == 204

    def test_authors_delete(self, test_client):
        """DELETE AUTHORS  ==> DELETE BOOKS with cascade"""
        headers_jwt = {
            'Authorization': 'Bearer {}'.format(TestApi.jwt_token),
            'If-Match': TestApi.author_1_etag
        }
        # DELETE
        ret = test_client.delete(
            AUTHORS_URL + TestApi.author_1_id, headers=headers_jwt
        )
        assert ret.status_code == 204

        # GET by id authors -> 404
        ret = test_client.get(AUTHORS_URL + TestApi.author_1_id)
        assert ret.status_code == 404

        # GET by id books -> 404
        ret = test_client.get(BOOKS_URL + TestApi.book_1_id)
        assert ret.status_code == 404
