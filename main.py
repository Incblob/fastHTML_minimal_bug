from fasthtml.common import *

app = FastHTML()


@app.get("/")
def home():
    return Main(Img(src="/test.jpg"))


serve(port=5002)
