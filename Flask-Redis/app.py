import socket
import os

app = Flask(__name__)
redis = Redis(host=os.environ.get("REDIS_HOST","127.0.0.1"),port= 6379)

@app.route("/hello")
def hello():
    redis.incr("hits")
    return "hostname[%s] visit %s times.\n" %redis.get("hits"),socket.gethostname

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)