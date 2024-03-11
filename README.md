# Special Test Tool

### You'll have to excuse the name, while I don't condone cheating I made this tool for someone for someone to assist them in their studies.

# Dependencies

* [pytesseract](https://pypi.org/project/pytesseract/)
* [openai-python](https://github.com/openai/openai-python)
* [PyQt6](https://pypi.org/project/PyQt6/)
* A screenshot tool (I tested this with [ShareX](https://getsharex.com/))


# How it works

I'll write a more lengthy explanation later but it works like this

Take screenshot of question using screenshot tool -> parse text from screenshot using pytesseract -> make API call to openai with the question -> return answer according to the prompt defined in tool_funcs.py
