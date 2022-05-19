'use strict';

/**
 * 저장 버튼 클릭 시 팝업창 띄우기
 */
function alert_save(){
    alert("저장되었습니다.")
}

/**
 * Tool 선택 시
 */
function Cal_Get_Info(obj) {
    const Calibration_Txt = document.getElementById('HardWare_CalibrationTool')
    Calibration_Txt.value = obj.value
}

function Barcode_Get_Info(obj) {
    const Barcode_Txt = document.getElementById('HardWare_BarcodeCarrier')
    Barcode_Txt.value = obj.value
}
function Cal_Get_Info(obj) {
    const Calibration_Txt = document.getElementById('HardWare_CalibrationTool')
    Calibration_Txt.value = obj.value
}

function openTextFile() {
    let input = document.querySelector('input');
    let textarea = document.querySelector('textarea')

    input.addEventListener('change', () => {
       let files = input.files;
       if(files.length == 0 ) return;

       const  file = files[0];

       let reader = new FileReader();

       reader.onload = (e) => {
           const file = e.target.result;
           const lines = file.split(/\r\n|\n/);
           textarea.value = lines.join('\n');
       };
       reader.onerror = (e) => alert(e.target.error.name);
       reader.readAsText(file);
    });
}
