from time import time
from datetime import datetime

current_time = time()
formatted_time = datetime.now().strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {current_time} or {current_time:.2e}")
print(formatted_time)
