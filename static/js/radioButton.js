
  /*選択済みのラジオボタンを押した際に、選択を解除する*/
  let beforeRadioButton = {};//これにラジオボタンのnameと前回のIDがセットで入る

  function doubleSelect(button){
    let nowRadioId = button.id;//現在のラジオボタンのidを取得
    let nowRadioName = button.name;//現在のラジオボタンのnameを取得

    if(! beforeRadioButton[nowRadioName]){//jsonに元からないと初期化
      beforeRadioButton[nowRadioName] = -1;
    }
    if(beforeRadioButton[nowRadioName] == nowRadioId){
      button.checked = false;
      beforeRadioButton[nowRadioName] = -1;
    }else{
      beforeRadioButton[nowRadioName] =nowRadioId;
    }
  }
