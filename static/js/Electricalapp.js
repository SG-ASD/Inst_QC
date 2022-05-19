'use strict';

/**
 * 저장 버튼 클릭 시 팝업창 띄우기
 */
function alert_save(){
    alert("저장되었습니다.")
}

/**
 * All Pass 체크 시 하위 체크박스에 체크 표시
 */
function onchange_check_electrical() {
    debugger
    const ElectricalTest_HiPotential = document.getElementById('ElectricalTest_HiPotential1');
    const ElectricalTest_GroundResistance = document.getElementById('ElectricalTest_GroundResistance1');
    const ElectricalTest_PowerSWFunction = document.getElementById('ElectricalTest_PowerSWFunction1');
    const ElectricalTest_PowerLED = document.getElementById('ElectricalTest_PowerLED1');

    ElectricalTest_HiPotential.click()
    ElectricalTest_GroundResistance.click()
    ElectricalTest_PowerSWFunction.click()
    ElectricalTest_PowerLED.click()
}
