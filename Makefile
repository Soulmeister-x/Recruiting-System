.RECIPEPREFIX = >
build:
>   source .venv/bin/activate
server:
>   build
>   python server_endpoint.py
client:
>   build
>   python client.py
