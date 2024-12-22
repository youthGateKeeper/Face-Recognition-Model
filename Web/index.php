<?php
session_start();
include("./config/DBconnect.php");

$request = $_SERVER['REQUEST_URI'];
$path = explode("?", $request);
$path[1] = isset($path[1]) ? $path[1] : null;
$resource = explode("/", $path[0]);

$page = "";

if ($resource[1] == "api") {
    switch ($resource[2]) {
        case "register":
            $page = "./api/register.php";
            break;
            case "login":
                $page = "./api/login.php";
                break;
        default:
            echo "잘못된 api 접근입니다.";
            return 0;
    }
    include $page;
} else {
    switch ($resource[1]) {
        case "":
            $page = "./pages/index.php";
            break;
        case "login":
            $page = "./pages/login.php";
            break;
        case "register":
            $page = "./pages/register.php";
            break;
        case "myPage":
            $page = "./pages/myPage.php";
            break;
        case "FaceRecognition":
            $page = "./pages/FaceRecognition.php";
            break;
        case "emotionDiary":
            $page = "./pages/emotionDiary.php";
            break;
        default:
            echo "잘못된 접근입니다.";
            return 0;
    }
    include("./componets/header.php");
    include $page;
    include("./componets/footer.php");
}
