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
function onchange_check_packaging() {
    const Appearance_Shock_Watch = document.getElementById('Appearance_Shock_Watch1');
    const Appearance_Binding = document.getElementById('Appearance_Binding2');
    const Appearance_Labels = document.getElementById('Appearance_Labels2');
    const Appearance_Packaging_Box = document.getElementById('Appearance_Packaging_Box1');
    const Appearance_Wooden_Pallet = document.getElementById('Appearance_Wooden_Pallet1');
    const Appearance_Transport_Jig = document.getElementById('Appearance_Transport_Jig2');

    Appearance_Shock_Watch.click()
    Appearance_Binding.click()
    Appearance_Labels.click()
    Appearance_Packaging_Box.click()
    Appearance_Wooden_Pallet.click()
    Appearance_Transport_Jig.click()
}

function onchange_check_unpacking() {
    debugger
    const Appearance_Front = document.getElementById('Appearance_Front1');
    const Appearance_Top = document.getElementById('Appearance_Top1');
    const Appearance_Right = document.getElementById('Appearance_Right1');
    const Appearance_Left = document.getElementById('Appearance_Left1');
    const Appearance_Back = document.getElementById('Appearance_Back1');
    const Appearance_Acc_Damage = document.getElementById('Appearance_Acc_Damage1');
    const Appearance_Acc_Missing = document.getElementById('Appearance_Acc_Missing1');

    Appearance_Front.click()
    Appearance_Top.click()
    Appearance_Right.click()
    Appearance_Left.click()
    Appearance_Back.click()
    Appearance_Acc_Damage.click()
    Appearance_Acc_Missing.click()
}