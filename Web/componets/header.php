<header>
    <ul>
        <li><a href="FaceRecognition">표정분석하기</a></li>
        <li><a href="emotionDiary">감정일기쓰기</a></li>
    </ul>
    <ul>
        <?php
        if(isset($_SESSION["user_idx"])) {
            echo "<li><a href='myPage'>마이페이지</a></li>";
            echo "<li><a href='logout'>로그아웃</a></li>";
        } else {
            echo "<li><a href='login'>로그인</a></li>";
            echo "<li><a href='register'>회원가입</a></li>";
        }
        ?>
    </ul>
</header>