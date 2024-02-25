# Simple API

<img src="image/personal_data.jpg" alt="Alt Text">


Simple HTTP API for playing with `User` model.

Basic authentication is a straightforward authentication scheme integrated into the HTTP protocol, allowing an HTTP user agent, like a web browser, to provide a username and password with a request. In this method, the username and password are joined with a colon, base64-encoded, and sent in the Authorization header of the HTTP request. However, since base64 encoding is easily reversible, Basic Authentication is considered insecure over unencrypted connections, making it essential to use it over HTTPS to protect credentials from interception. Although simple and widely supported, Basic Authentication's lack of features such as token expiration and revocation makes it less suitable for complex or security-sensitive applications


## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints


## Setup

```
$ pip3 install -r requirements.txt
```


## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```


## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)

## Authors

- [Mouayed sabbagh](https://github.com/MOUAYEDSB)
