# Week 1 Submission

## What I Learned

- How to connect to an AI model using an API key
- What tokens are — every word costs tokens, longer input = more cost
- The model has no memory between separate calls — you have to resend history every time
- How a `messages` list works: system sets rules, user asks, assistant replies
- Streaming — printing words as they arrive instead of waiting for the full reply
- How to summarize old context to save tokens (compaction)

## Problems I Faced and Fixed

- **Typo `"conent"` instead of `"content"`** — crashed on first run, spotted and fixed
- **`pass` instead of `return`** — function returned `None`, added the correct return line
- **Wrong model name `deepseek-v4-flash:free`** — got 404, switched to a working model
- **Appending system message in the loop instead of user message** — model was getting duplicate system prompts
- **API call happening before user message was appended** — model didn't see the latest message, fixed the order
- **`compact=False` referenced before assignment** — would crash if `/compact` never typed, fixed by checking `user_text` directly
- **`end=" "` adding extra spaces between tokens** — names like Saksham printed as `S a k s h a m`, fixed to `end=""`
- **Nested list bug in compaction slice** — `[messages[0] + messages[...]]` tried to add a dict to a list, fixed with `[messages[0]] + messages[-(2*N):]`
- **Gemini model unavailable on OpenRouter** — tested all three models, removed the broken one
