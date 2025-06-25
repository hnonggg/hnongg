<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>FinGPT - Chuyên gia tài chính của bạn</title>
  <style>
    body { font-family: Arial, sans-serif; background: #e3f2fd; margin: 0; padding: 0; }
    .container { max-width: 600px; margin: 40px auto; background: white; padding: 20px; border-radius: 12px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
    h1 { text-align: center; color: #1976d2; }
    .chat-box { border: 1px solid #ccc; padding: 10px; height: 400px; overflow-y: auto; background: #f9f9f9; margin-bottom: 10px; border-radius: 8px; }
    .user, .bot { margin: 10px 0; padding: 10px; border-radius: 8px; }
    .user { background: #bbdefb; text-align: right; }
    .bot { background: #c8e6c9; text-align: left; }
    input[type=text] { width: 100%; padding: 10px; border-radius: 8px; border: 1px solid #ccc; }
    button { padding: 10px 20px; margin-top: 10px; background: #1976d2; color: white; border: none; border-radius: 8px; cursor: pointer; }
  </style>
</head>
<body>
  <div class="container">
    <h1>💰 FinGPT - Chuyên gia tài chính của bạn</h1>
    <div class="chat-box" id="chat"></div>
    <input type="text" id="input" placeholder="Hỏi về đầu tư, tiết kiệm, chứng khoán..." />
    <button onclick="sendMessage()">Gửi</button>
  </div>

  <script>
    const chatBox = document.getElementById('chat');
    const inputBox = document.getElementById('input');

    async function sendMessage() {
      const userText = inputBox.value.trim();
      if (!userText) return;
      appendMessage(userText, 'user');
      inputBox.value = '';

      const messages = [
        { role: 'system', content: 'Bạn là FinGPT, chuyên gia tư vấn tài chính chuyên nghiệp. Hãy trả lời bằng tiếng Việt chuẩn, súc tích, đáng tin cậy, hỗ trợ người dùng trong các lĩnh vực đầu tư, tiết kiệm, tài chính cá nhân, chứng khoán và thị trường.' },
        { role: 'user', content: userText }
      ];

      try {
        const res = await fetch('https://openrouter.ai/api/v1/chat/completions', {
          method: 'POST',
          headers: {
            'Authorization': 'Bearer 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',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            model: 'mistralai/mistral-small-3.2-24b-instruct-2506',
            messages: messages,
            max_tokens: 700,
            temperature: 0.75
          })
        });

        const data = await res.json();
        const reply = data.choices?.[0]?.message?.content || '[Lỗi khi lấy dữ liệu từ AI]';
        appendMessage(reply, 'bot');
      } catch (err) {
        appendMessage('[Lỗi kết nối API]', 'bot');
        console.error(err);
      }
    }

    function appendMessage(text, sender) {
      const msg = document.createElement('div');
      msg.className = sender;
      msg.textContent = text;
      chatBox.appendChild(msg);
      chatBox.scrollTop = chatBox.scrollHeight;
    }
  </script>
</body>
</html>
