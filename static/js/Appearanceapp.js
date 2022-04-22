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
            <option value="Packaging Condition">Packaging Condition</option>
            <option value="Appearance of instrument">Appearance of instrument</option>
            <option value="Instrument Accessories Kits">Instrument Accessories Kits</option>`;
    }
    else if (obj.value == "Electrical Test") {
        document.getElementById("inspection_subcategory").innerHTML = `
            <option value="Electrical Test">Electrical Test</option>`;
    }
    else if (obj.value == "Hardware Adjustment") {
        document.getElementById("inspection_subcategory").innerHTML = `
            <option value="Hardware Adjustment">Hardware Adjustment</option>`;
    }
    else if (obj.value == "Performance Verification") {
        document.getElementById("inspection_subcategory").innerHTML = `
            <option value="Performance Verification">Performance Verification</option>`;
    }
    else if (obj.value == "Attachment") {
        document.getElementById("inspection_subcategory").innerHTML = `
            <option value="Attachment">Attachment</option>`;
    }
    else if (obj.value == "Accessories Kits") {
        document.getElementById("inspection_subcategory").innerHTML = `
            <option value="Accessories Kits">Accessories Kits</option>`;
    }
}