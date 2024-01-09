# Gemini on Discord

## 介紹
在輸入框中輸入 `/chat`，就會出現 `message` 欄位，輸入訊息即可與 Gemini 對話。但 `message` 只能讀取單行文字，需要多行輸入的請用 `?chat {message}` 去呼叫機器人。

也能讀取圖片，在輸入框中輸入 `/see`，會出現 `image` 欄位，只要加上附件就好。也有 `message` 欄位，可選。注意讀取圖片**沒有記憶功能**。

## 專案設置

### 創建虛擬環境
我使用的 python 版本是 [3.10.13](https://www.python.org/downloads/release/python-31012/)。

以任何方式創建虛擬環境，之後執行
```
pip install requirements.txt
```

### 申請 API
1. Gemini API

    1. [Google AI](https://ai.google.dev/) 的官網。

    2. 點選 `Get API Key in Google AI Studio`。

    3. 同意服務條款後，進入 `Google AI Studio`。

    4. 點選左側的 `Get API Key`，接著點選 `Create API key in new project`，並複製 API key。如果出現 *The caller does not have permission* 的錯誤，這篇 [StackOverflow](https://stackoverflow.com/questions/77762483/the-caller-does-not-have-permission-when-creating-api-key) 的文章應該能幫助你。

2. Discord API

    1. [Discord Developer](https://discord.com/developers/applications) 的官網。

    2. 點選左側的 `Application`，再點選右上方的 `New Application`，輸入名稱，同意條款並創建。

    3. 點選左方的 `Bot`，再點選右方的 `Add Bot`，已經申請過的則沒有 `Add Bot`。

    4. 往下滑將 `MESSAGE CONTENT INTENT` 的選項開啟。

    5. 往上滑選擇 `View Token`，如果有申請過了則是 `Reset Token`

### 執行
在專案的根目錄下創建 `.env` 文件，並按照下列範例輸入你剛剛申請的 API key
```
DISCORD_API_KEY = "Your Discord Bot Token"
GEMINI_API_KEY = "Your Gemini API key"
```
然後執行 `main.py`。

## 指令集

指令 | 說明
---|---
/chat| 在輸入框輸入 `/chat` 後會出現 `message` 欄位，送出後調用 `gemini-pro`。
?chat| 輸入 `?chat` 之後空一格，後方輸入文字，支援多行輸入。
/reset| 系統會自動記錄你最新的 10 則對話紀錄，使用 `/reset` 將其全部清除。
/see| 在輸入框輸入 `/see` 後會出現 `image`，附加文件後可以選擇要不要在 `message` 欄位附加訊息，送出後調用 `gemini-pro-vision`。