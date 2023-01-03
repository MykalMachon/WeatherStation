from sys import argv

import uvicorn

from .main import app

if __name__ == "__main__":
  if "--test" in argv:
    print("🧪 Running in test mode...")
    uvicorn.run('main:app', host="localhost", port=5000, log_level="debug", reload=True)
  else:
    print("🚀 Running in production mode...")
    uvicorn.run(app, host="localhost", port=5000, log_level="info")
    