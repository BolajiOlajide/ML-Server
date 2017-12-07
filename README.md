## ML-Server

### Installation
Setting up the `ML-Server` if you follow the instructions laid out below:

- Create a `virtual-environment` for the application, ensure it is a python3 environment
- Install the project's dependencies with the command `pip install -r requirements.txt` via your terminal
- You can make a copy of the `.env.sample` file and name it  `.env` and in this file you set the PORT to your choice.
- After this is done, you can start the application with the command `python main.py` via your terminal

### Endpoints
The following Endpoints are available:

#### Emulate ML Model
###### POST HTTP Request
-   `POST /ml`
`INPUT`: As defined in [input_data.json](https://github.com/BolajiOlajide/ML-Server/blob/master/input_data.json)
    ###### HTTP Response
-   HTTP Status: `200: OK`
-   JSON data
```json
{
  "data": [
    {
      "Predict": 1,
      "Userid": 1
    },
    {
      "Predict": 0,
      "Userid": 2
    }
  ]
}
```

###### POST HTTP Request
-   `POST /login`
`INPUT`: As defined in [input_data.json](https://github.com/BolajiOlajide/ML-Server/blob/master/input_data.json)
    ###### HTTP Response
-   HTTP Status: `200: OK`
-   JSON data
```json
{
  "openid": "<open-id>"
}
```
