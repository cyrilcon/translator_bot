import aiohttp

from config import config


async def translate_text(text: str) -> str:
    async with aiohttp.ClientSession() as session:
        payload = {
            "q": text,
            "source": "ru",
            "target": "en",
            "format": "text",
        }
        async with session.post(config.api_url, json=payload) as response:
            if response.status == 200:
                data = await response.json()
                return data.get("translatedText", "Ошибка перевода")
            else:
                return "Ошибка при обращении к серверу перевода"
