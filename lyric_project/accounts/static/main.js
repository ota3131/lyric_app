// main.js

// SweetAlertを使った共通アラート関数
function showAlert(title, text, icon = "info") {
  swal({
    title: title,
    text: text,
    icon: icon,
  });
}

// 例：すばらしい通知を表示する関数
function amazingSample() {
  showAlert("すばらしい！！", "You clicked the button!", "success");
}

// 他の用途で呼び出す例
// showAlert("エラー", "予期せぬエラーが発生しました。", "error");
// showAlert("確認", "本当に実行しますか？", "warning");
