# WebSocket

---
## 基础

```python
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi import (
    Cookie,
    Depends,
    FastAPI,
    Query,
    WebSocket,
    WebSocketException,
    status,
)
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()  # 客户端

    try:
        while True:
            data = await websocket.receive_text()  # 等待消息
            await websocket.send_text('Message')  # 发送消息

    # 断开连接
    except WebSocketDisconnect:
        pass
```

!!! none "抛出异常"

    ```python
    raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
    ```