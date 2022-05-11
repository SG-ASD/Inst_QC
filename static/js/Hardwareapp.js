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
            <option value="">--항목 선택--</option>
            <option value="Packaging Condition">1) Packaging Condition</option>
            <option value="Appearance of instrument">2) Appearance of instrument</option>
            <option value="Instrument Accessories Kits">3) Instrument Accessories Kits</option>`;
    }
    else if (obj.value == "Electrical Test") {
        document.getElementById("inspection_subcategory").innerHTML = `
            {% load static %}
            <option value="">--항목 선택--</option>
            <option value="Electrical Test" href="{% url 'Electricalapp:update' target_Appearance.Instrument_SN_id %}">1) Electrical Test</option>
            <option value="{{ obj.value }}" href="{% url 'Electricalapp:update' target_Appearance.Instrument_SN_id %}">{{ obj.value }}</option>`;
    }
    else if (obj.value == "Hardware Adjustment") {
        document.getElementById("inspection_subcategory").innerHTML = `
            <option value="">--항목 선택--</option>
            <option value="Hardware Adjustment">1) Hardware Adjustment</option>`;
    }
    else if (obj.value == "Performance Verification") {
        document.getElementById("inspection_subcategory").innerHTML = `
            <option value="">--항목 선택--</option>
            <option value="Performance Verification">1) Performance Verification</option>`;
    }
    else if (obj.value == "Attachment") {
        document.getElementById("inspection_subcategory").innerHTML = `
            <option value="">--항목 선택--</option>
            <option value="Attachment">1) Attachment</option>`;
    }
    else if (obj.value == "Accessories Kits") {
        document.getElementById("inspection_subcategory").innerHTML = `
            <option value="">--항목 선택--</option>
            <option value="Accessories Kits">1) Accessories Kits</option>`;
    }
}

/**
 * 검사성적서의 하위 select list에서 subcategory 선택 시
 * 해당 하위 subcategory 화면으로 이동
 *
 * @param obj - 선택한 subcategory
 */
function select_subcategory(obj) {
    alert(obj.value)
    alert(obj.href)
    if (obj.value == "Electrical Test"){
        document.location.href = "http://127.0.0.1:8000/QC/";
        // document.location.href = "{% url 'Electricalapp:update' target_Appearance.Instrument_SN_id %}"
    }
}


function onchange_check() {
    const ElectricalTest_HiPotential = document.getElementById('ElectricalTest_HiPotential1');
    const ElectricalTest_GroundResistance = document.getElementById('ElectricalTest_GroundResistance1');
    const ElectricalTest_PowerSWFunction = document.getElementById('ElectricalTest_PowerSWFunction1');
    const ElectricalTest_PowerLED = document.getElementById('ElectricalTest_PowerLED1');


    ElectricalTest_HiPotential.click()
    ElectricalTest_GroundResistance.click()
    ElectricalTest_PowerSWFunction.click()
    ElectricalTest_PowerLED.click()
}

function Cal_Get_Info(obj) {
    const Calibration_Txt = document.getElementById('HardWare_CalibrationTool')
    Calibration_Txt.value = obj.value
}
function Barcode_Get_Info(obj) {
    const Barcode_Txt = document.getElementById('HardWare_BarcodeCarrier')
    Barcode_Txt.value = obj.value

}