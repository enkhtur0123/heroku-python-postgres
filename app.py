from flask import Flask, render_template
import connecttodb

app = Flask(__name__)

@app.route("/")
def index():
    
    # Load current count
    f = open("count.txt", "r")
    count = int(f.read())
    f.close()

    # Increment the count
    count += 1

    # Overwrite the count
    f = open("count.txt", "w")
    f.write(str(count))
    f.close()

    count = connecttodb.rowcount()
    url = connecttodb.getdatabaseurl()
    # Render HTML with count variable
    return render_template("index.html", count=count, url=url)

@app.route('/api/databaseurl', methods=['GET'])
def api_url():
    return connecttodb.getdatabaseurl()


if __name__ == "__main__":
    app.run()