# 🛡️ NSFW Image Moderation API (FastAPI)

Простое backend-приложение на FastAPI, которое принимает изображение и проверяет его на наличие неприемлемого (NSFW) контента через API DeepAI.

---

## 📌 Функциональность

- POST `/moderate` — приём `.jpg` или `.png` изображения.
- Отправка изображения в DeepAI NSFW Detector API.
- Возврат статуса:
  - `{"status": "OK"}` — изображение безопасно
  - `{"status": "REJECTED", "reason": "NSFW content"}` — обнаружен неприемлемый контент

---

## ⚙️ Установка и запуск

### 1. Клонируй репозиторий:

```bash
git clone https://github.com/your_username/nsfw-detector.git
cd nsfw-detector
````

### 2. Установи зависимости:

```bash
pip install -r requirements.txt
```

### 3. Получи API-ключ

Зарегистрируйся на [https://deepai.org/](https://deepai.org/) и получи бесплатный ключ.

### 4. Создай файл `.env` в корне проекта:

```ini
DEEPAI_API_KEY=your_deepai_key_here
```

### 5. Запусти сервер:

```bash
uvicorn app.main:app --reload
```

---

## 🧪 Пример запроса (через `curl`):

```bash
curl -X POST -F "file=@cat.jpg" http://localhost:8000/moderate
```

---

## 📝 Ответы API

| Статус     | Описание            |
| ---------- | ------------------- |
| `OK`       | Контент безопасен   |
| `REJECTED` | Найден NSFW-контент |

---

## 🧠 Технические детали

* Используется `nsfw_score` из DeepAI:

  * `> 0.7` — контент считается неприемлемым
  * `≤ 0.7` — безопасный
* Обработка ошибок API и форматов изображений

---

## 📂 Структура проекта

```
ai-nsfw-detector/
├── app/
│   └── main.py
├── requirements.txt
├── README.md
├── .env (в .gitignore)
```

---

## 🛑 Внимание

* Не публикуй `.env` и API-ключи в открытом доступе!
* При использовании бесплатного API — возможно ограничение по количеству запросов.

---

## 🧑‍💻 Автор

Михаил Шабалин
Telegram: [@m1hael_AI](https://t.me/m1hael_AI)
GitHub: [https://github.com/your\_username](https://github.com/your_username)

