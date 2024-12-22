function register() {
  const username = document.querySelector("#username").value;
  const password = document.querySelector("#password").value;
  const gender = document.querySelector("#gender").value;
  const age = document.querySelector("#age").value;

  if (!username) {
    alert("아이디를 입력해주세요!");
  } else if (!password) {
    alert("비밀번호를 입력해주세요!");
  } else if (!gender) {
    alert("성별을 선택해주세요!");
  } else if (!age) {
    alert("나이를 입력해주세요!");
  } else {
    $.post("./api/register", {
      username: username,
      password: password,
      gender: gender,
      age: age,
    }).done(function (data) {
      if (data == "회원가입이 완료되었습니다.") {
        alert(data);
        location.href = "./login";
      } else {
        console.log(data);
      }
    });
  }
}

function login() {
  const username = document.querySelector("#username").value;
  const password = document.querySelector("#password").value;

  if (!username) {
    alert("아이디를 입력해주세요!");
  } else if (!password) {
    alert("비밀번호를 입력해주세요!");
  } else {
    $.post("./api/login", {
      username: username,  
      password: password  
    }).done(function (data) {
        if(data == "로그인이 완료되었습니다.") {
            alert(data);
            location.href = "./";
        } else {
            console.log(data);
        }
    })
  }
}
