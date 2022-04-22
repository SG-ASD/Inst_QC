'use strict';

/**
 * 저장 버튼 클릭 시 팝업창 띄우기
 */
function alert_save(){
    alert("저장되었습니다.")
}

/**
 * 검사성적서의 상위 select list에서 category 선택 시
 * 하위 select list에 해당 category의 subcategory 표시
 *
 * @param obj - 선택한 category
 */
function select_category(obj) {
    if (obj.value == "Appearance Inspection") {
        document.getElementById("inspection_subcategory").innerHTML = `
            <option value="Packaging Condition">1) Packaging Condition</option>
            <option value="Appearance of instrument">2) Appearance of instrument</option>
            <option value="Instrument Accessories Kits">3) Instrument Accessories Kits</option>`;
    }
    else if (obj.value == "Electrical Test") {
        document.getElementById("inspection_subcategory").innerHTML = `
            <option value="Electrical Test">1) Electrical Test</option>`;
    }
    else if (obj.value == "Hardware Adjustment") {
        document.getElementById("inspection_subcategory").innerHTML = `
            <option value="Hardware Adjustment">1) Hardware Adjustment</option>`;
    }
    else if (obj.value == "Performance Verification") {
        document.getElementById("inspection_subcategory").innerHTML = `
            <option value="Performance Verification">1) Performance Verification</option>`;
    }
    else if (obj.value == "Attachment") {
        document.getElementById("inspection_subcategory").innerHTML = `
            <option value="Attachment">1) Attachment</option>`;
    }
    else if (obj.value == "Accessories Kits") {
        document.getElementById("inspection_subcategory").innerHTML = `
            <option value="Accessories Kits">1) Accessories Kits</option>`;
    }
}

/**
 * All Pass 체크 시 하위 체크박스에 체크 표시
 */
function onchange_check() {
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