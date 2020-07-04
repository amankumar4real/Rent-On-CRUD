from app import create_app

config_name = "development"

app = create_app(config_name)


@app.route("/")
def Home():
    return "Home"


if __name__ == "main":
    app.run()
