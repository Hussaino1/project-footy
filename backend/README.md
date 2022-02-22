# Backend API

- [Backend API](#backend-api)
  - [Summary](#summary)
  - [`GET`](#get)
    - [`/read/allPlayers`](#readallplayers)
    - [`/read/player/{id}`](#readplayerid)
  - [`POST`](#post)
    - [`/create/player`](#createplayer)
  - [`PUT`](#put)
    - [`/update/player/{id}`](#updateplayerid)
    - [`/complete/player/{id}`](#completeplayerid)
  - [`DELETE`](#delete)
    - [`/delete/player/{id}`](#deleteplayerid)

## Summary

| URL                     | Method   | Request Body               |
| ----------------------- | -------- | -------------------------- |
| `/read/allPlayers`        | `GET`    | None                       |
| `/read/player/{id}`       | `GET`    | None                       |
| `/create/player`          | `POST`   | `{"description": <value>}` |
| `/update/player/{id}`     | `PUT`    | `{"description": <value>}` |
| `/complete/player/{id}`   | `PUT`    | None                       |
| `/incomplete/player/{id}` | `PUT`    | None                       |
| `/delete/player/{id}`     | `DELETE` | None                       |

## `GET`

### `/read/allPlayers`

Example Response

```json
{
    "players": [
        {
            "id": 1,
            "description": "Harry Kane",
            "completed": "true"
        },
        {
            "id": 2,
            "description": "Steven Gerrard",
            "completed": "false"
        }
    ]
}
```

### `/read/player/{id}`

Path Parameters

| Parameter | Description                                |
| --------- | ------------------------------------------ |
| `{id}`    | ID for the player to query from the database |

Example Response

```json
{
    "id": 1,
    "description": "Harry Kane",
    "completed": "true"
}
```

## `POST`

### `/create/player`

Example Request

```json
{
    "description": "Harry Kane"
}
```

Example Response

```text
Added player with description: Harry Kane
```

## `PUT`

### `/update/player/{id}`

Path Parameters

| Parameter | Description                                |
| --------- | ------------------------------------------ |
| `{id}`    | ID for the player to query from the database |

Example Request

```json
{
    "description": "Steven Gerrard"
}
```

Example Response

```text
Updated player (ID: 1) with description: Harry Kane
```

### `/complete/player/{id}`

Path Parameters

| Parameter | Description                                |
| --------- | ------------------------------------------ |
| `{id}`    | ID for the player to query from the database |

Example Response

```text
Player with ID: 1 set to completed = False
```


## `DELETE`

### `/delete/player/{id}`

Path Parameters

| Parameter | Description                                |
| --------- | ------------------------------------------ |
| `{id}`    | ID for the player to query from the database |

Example Response

```text
Deleted player with ID: 1
```
