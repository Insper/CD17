
  // Initialize Firebase
  var config = {
    apiKey: "AIzaSyBg8FLM_Lg", // Use sua própria API Key
    authDomain: "teste-ab.firebaseapp.com",
    databaseURL: "https://teste-ab.firebaseio.com",
    storageBucket: "teste-ab.appspot.com",
    messagingSenderId: "313208609268"
  };
  firebase.initializeApp(config);

  database = firebase.database();

  logs = this.database.ref('logs');

 function envia(tipo_evt, user_id_var, tempo_var, versao_var){
  this.logs.push(
  {
  user_id: user_id_var,
  tempo: tempo_var,
  versao: versao_var,
  tipo: tipo_evt
  }
  );
 }


function tempo_inicial(){
  // definir tempo inicial
  var d = Date.now();
  // enviar para Firebase
  envia("inicio", id_pessoa, d, versao);
}

