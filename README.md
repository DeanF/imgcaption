This python package gets image captions from Microsoft's CaptionBot service

Usage Example:
```python
import imgcaption
caption_api = imgcaption.API()
print(caption_api.get_url_caption('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Bing_logo.svg/2000px-Bing_logo.svg.png'))
I am not really confident, but I think it's a sign on a pole.
```