from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'GET':
        return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Отбор астронавтов</title>
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
          crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="static/css/style1.css">
</head>
<body>
<div>
    <form class="login_form" method="post">

        <input type="text" id="surname" class="form-control" placeholder="Фамилия" name="surname">
        <input type="text" id="name" class="form-control" placeholder="Имя" name="name">
        <p></p>
        <input type="text" id="email" class="form-control" placeholder="Email" name="name">
        <div>
            <label for="edu"><br>Ваше образование</label>
            <select id="edu" class="form-control" name="education">
                <option>Высшее</option>
                <option>Среднее</option>
                <option>Начальное</option>
            </select>
        </div>


        <div class="form-group">
            <label><br>Ваши профессии:</label>
            <div class="form-group form-check">
                <input type="checkbox" class="form-check-input" id="ing" name="profession">
                <label class="form-check-label" for="ing">инженер</label>
            </div>

            <div class="form-group form-check">
                <input type="checkbox" class="form-check-input" id="pilot" name="profession">
                <label class="form-check-label" for="pilot">пилот</label>
            </div>

            <div class="form-group form-check">
                <input type="checkbox" class="form-check-input" id="builder" name="profession">
                <label class="form-check-label" for="builder">строитель</label>
            </div>

        </div>

        <div class="form-group">
            <label for="form-check"><br>Укажите пол</label>
            <div class="form-check">
                <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                <label class="form-check-label" for="male">
                    Мужской
                </label>
            </div>

            <div class="form-check">
                <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                <label class="form-check-label" for="female">
                    Женский
                </label>
            </div>
        </div>

        <div class="form-group">
            <label for="why"><br>Ваша мотивация</label>
            <textarea id="why" class="form-control" name="reason"></textarea>
        </div>

        <div class="form-group">
            <label for="photo"><br>Приложите фотографию</label>
            <input type="file" class="form-control-file" id="photo" name="file">

        </div>
        <p></p>
        <div class="form-group form-check">
            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
            <label class="form-check-label" for="acceptRules">Готов жить на Марсе</label>
        </div>
        <p></p>
        <button type="submit" class="btn btn-primary">Записаться</button>

    </form>
</div>
</body>
</html>'''
    elif request.method == 'POST':
        return 'OK'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
