<!DOCTYPE html>
<html lang="ko">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>회원가입</title>
    <link rel="stylesheet" href="../style.css">
</head>

<body>
    <div class="main">
        <div class="login">
            <h2>회원가입</h2>
            <input id="username" class="inputStyle" type="text" placeholder="username">
            <input id="password" class="inputStyle" type="password" placeholder="password">
            <select class="inputStyle" name="gender" id="gender">
                <option value="">gender</option>
                <option value="남">남</option>
                <option value="여">여</option>
            </select>
            <input id="age" class="inputStyle" type="text" placeholder="age">
            <button onclick="register()">회원가입</button>
        </div>
    </div>
    <script src="../script.js"></script>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</body>

</html>