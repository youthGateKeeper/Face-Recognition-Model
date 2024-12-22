<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];

    $sql = "SELECT * FROM users WHERE username = :username AND password = :password";
    $stmt = $pdo->prepare($sql);
    $stmt->bindParam(":username", $username);
    $stmt->bindParam(":password", $password);
    $stmt->execute();
    $result = $stmt->fetch(PDO::FETCH_ASSOC);

    if(!$result) {
        echo "아이디와 비밀번호를 확인해주세요!";
    } else {
        $_SESSION["user_idx"] = $result["user_idx"];
        echo "로그인이 완료되었습니다.";
    }

}