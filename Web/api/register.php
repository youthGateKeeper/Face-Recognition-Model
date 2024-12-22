<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];
    $gender = $_POST["gender"];
    $age = $_POST["age"];

    $sql = "INSERT INTO users (username, password, gender, age) VALUES (?, ?, ?, ?)";
    $stmt = $pdo->prepare($sql);
    $stmt->execute([$username, $password, $gender, $age]);

    echo "회원가입이 완료되었습니다.";
}
