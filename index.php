<?php
session_start();
include("./Web/config/DBconnect.php");

$request = $_SERVER['REQUEST_URI'];
$path = explode("?", $request);
$path[1] = isset($path[1]) ? $path[1] : null;
$resource = explode("/", $path[0]);

$page = "";

if ($resource[1] == "api") {
    switch ($resource[2]) {
        case "register":
            $page = "./Web/api/register.php";
            break;
        case "login":
            $page = "./Web/api/login.php";
            break;
        default:
            echo "잘못된 api 접근입니다.";
            return 0;
    }
    include $page;
} else {
    switch ($resource[1]) {
        case "":
            $page = "./Web/pages/index.php";
            break;
        case "login":
            $page = "./Web/pages/login.php";
            break;
        case "logout":
            $page = "./Web/pages/logout.php";
            break;
        case "register":
            $page = "./Web/pages/register.php";
            break;
        case "myPage":
            $page = "./Web/pages/myPage.php";
            break;
        case "FaceRecognition":
            $page = "./Web/pages/FaceRecognition.php";
            break;
        case "emotionDiary":
            $page = "./Web/pages/emotionDiary.php";
            break;
        default:
            echo "잘못된 접근입니다.";
            return 0;
    }
    include("./Web/componets/header.php");
    include $page;
    include("./Web/componets/footer.php");
}
