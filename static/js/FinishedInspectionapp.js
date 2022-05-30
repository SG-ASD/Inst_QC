'use strict';

/**
 * 저장 버튼 클릭 시 팝업창 띄우기
 */
function alert_save(){
    alert("저장되었습니다.")
}



function Barcode_Scanner_Get_Info(obj) {
    debugger
    const Barcode_Scanner_Txt = document.getElementById('Barcode_Scanner')
    Barcode_Scanner_Txt.value = obj.value
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

/**
 * All Pass 체크 시 하위 체크박스에 체크 표시
 */
function onchange_check_finished_report() {
    debugger
    const Computer_Version = document.getElementById('Computer_Version1');
    const SL_Install = document.getElementById('SL_Install1');
    const Method_Import = document.getElementById('Method_Import1');
    const SL_Maintenance_Screen = document.getElementById('SL_Maintenance_Screen1');
    const SL_Home_Screen = document.getElementById('SL_Home_Screen1');
    const SL_mode = document.getElementById('SL_mode1');
    const SL_Protocol = document.getElementById('SL_Protocol1');
    const SL_Setting_Screen = document.getElementById('SL_Setting_Screen1');
    const SL_Trace = document.getElementById('SL_Trace1');
    const Condition = document.getElementById('Condition1');
    const HHS_Labeled = document.getElementById('HHS_Labeled1');
    const Label_Option = document.getElementById('Label_Option1');
    const UDI_Barcode = document.getElementById('UDI_Barcode1');
    const UDI_HRI = document.getElementById('UDI_HRI1');

    Computer_Version.click()
    SL_Install.click()
    Method_Import.click()
    SL_Maintenance_Screen.click()
    SL_Home_Screen.click()
    SL_mode.click()
    SL_Protocol.click()
    SL_Setting_Screen.click()
    SL_Trace.click()
    Condition.click()
    HHS_Labeled.click()
    Label_Option.click()
    UDI_Barcode.click()
    UDI_HRI.click()
}

