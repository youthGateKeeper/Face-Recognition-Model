<?php
if(!$_SESSION["user_idx"]) {
    echo "<script>alert('로그인 후 이용 가능한 페이지 입니다.');</script>";
    header("./login");
} else { ?>
    <!DOCTYPE html>
    <html lang="ko">
    
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" cwqontent="width=device-width, initial-scale=1.0">
        <title>감정일기쓰기</title>
        <link rel="stylesheet" href="../style.css">
    </head>
    
    <body>
        <div>
            <h3>내가 쓴 감정일기</h3>
        </div>
        <script src="../script.js"></script>
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    </body>
    
    </html>
<?php
}
?>