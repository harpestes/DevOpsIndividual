from molotov import scenario
import json

BASE_URL = "http://172.19.128.1:3141"


@scenario(10)
async def test_server_returns_json(session):
    async with session.get(BASE_URL) as response:
        assert response.status == 200, f"Очікувався 200, отримано {response.status}"

        data = await response.text()

        try:
            json.loads(data)
        except json.JSONDecodeError:
            assert False, f"Невірний формат відповіді (не JSON): {data}"

        print("Сервер повертає валідний JSON і статус 200")